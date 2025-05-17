# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

# groq_assistant.py
import os
import json
import time
from datetime import datetime
import requests
from utils.memory_manager import save_entry
from utils.config import load_key
from utils.logger import log_info, log_error

SOURCE = "Groq"
API_KEY_FILE = "groq_api_key.txt"
API_KEY_HINT = "Visit https://console.groq.com to get your API key."
GROQ_API_CHECK = {
    'url': "https://api.groq.com/openai/v1/models",
    'method': 'get',
    'headers': {"Authorization": f"Bearer {load_key(API_KEY_FILE, API_KEY_HINT)}"} # Initial load for header
}

def ask_groq(prompt):
    api_key = load_key(API_KEY_FILE, API_KEY_HINT, GROQ_API_CHECK)
    if not api_key:
        return "[⚠️] Groq API key not provided."
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "messages": [{"role": "user", "content": prompt}],
            "model": "mixtral-8x7b-32768",
            "temperature": 0.7
        }
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        response.raise_for_status()
        log_info("Groq response received.", module="groq_assistant")
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        log_error(f"Groq API error: {e}", module="groq_assistant")
        try:
            error_data = response.json()
            return f"[❌] Groq API error: {error_data.get('error', {}).get('message', str(e))}"
        except:
            return f"[❌] Groq API error: {e}"

def chat():
    print(f"\n🤖 [Groq Assistant] — Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        answer = ask_groq(user_input)
        if answer:
            print("Assistant:", answer)
            save_entry(SOURCE, user_input, answer)

if __name__ == "__main__":
    log_info("Groq Assistant started.", module="groq_assistant")
    chat()


__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    allowed_user = "David Louis-Charles"
    return allowed_user in __author_id__
