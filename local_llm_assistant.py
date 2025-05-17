# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

# local_llm_assistant.py
import sys
print(f"Interpréteur Python utilisé : {sys.executable}")
import os
import json
import time
import subprocess
from sentence_transformers import SentenceTransformer, util
import torch
from langchain_community.llms import Ollama
from utils.logger import log_info, log_error, log_warning
from utils.memory_manager import load_memory, save_memory, save_local_llm_entry
import sys
from datetime import datetime

DEFAULT_MODEL = "tinyllama"
model_name = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_MODEL
llm = Ollama(model=model_name) # Use the correct class name

# Load memory and embeddings
memory_entries = load_memory()
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
texts = [entry["content"] for entry in memory_entries if "content" in entry]
embeddings = embedding_model.encode(texts, convert_to_tensor=True) if texts else torch.empty(0)

FEEDBACK_LOG_FILE = "../logs/feedback.log"

def record_feedback(user_query, model, response, feedback):
    os.makedirs(os.path.dirname(FEEDBACK_LOG_FILE), exist_ok=True)
    timestamp = datetime.utcnow().isoformat()
    with open(FEEDBACK_LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] Model: {model}, Question: {user_query}\nResponse: {response}\nFeedback: {feedback}\n\n")
    log_info(f"Feedback recorded: {feedback}", module="local_llm")

def retrieve_relevant_memories(query, top_k=5, similarity_threshold=None):
    if not embeddings.numel():
        return []
    query_embedding = embedding_model.encode(query, convert_to_tensor=True)
    similarities = util.pytorch_cos_sim(query_embedding, embeddings)[0]
    sorted_indices = torch.argsort(similarities, descending=True)[:top_k]
    relevant_memories = [texts[i] for i in sorted_indices if similarity_threshold is None or similarities[i] >= similarity_threshold]
    return relevant_memories

def build_context_with_memory(user_query, use_memory=True, similarity_threshold=None):
    if use_memory:
        relevant = retrieve_relevant_memories(user_query, similarity_threshold=similarity_threshold)
        memory_snippets = "\n".join(f"- {r}" for r in relevant)
        return f"The assistant has the following prior context:\n{memory_snippets}\n\nNow answer:\n{user_query}" if memory_snippets else user_query
    else:
        return user_query

def load_new_model(new_model_name):
    global llm
    global model_name
    try:
        llm = Ollama(model=model_name) # Use the correct class name
        model_name = new_model_name
        log_info(f"Model switched to: {model_name}", module="local_llm")
        return True
    except Exception as e:
        log_error(f"Error loading model '{new_model_name}': {e}", module="local_llm")
        return False

def list_ollama_models_numbered():
    try:
        result = subprocess.run(['ollama', 'list'], capture_output=True, text=True, check=True)
        models = result.stdout.strip().split('\n')[1:]  # Skip the header
        if models:
            print("\n[+] Available Ollama models:")
            numbered_models = {}
            for i, model_info in enumerate(models):
                parts = model_info.split()
                if parts:
                    print(f"{i+1}. {parts[0]}")
                    numbered_models[str(i+1)] = parts[0]
            return numbered_models
        else:
            print("[!] No Ollama models found.")
            return {}
    except FileNotFoundError:
        log_error("Ollama command not found.", module="local_llm")
        return {}
    except subprocess.CalledProcessError as e:
        log_error(f"Error listing Ollama models: {e}", module="local_llm")
        return {}

def check_for_model_update(model_name):
    try:
        result = subprocess.run(['ollama', 'pull', '--dry-run', model_name], capture_output=True, text=True, check=False)
        if "already up-to-date" not in result.stdout:
            log_warning(f"Update found for Ollama model '{model_name}'.", module="local_llm")
            return True
        else:
            log_info(f"Ollama model '{model_name}' is up-to-date.", module="local_llm")
            return False
    except FileNotFoundError:
        log_error("Ollama command not found.", module="local_llm")
        return False
    except subprocess.CalledProcessError as e:
        log_error(f"Error checking for model update: {e}", module="local_llm")
        return False

