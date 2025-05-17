# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

import os
import json
import time
import openai
from datetime import datetime

MEMORY_FILE = "../memory/memory_db.json"
SOURCE = "OpenAI"

# Prompt for API Key if missing
if not os.getenv("OPENAI_API_KEY"):
    print("[🔐] Missing OpenAI API Key. Get yours at https://platform.openai.com/account/api-keys")
    os.environ["OPENAI_API_KEY"] = input("Paste OpenAI API Key: ")

openai.api_key = os.getenv("OPENAI_API_KEY")

def save_to_memory(prompt, answer):
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
    memory = []
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            memory = json.load(f)

    memory.append({
        "timestamp": datetime.utcnow().isoformat(),
        "source": SOURCE,
        "prompt": prompt,
        "response": answer
    })

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def ask_openai(prompt):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message["content"]
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
    allowed_user = "David Louis-Charles"
    return allowed_user in __author_id__
