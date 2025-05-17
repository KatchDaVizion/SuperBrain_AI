# SuperBrain AI Platform – Claude Assistant
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
import anthropic

# 🔄 Ensure latest Claude SDK (Anthropic)
def ensure_latest_anthropic():
    try:
        print("[🔄] Checking for Anthropic SDK updates...")
        subprocess.run([os.path.join(sys.prefix, "bin", "pip"), "install", "--upgrade", "anthropic", "--break-system-packages"], check=True)
        print(f"[ℹ️] Anthropic SDK version: {anthropic.__version__}")
    except Exception as e:
        print(f"[!] Failed to update Claude SDK: {e}")

ensure_latest_anthropic()

# 🔐 Encrypted API key storage
KEY_FILE = os.path.expanduser("~/.claude_api.enc")
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

def get_valid_claude_client():
    for _ in range(2):
        api_key = load_encrypted_api_key()
        if not api_key:
            print("[🔐] Missing Claude (Anthropic) API Key. Get it at https://console.anthropic.com/account/keys")
            api_key = input("Paste Claude API Key: ")
            save_encrypted_api_key(api_key)
        else:
            print("[🔑] Reusing encrypted Claude API Key.")

        try:
            client = anthropic.Anthropic(api_key=api_key)
            _ = client.models.list()
            return client
        except Exception as e:
            print(f"[!] Stored API key failed: {e}\n[↩️] Please enter a new one.")
            os.remove(KEY_FILE)

    print("[❌] Failed to authenticate after retry.")
    exit(1)

client = get_valid_claude_client()
model = os.getenv("CLAUDE_MODEL", "claude-3-opus-20240229")

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
        print("Claude:", response.content[0].text)
    except Exception as e:
        print(f"[!] Error: {e}")

__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    return "David Louis-Charles" in __author_id__
