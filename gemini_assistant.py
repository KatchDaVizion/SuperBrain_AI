# SuperBrain AI Platform – Gemini Assistant
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

import os
import subprocess
import json
from datetime import datetime, timezone
import google.generativeai as genai
from memory_encryption import encrypt_text

MEMORY_FILE = "../memory/memory_db.json"
SOURCE = "Gemini"

def ensure_latest_gemini():
    try:
        print("[🔄] Checking for Gemini SDK updates...")
        subprocess.run(["pip", "install", "--upgrade", "google-generativeai"], check=True)
        import google.generativeai as genai
        print(f"[ℹ️] Gemini SDK version: {genai.__version__}")
    except Exception as e:
        print(f"[!] Failed to update Gemini SDK: {e}")

ensure_latest_gemini()

if not os.getenv("GEMINI_API_KEY"):
    print("[🔐] Missing Gemini API Key. Get yours at https://makersuite.google.com/app/apikey")
    os.environ["GEMINI_API_KEY"] = input("Paste Gemini API Key: ")

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model_name = os.getenv("GEMINI_MODEL") or input("[🧠] Enter Gemini model (default = gemini-pro): ") or "gemini-pro"
model = genai.GenerativeModel(model_name)

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

print("\n🤖 [Gemini Assistant] — Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ("exit", "quit"):
        break
    try:
        response = model.generate_content(user_input)
        print("Gemini:", response.text)
        save_to_memory(user_input, response.text)
    except Exception as e:
        print(f"[!] Error: {e}")

__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    return "David Louis-Charles" in __author_id__
