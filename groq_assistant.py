# SuperBrain AI Platform – Groq Assistant
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

import os
import subprocess
import sys
import base64
import getpass
import hashlib
from datetime import datetime, timezone
from cryptography.fernet import Fernet
from groq import Groq

# 🔄 Ensure latest Groq SDK
def ensure_latest_groq():
    try:
        print("[🔄] Checking for Groq SDK updates...")
        subprocess.run([
            os.path.join(sys.prefix, "bin", "pip"),
            "install", "--upgrade", "groq", "--break-system-packages"
        ], check=True)
        import groq
        print(f"[ℹ️] Groq SDK version: {groq.__version__}")
    except Exception as e:
        print(f"[!] Failed to update Groq SDK: {e}")

ensure_latest_groq()

# 🔐 Encrypted API key storage
KEY_FILE = os.path.expanduser("~/.groq_api.enc")
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
def get_valid_groq_client():
    for _ in range(2):
        api_key = load_encrypted_api_key()
        if not api_key:
            print("[🔐] Missing Groq API Key. Get yours at https://console.groq.com/api-keys")
            api_key = input("Paste Groq API Key: ")
            save_encrypted_api_key(api_key)
        else:
            print("[🔑] Reusing encrypted Groq API Key.")

        try:
            test_client = Groq(api_key=api_key)
            _ = test_client.models.list()
            return test_client
        except Exception as e:
            print(f"[!] Stored API key failed: {e}\n[↩️] Please enter a new one.")
            os.remove(KEY_FILE)

    print("[❌] Failed to authenticate after retry.")
    exit(1)

client = get_valid_groq_client()
model = os.getenv("GROQ_MODEL", "mixtral-8x7b-32768")

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
        print("Groq:", response.choices[0].message.content)
    except Exception as e:
        print(f"[!] Error: {e}")

__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    return "David Louis-Charles" in __author_id__
