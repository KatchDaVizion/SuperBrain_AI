# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

# multi_ai_query.py
import os
import json
import time
from datetime import datetime
from utils.config import load_key
from utils.logger import log_info, log_error
from openai import OpenAI
from anthropic import Anthropic
import requests

SOURCE = "Multi-Model"
OPENAI_KEY_FILE = "openai_api_key.txt"
OPENAI_KEY_HINT = "Get yours at https://platform.openai.com/api-keys"
CLAUDE_KEY_FILE = "claude_api_key.txt"
CLAUDE_KEY_HINT = "Get yours at https://console.anthropic.com/account/keys"
GEMINI_KEY_FILE = "gemini_api_key.txt"
GEMINI_KEY_HINT = "Get yours from https://makersuite.google.com/app/apikey"
GROQ_KEY_FILE = "groq_api_key.txt"
GROQ_KEY_HINT = "Visit https://console.groq.com to get your API key."

openai_client = None
claude_client = None

def get_openai_response(prompt):
    global openai_client
    api_key = load_key(OPENAI_KEY_FILE, OPENAI_KEY_HINT, {'url': "https://api.openai.com/v1/engines", 'method': 'get', 'headers': {"Authorization": f"Bearer {load_key(OPENAI_KEY_FILE, OPENAI_KEY_HINT)}"}} if openai_client is None else None)
    if not api_key and openai_client is None:
        log_warning("OpenAI API key not available.", module="multi_ai_query")
        return None
    if openai_client is None and api_key:
        openai_client = OpenAI(api_key=api_key)
    if openai_client:
        try:
            completion = openai_client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}], max_tokens=500)
            log_info("OpenAI response received.", module="multi_ai_query")
            return completion.choices[0].message.content
        except Exception as e:
            log_error(f"OpenAI API error: {e}", module="multi_ai_query")
            return f"[OpenAI Error: {e}]"
    return "[OpenAI Not Available]"

def get_claude_response(prompt):
    global claude_client
    api_key = load_key(CLAUDE_KEY_FILE, CLAUDE_KEY_HINT, {'url': "https://api.anthropic.com/v1/models", 'method': 'get', 'headers': {"X-API-Key": load_key(CLAUDE_KEY_FILE, CLAUDE_KEY_HINT)}} if claude_client is None else None)
    if not api_key and claude_client is None:
        log_warning("Claude API key not available.", module="multi_ai_query")
        return None
    if claude_client is None and api_key:
        claude_client = Anthropic(api_key=api_key)
    if claude_client:
        try:
            completion = claude_client.messages.create(model="claude-3-opus-20240229", max_tokens=500, messages=[{"role": "user", "content": prompt}])
            log_info("Claude response received.", module="multi_ai_query")
            return completion.content[0].text
        except Exception as e:
            log_error(f"Claude API error: {e}", module="multi_ai_query")
            return f"[Claude Error: {e}]"
    return "[Claude Not Available]"

def get_gemini_response(prompt):
    api_key = load_key(GEMINI_KEY_FILE, GEMINI_KEY_HINT, {'url': "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro", 'method': 'get', 'params': {"key": load_key(GEMINI_KEY_FILE, GEMINI_KEY_HINT)}})
    if not api_key:
        log_warning("Gemini API key not available.", module="multi_ai_query")
        return "[Gemini Not Available]"
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
        headers = {"Content-Type": "application/json"}
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        log_info("Gemini response received.", module="multi_ai_query")
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except requests.exceptions.RequestException as e:
        log_error(f"Gemini API error: {e}", module="multi_ai_query")
        try:
            error_data = response.json()
            return f"[Gemini Error: {error_data.get('error', {}).get('message', str(e))}]"
        except:
            return f"[Gemini Error: {e}]"

def get_groq_response(prompt):
    api_key = load_key(GROQ_KEY_FILE, GROQ_KEY_HINT, {'url': "https://api.groq.com/openai/v1/models", 'method': 'get', 'headers': {"Authorization": f"Bearer {load_key(GROQ_KEY_FILE, GROQ_KEY_HINT)}}"})
    if not api_key:
        log_warning("Groq API key not available.", module="multi_ai_query")
        return "[Groq Not Available]"
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        payload = {"messages": [{"role": "user", "content": prompt}], "model": "mixtral-8x7b-32768", "temperature": 0.7}
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        response.raise_for_status()
        log_info("Groq response received.", module="multi_ai_query")
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        log_error(f"Groq API error: {e}", module="multi_ai_query")
        try:
            error_data = response.json()
            return f"[Groq Error: {error_data.get('error', {}).get('message', str(e))}]"
        except:
            return f"[Groq Error: {e}]"

def query_all(prompt):
    print(f"\n[+] Querying multiple AI models for: '{prompt}'...\n")
    responses = {
        "OpenAI": get_openai_response(prompt),
        "Claude": get_claude_response(prompt),
        "Gemini": get_gemini_response(prompt),
        "Groq": get_groq_response(prompt),
    }
    for model,


__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    allowed_user = "David Louis-Charles"
    return allowed_user in __author_id__
