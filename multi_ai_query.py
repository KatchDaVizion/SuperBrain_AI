# multi_ai_query.py – Secure, Tabulated, Memory-Logging Version with Venice Support
# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved

import os
import json
from datetime import datetime
from tabulate import tabulate

# === Fallback Logger ===
def log_info(msg, module="multi_ai_query"):
    print(f"[INFO][{module}] {msg}")

def log_error(msg, module="multi_ai_query"):
    print(f"[ERROR][{module}] {msg}")

def log_warning(msg, module="multi_ai_query"):
    print(f"[WARN][{module}] {msg}")

# === Memory ===
MEMORY_FILE = "memory/memory_db.json"

def save_entry(source, prompt, response):
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
    memory = []
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            memory = json.load(f)
    memory.append({
        "timestamp": datetime.utcnow().isoformat(),
        "source": source,
        "prompt": prompt,
        "response": response
    })
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

# === Encrypted Key Loader ===
import base64, getpass, hashlib
from cryptography.fernet import Fernet

SECRET = hashlib.sha256(getpass.getuser().encode()).digest()
FERNET_KEY = base64.urlsafe_b64encode(SECRET[:32])
fernet = Fernet(FERNET_KEY)

KEYS = {
    "OpenAI": "~/.openai_api.enc",
    "Claude": "~/.claude_api.enc",
    "Gemini": "~/.gemini_api.enc",
    "Groq": "~/.groq_api.enc",
    "Venice": "~/.venice_api.enc"
}

def load_encrypted_key(path):
    path = os.path.expanduser(path)
    if not os.path.exists(path):
        return None
    try:
        with open(path, "rb") as f:
            return fernet.decrypt(f.read()).decode()
    except:
        return None

# === AI Client Imports ===
from openai import OpenAI
from anthropic import Anthropic
import google.generativeai as genai
from groq import Groq
import requests

# === AI Response Functions ===
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

def get_venice_response(prompt, model="llama-3.3-70b"):
    key = load_encrypted_key(KEYS["Venice"])
    if not key:
        return "[Missing Venice Key]"
    try:
        headers = {
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        }
        r = requests.post("https://api.venice.ai/api/v1/chat/completions", headers=headers, json=payload)
        if r.status_code == 200:
            return r.json()["choices"][0]["message"]["content"].strip()
        else:
            return f"[Venice Error {r.status_code}]: {r.text}"
    except Exception as e:
        return f"[Venice Error: {e}]"

# === Main Query Execution ===
def query_all(prompt):
    print(f"\n[+] Querying all AI models for: '{prompt}'...\n")
    responses = {
        "OpenAI": get_openai_response(prompt),
        "Claude": get_claude_response(prompt),
        "Gemini": get_gemini_response(prompt),
        "Groq": get_groq_response(prompt),
        "Venice": get_venice_response(prompt)
    }

    for model, reply in responses.items():
        save_entry("multi_ai_query", f"{model} → {prompt}", reply)
        log_info(f"Saved {model} response to memory.")

    print(tabulate([[m, r] for m, r in responses.items()], headers=["Model", "Response"], tablefmt="fancy_grid"))

# === Entry Point ===
if __name__ == "__main__":
    print("\n🧠 [SuperBrain] Multi-AI Query")
    user_query = input("Prompt > ").strip()
    if user_query:
        query_all(user_query)
    else:
        print("[!] No input provided.")

# === Signature ===
__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    return "David Louis-Charles" in __author_id__