def update_model(model_name):
    try:
        log_info(f"Pulling latest version of Ollama model '{model_name}'.", module="local_llm")
        result = subprocess.run(['ollama', 'pull', model_name], check=True)
        log_info(f"Ollama model '{model_name}' updated successfully.", module="local_llm")
        global llm
        llm = Ollama(model=model_name) # Use the correct class name
        return True
    except FileNotFoundError:
        log_error("Ollama command not found.", module="local_llm")
        return False
    except subprocess.CalledProcessError as e:
        log_error(f"Error updating model '{model_name}': {e}", module="local_llm")
        return False

def download_new_model(model_name_to_download):
    try:
        log_info(f"Downloading Ollama model '{model_name_to_download}'.", module="local_llm")
        result = subprocess.run(['ollama', 'pull', model_name_to_download], check=True, capture_output=True, text=True)
        log_info(f"Ollama model '{model_name_to_download}' downloaded successfully.", module="local_llm")
        print(f"[+] Model '{model_name_to_download}' downloaded. Use '/model' to switch.")
        return True
    except FileNotFoundError:
        log_error("Ollama command not found.", module="local_llm")
        print("[!] Error: Ollama command not found.")
        return False
    except subprocess.CalledProcessError as e:
        log_error(f"Error downloading model '{model_name_to_download}': {e.stderr}", module="local_llm")
        print(f"[!] Error downloading model '{model_name_to_download}': {e.stderr}")
        return False

# Check for update on startup
if check_for_model_update(model_name):
    if input(f"Do you want to update the Ollama model '{model_name}' now? (y/N): ").lower() == 'y':
        update_model(model_name)

# Main loop
while True:
    print(f"\n🧠 Current model: {model_name}")
    print("Options: ")
    print("  - Type your question to chat.")
    print("  - '/model <number>' to switch model.")
    print("  - '/list' to see available models.")
    print("  - '/update' to check for and update the current model.")
    print("  - '/download <model_name>' to download a new Ollama model (e.g., '/download llama3').")
    print("  - '/exit' or '/quit' to exit.")
    user_input = input(">> ")

    if user_input.strip().lower() in ("/exit", "/quit"):
        break
    elif user_input.startswith("/model "):
        model_number_str = user_input.split("/model ")[1].strip()
        if model_number_str:
            available_models = list_ollama_models_numbered()
            if available_models and model_number_str in available_models:
                new_model = available_models[model_number_str]
                load_new_model(new_model)
            else:
                print("[!] Invalid model number. Use '/list' to see available models.")
        else:
            print("[!] Please specify a model number (e.g., /model 1).")
        continue
    elif user_input.lower() == "/list":
        list_ollama_models_numbered()
        continue
    elif user_input.lower() == "/update":
        if check_for_model_update(model_name):
            update_model(model_name)
        else:
            print(f"[-] Ollama model '{model_name}' is already up-to-date.")
        continue
    elif user_input.startswith("/download "):
        model_to_download = user_input.split("/download ")[1].strip()
        if model_to_download:
            download_new_model(model_to_download)
        else:
            print("[!] Please specify the model name to download (e.g., /download llama3).")
        continue

    use_memory_input = input("Use memory? (y/N): ").lower()
    use_memory = use_memory_input == 'y'

    similarity_threshold = None
    if use_memory:
        threshold_input = input("Enter similarity threshold (optional, e.g., 0.7): ").strip()
        if threshold_input:
            try:
                similarity_threshold = float(threshold_input)
            except ValueError:
                print("[!] Invalid threshold. Using default.")

    prompt = build_context_with_memory(user_input, use_memory, similarity_threshold)
    try:
        response = llm(prompt)
        print(f"\n🤖 {response}\n")
        save_local_llm_entry(model_name, user_input + "\n" + response)
        memory_entries = load_memory() # Reload memory to update embeddings
        texts = [entry["content"] for entry in memory_entries if "content" in entry]
        embeddings = embedding_model.encode(texts, convert_to_tensor=True) if texts else torch.empty(0)

        # Get user feedback
        feedback = input("Was this response helpful? (y/n): ").lower()
        if feedback in ['y', 'n']:
            record_feedback(user_input, model_name, response, "Positive" if feedback == 'y' else "Negative")
        else:
            print("[!] Invalid feedback.")

    except Exception as e:
        log_error(f"Error during Ollama interaction: {e}", module="local_llm")
        print(f"[!] Error: {e}")


__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    allowed_user = "David Louis-Charles"
    return allowed_user in __author_id__
