# SuperBrain AI Platform – Groq Assistant
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

import os
import subprocess
import json
from datetime import datetime, timezone
from groq import Groq
from memory_encryption import encrypt_text

MEMORY_FILE = "../memory/memory_db.json"
SOURCE = "Groq"

def ensure_latest_groq():
    try:
        print("[🔄] Checking for Groq SDK updates...")
        subprocess.run(["pip", "install", "--upgrade", "groq"], check=True)
        import groq
        print(f"[ℹ️] Groq SDK version: {groq.__version__}")
    except Exception as e:
        print(f"[!] Failed to update Groq SDK: {e}")

ensure_latest_groq()

if not os.getenv("GROQ_API_KEY"):
    print("[🔐] Missing Groq API Key. Get yours at https://console.groq.com/api-keys")
    os.environ["GROQ_API_KEY"] = input("Paste Groq API Key: ")

client = Groq(api_key=os.environ["GROQ_API_KEY"])
model = os.getenv("GROQ_MODEL") or input("[🧠] Enter Groq model (default = mixtral-8x7b-32768): ") or "mixtral-8x7b-32768"

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

print("\n🤖 [Groq Assistant] — Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ("exit", "quit"):
        break
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": user_input}]
        )
        reply = response.choices[0].message.content
        print("Groq:", reply)
        save_to_memory(user_input, reply)
    except Exception as e:
        print(f"[!] Error: {e}")

__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    return "David Louis-Charles" in __author_id__
