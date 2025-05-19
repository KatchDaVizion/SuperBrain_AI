# SuperBrain AI Platform – OpenAI Assistant
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

import os
import json
import subprocess
import sys
import base64
import getpass
import hashlib
from datetime import datetime, timezone
from cryptography.fernet import Fernet
from openai import OpenAI

# 🔄 Ensure the latest OpenAI SDK is installed
def ensure_latest_openai():
    try:
        print("[🔄] Checking for OpenAI SDK updates...")
        subprocess.run([os.path.join(sys.prefix, "bin", "pip"), "install", "--upgrade", "openai", "--break-system-packages"], check=True)
        import openai
        print(f"[ℹ️] OpenAI SDK version: {openai.__version__}")
    except subprocess.CalledProcessError as e:
        print(f"[❌] Failed to update OpenAI SDK: {e}")

ensure_latest_openai()

# 🔐 Encrypted API key storage
KEY_FILE = os.path.expanduser("~/.openai_api.enc")
SECRET = hashlib.sha256(getpass.getuser().encode()).digest()
FERNET_KEY = base64.urlsafe_b64encode(SECRET[:32])
fernet = Fernet(FERNET_KEY)

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

# Load or prompt for API key
def get_valid_openai_client():
    for _ in range(2):
        api_key = load_encrypted_api_key()
        if not api_key:
            print("[🔐] Missing OpenAI API Key. Get yours at https://platform.openai.com/account/api-keys")
            api_key = input("Paste OpenAI API Key: ")
            save_encrypted_api_key(api_key)
        else:
            print("[🔑] Reusing encrypted OpenAI API Key.")

        try:
            client = OpenAI(api_key=api_key)
            models = client.models.list()
            return client
        except Exception as e:
            print(f"[!] Stored API key failed: {e}\n[↩️] Please enter a new one.")
            os.remove(KEY_FILE)

    print("[❌] Failed to authenticate after retry.")
    exit(1)

client = get_valid_openai_client()
MEMORY_FILE = "../memory/memory_db.json"
SOURCE = "OpenAI"

def save_to_memory(prompt, answer):
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
    memory = []
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            memory = json.load(f)

    memory.append({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "source": SOURCE,
        "prompt": prompt,
        "response": answer
    })

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def ask_openai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
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

# 🔒 Authorship Signature
__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    allowed_user = "David Louis-Charles"
    return allowed_user in __author_id__
