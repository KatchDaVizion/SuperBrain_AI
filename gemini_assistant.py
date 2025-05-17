# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

# gemini_assistant.py
import os
import json
import time
from datetime import datetime
from utils.memory_manager import save_entry
from utils.config import load_key, save_key
from utils.logger import log_info, log_error
import requests

SOURCE = "Gemini"
API_KEY_FILE = "gemini_api_key.txt"
API_KEY_HINT = "Get yours from https://makersuite.google.com/app/apikey"
GEMINI_API_CHECK = {
    'url': "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro",
    'method': 'get',
    'params': {"key": load_key(API_KEY_FILE, API_KEY_HINT)} # Key as a parameter
}

def ask_gemini(prompt):
    try:
        api_key = load_key(API_KEY_FILE, API_KEY_HINT, GEMINI_API_CHECK)
        if not api_key:
            return "[⚠️] Gemini API key not provided."
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
        headers = {"Content-Type": "application/json"}
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        log_info("Gemini response received.", module="gemini_assistant")
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except requests.exceptions.RequestException as e:
        log_error(f"Gemini API error: {e}", module="gemini_assistant")
        try:
            error_data = response.json()
            return f"[❌] Gemini API error: {error_data.get('error', {}).get('message', str(e))}"
        except:
            return f"[❌] Gemini API error: {e}"

def chat():
    print(f"\n🤖 [Gemini Assistant] — Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        answer = ask_gemini(user_input)
        if answer:
            print("Assistant:", answer)
            save_entry(SOURCE, user_input, answer)

if __name__ == "__main__":
    log_info("Gemini Assistant started.", module="gemini_assistant")
    chat()


__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    allowed_user = "David Louis-Charles"
    return allowed_user in __author_id__
