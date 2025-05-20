# multi_ai_query.py – Secure, Tabulated, Memory-Logging Version
# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved

import os
import json
from datetime import datetime
from tabulate import tabulate
from utils.logger import log_info, log_error, log_warning
from utils.memory_manager import save_entry

# === Encrypted Client Loaders ===
from openai import OpenAI
from anthropic import Anthropic
import google.generativeai as genai
from groq import Groq
import base64, getpass, hashlib
from cryptography.fernet import Fernet

# === Encrypted Key Files ===
KEYS = {
    "OpenAI": "~/.openai_api.enc",
    "Claude": "~/.claude_api.enc",
    "Gemini": "~/.gemini_api.enc",
    "Groq": "~/.groq_api.enc"
}

# === Key Decryption Logic ===
SECRET = hashlib.sha256(getpass.getuser().encode()).digest()
FERNET_KEY = base64.urlsafe_b64encode(SECRET[:32])
fernet = Fernet(FERNET_KEY)

def load_encrypted_key(path):
    path = os.path.expanduser(path)
    if not os.path.exists(path):
        return None
    try:
        with open(path, "rb") as f:
            return fernet.decrypt(f.read()).decode()
    except:
        return None

# === API Response Handlers ===
def get_openai_response(prompt):
    key = load_encrypted_key(KEYS["OpenAI"])
    if not key:
        return "[Missing OpenAI Key]"
    try:
        client = OpenAI(api_key=key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[OpenAI Error: {e}]"

def get_claude_response(prompt):
    key = load_encrypted_key(KEYS["Claude"])
    if not key:
        return "[Missing Claude Key]"
    try:
        client = Anthropic(api_key=key)
        response = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=500,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text.strip()
    except Exception as e:
        return f"[Claude Error: {e}]"

def get_gemini_response(prompt):
    key = load_encrypted_key(KEYS["Gemini"])
    if not key:
        return "[Missing Gemini Key]"
    try:
        genai.configure(api_key=key)
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"[Gemini Error: {e}]"

def get_groq_response(prompt):
    key = load_encrypted_key(KEYS["Groq"])
    if not key:
        return "[Missing Groq Key]"
    try:
        client = Groq(api_key=key)
        response = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[Groq Error: {e}]"

# === Main Query Logic ===
def query_all(prompt):
    print(f"\n[+] Querying multiple AI models for: '{prompt}'...\n")
    responses = {
        "OpenAI": get_openai_response(prompt),
        "Claude": get_claude_response(prompt),
        "Gemini": get_gemini_response(prompt),
        "Groq": get_groq_response(prompt)
    }

    # Save all to memory
    for model, reply in responses.items():
        save_entry("multi_ai_query", f"{model} → {prompt}", reply)
        log_info(f"Saved {model} response to memory.", module="multi_ai_query")

    # Display table
    print(tabulate([[m, r] for m, r in responses.items()], headers=["Model", "Response"], tablefmt="fancy_grid"))

# === Main Loop ===
if __name__ == "__main__":
    print("\n[🧠] Enter your multi-model query:")
    user_query = input("> ").strip()
    if user_query:
        query_all(user_query)
    else:
        print("[!] No input provided.")

__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    return "David Louis-Charles" in __author_id__
