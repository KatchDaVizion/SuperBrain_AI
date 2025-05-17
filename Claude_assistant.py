# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

# claude_assistant.py
import os
import json
import time
from datetime import datetime
from anthropic import Anthropic
from utils.memory_manager import save_entry
from utils.config import load_key
from utils.logger import log_info, log_error

MEMORY_FILE = "../memory/memory_db.json" # No longer directly used here
SOURCE = "Claude"
API_KEY_FILE = "claude_api_key.txt"
API_KEY_HINT = "Get yours at https://console.anthropic.com/account/keys"
CLAUDE_API_CHECK = {
    'url': "https://api.anthropic.com/v1/models",
    'method': 'get',
    'headers': {"X-API-Key": load_key(API_KEY_FILE, API_KEY_HINT)}, # Initial load for header
}

client = Anthropic(api_key=load_key(API_KEY_FILE, API_KEY_HINT, CLAUDE_API_CHECK))

def ask_claude(prompt):
    try:
        completion = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        log_info("Claude response received.", module="claude_assistant")
        return completion.content[0].text
    except Exception as e:
        log_error(f"Claude API error: {e}", module="claude_assistant")
        return f"[!] Error: {e}"

def chat():
    print(f"\n🧠 [Claude Assistant] — Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        answer = ask_claude(user_input)
        print("Assistant:", answer)
        save_entry(SOURCE, user_input, answer)

if __name__ == "__main__":
    log_info("Claude Assistant started.", module="claude_assistant")
    chat()


__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    allowed_user = "David Louis-Charles"
    return allowed_user in __author_id__
