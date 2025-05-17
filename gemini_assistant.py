# SuperBrain AI Platform – Gemini Assistant
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

import os
import subprocess
import sys
import base64
import getpass
import hashlib
from cryptography.fernet import Fernet
from datetime import datetime, timezone

# 🔄 Ensure latest Gemini SDK
def ensure_latest_gemini():
    try:
        print("[🔄] Checking for Gemini SDK updates...")
        subprocess.run([
            os.path.join(sys.prefix, "bin", "pip"),
            "install", "--upgrade", "google-generativeai", "--break-system-packages"
        ], check=True)
        import google.generativeai as genai
        print(f"[ℹ️] Gemini SDK version: {genai.__version__}")
    except Exception as e:
        print(f"[!] Failed to update Gemini SDK: {e}")

ensure_latest_gemini()

# 🔐 Secure API key store
KEY_FILE = os.path.expanduser("~/.gemini_api.enc")
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

# Load or validate API key
import google.generativeai as genai
def get_valid_gemini_client():
    for _ in range(2):
        api_key = load_encrypted_api_key()
        if not api_key:
            print("[🔐] Missing Gemini API Key. Get yours at https://makersuite.google.com/app/apikey")
            api_key = input("Paste Gemini API Key: ")
            save_encrypted_api_key(api_key)
        else:
            print("[🔑] Reusing encrypted Gemini API Key.")

        try:
            genai.configure(api_key=api_key)
            models = genai.list_models()
            return api_key, models
        except Exception as e:
            print(f"[!] Stored API key failed: {e}\n[↩️] Please enter a new one.")
            os.remove(KEY_FILE)

    print("[❌] Failed to authenticate after retry.")
    exit(1)

api_key, all_models = get_valid_gemini_client()

# 🔍 Choose a valid model
supported_models = [
    m.name for m in all_models
    if "generateContent" in m.supported_generation_methods
    and "vision" not in m.name
    and not m.name.endswith("deprecated")
]
print("[📋] Supported models:", supported_models)

model_name = os.getenv("GEMINI_MODEL")
if model_name not in supported_models:
    model_name = "models/gemini-1.5-flash" if "models/gemini-1.5-flash" in supported_models else supported_models[0]
    print(f"[⚙️] Using fallback model: {model_name}")

model = genai.GenerativeModel(model_name)

print("\n🤖 [Gemini Assistant] — Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ("exit", "quit"):
        break
    try:
        response = model.generate_content(user_input)
        print("Gemini:", response.text)
    except Exception as e:
        print(f"[!] Error: {e}")

__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    return "David Louis-Charles" in __author_id__
