# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

import os
import json
import subprocess
from datetime import datetime, timezone
from openai import OpenAI
from memory_encryption import encrypt_text

MEMORY_FILE = "../memory/memory_db.json"
SOURCE = "OpenAI"

def ensure_latest_openai():
    try:
        print("[🔄] Checking for OpenAI SDK updates...")
        subprocess.run(["pip", "install", "--upgrade", "openai"], check=True)
        import openai
        print(f"[ℹ️] OpenAI SDK version: {openai.__version__}")
    except subprocess.CalledProcessError as e:
        print(f"[❌] Failed to update OpenAI SDK: {e}")

ensure_latest_openai()

if not os.getenv("OPENAI_API_KEY"):
    print("[🔐] Missing OpenAI API Key. Get yours at https://platform.openai.com/account/api-keys")
    os.environ["OPENAI_API_KEY"] = input("Paste OpenAI API Key: ")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

model = os.getenv("OPENAI_MODEL")
if not model:
    model = input("[🧠] Enter OpenAI model (default = gpt-3.5-turbo): ") or "gpt-3.5-turbo"

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

def ask_openai(prompt):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[!] Error: {e}"

def chat():
    print(f"\n🤖 [OpenAI Assistant] — Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        answer = ask_openai(user_input)
        print("Assistant:", answer)
        save_to_memory(user_input, answer)

if __name__ == "__main__":
    chat()

__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    return "David Louis-Charles" in __author_id__
