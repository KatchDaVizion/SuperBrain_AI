# SuperBrain AI Platform – Claude Assistant
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

import os
import subprocess
import json
from datetime import datetime, timezone
import anthropic
from memory_encryption import encrypt_text

MEMORY_FILE = "../memory/memory_db.json"
SOURCE = "Claude"

def ensure_latest_anthropic():
    try:
        print("[🔄] Checking for Anthropic SDK updates...")
        subprocess.run(["pip", "install", "--upgrade", "anthropic"], check=True)
        import anthropic
        print(f"[ℹ️] Anthropic SDK version: {anthropic.__version__}")
    except Exception as e:
        print(f"[!] Failed to update Claude SDK: {e}")

ensure_latest_anthropic()

if not os.getenv("ANTHROPIC_API_KEY"):
    print("[🔐] Missing Claude API Key. Get it at https://console.anthropic.com/account/keys")
    os.environ["ANTHROPIC_API_KEY"] = input("Paste Claude API Key: ")

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
model = os.getenv("CLAUDE_MODEL") or input("[🧠] Enter Claude model (default = claude-3-opus-20240229): ") or "claude-3-opus-20240229"

def save_to_memory(prompt, answer):
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
    memory = []
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            memory = json.load(f)

    memory.append({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "source": SOURCE,
        "prompt": encrypt_text(prompt),
        "response": encrypt_text(answer)
    })

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

print("\n🤖 [Claude Assistant] — Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ("exit", "quit"):
        break
    try:
        response = client.messages.create(
            model=model,
            max_tokens=1000,
            messages=[{"role": "user", "content": user_input}]
        )
        reply = response.content[0].text
        print("Claude:", reply)
        save_to_memory(user_input, reply)
    except Exception as e:
        print(f"[!] Error: {e}")

__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    return "David Louis-Charles" in __author_id__
