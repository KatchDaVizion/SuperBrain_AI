# SuperBrain AI Platform – Venice Assistant
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved

import os
import json
import requests
import base64
import getpass
import hashlib
from datetime import datetime, timezone
from cryptography.fernet import Fernet

# === CONFIG ===
KEY_FILE = os.path.expanduser("~/.venice_api.enc")
SECRET = hashlib.sha256(getpass.getuser().encode()).digest()
FERNET_KEY = base64.urlsafe_b64encode(SECRET[:32])
fernet = Fernet(FERNET_KEY)
API_URL = "https://api.venice.ai/api/v1"

# === ENCRYPTED API KEY ===
def save_encrypted_api_key(api_key):
    with open(KEY_FILE, "wb") as f:
        f.write(fernet.encrypt(api_key.encode()))

def load_encrypted_api_key():
    if not os.path.exists(KEY_FILE):
        return None
    try:
        with open(KEY_FILE, "rb") as f:
            return fernet.decrypt(f.read()).decode()
    except:
        return None

def get_valid_venice_key():
    for _ in range(2):
        api_key = load_encrypted_api_key()
        if not api_key:
            print("[🔐] Missing Venice API Key. Get yours at https://venice.ai/settings/api")
            api_key = input("Paste Venice API Key: ").strip()
            save_encrypted_api_key(api_key)
        else:
            print("[🔑] Reusing encrypted Venice API Key.")

        # Quick test
        try:
            headers = {"Authorization": f"Bearer {api_key}"}
            r = requests.get(f"{API_URL}/models", headers=headers)
            if r.status_code == 200:
                return api_key
            else:
                print(f"[❌] Venice API Error: {r.status_code} - {r.text}")
        except Exception as e:
            print(f"[!] Connection error: {e}")

        os.remove(KEY_FILE)

    print("[❌] Failed to authenticate with Venice API.")
    exit(1)

# === MEMORY ===
MEMORY_FILE = "memory/memory_db.json"
SOURCE = "Venice"

def save_to_memory(prompt, answer, model):
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
    memory = []
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            memory = json.load(f)
    memory.append({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "source": SOURCE,
        "model": model,
        "prompt": prompt,
        "response": answer
    })
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

# === LIST AVAILABLE MODELS ===
def list_models(api_key):
    try:
        headers = {"Authorization": f"Bearer {api_key}"}
        r = requests.get(f"{API_URL}/models", headers=headers)
        if r.status_code == 200:
            data = r.json()
            models = data.get("models") or data
            if isinstance(models, list):
                print("[🧠] Available Venice Models:")
                for m in models:
                    if isinstance(m, dict) and "id" in m:
                        print(" -", m["id"])
            else:
                print("[!] Unexpected model format in response:", models)
        else:
            print(f"[!] Failed to list models: {r.status_code} - {r.text}")
    except Exception as e:
        print(f"[!] Error: {e}")

# === VENICE CHAT LOOP ===
def venice_chat(api_key):
    model = "llama-3.3-70b"
    temperature = 1.0
    print("\n🤖 [Venice Assistant] — Type 'exit' to quit. '/list_models' to view models, '/model <id>' to change.\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit", "quit"):
            break
        elif user_input.lower() == "/list_models":
            list_models(api_key)
            continue
        elif user_input.lower().startswith("/model "):
            new_model = user_input.split("/model ", 1)[1].strip()
            if new_model:
                model = new_model
                print(f"[✅] Switched to Venice model: {model}")
            else:
                print("[!] No model specified.")
            continue

        try:
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": model,
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ],
                "temperature": temperature
            }
            r = requests.post(f"{API_URL}/chat/completions", headers=headers, json=payload)
            if r.status_code == 200:
                reply = r.json()["choices"][0]["message"]["content"]
                print("Venice:", reply.strip())
                save_to_memory(user_input, reply, model)
            else:
                print(f"[Venice Error {r.status_code}]: {r.text}")
        except Exception as e:
            print(f"[!] Request failed: {e}")

# === ENTRY POINT ===
if __name__ == "__main__":
    api_key = get_valid_venice_key()
    venice_chat(api_key)

# 🔒 Authorship Signature
__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    return "David Louis-Charles" in __author_id__
