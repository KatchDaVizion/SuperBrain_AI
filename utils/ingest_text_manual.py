# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

# ingest_text_manual.py
import os
import json
import time
from datetime import datetime
from utils.memory_manager import save_entry
from utils.logger import log_info, log_error

SOURCE = "manual_input"

def ingest_manual_text():
    print("\n📝 [Manual Text Ingestion]")
    text_to_ingest = input("Enter the text you want to ingest into memory: ")
    if text_to_ingest:
        save_entry(SOURCE, "manual_feed", text_to_ingest)
        log_info("Manually ingested text.", module="ingest_text_manual")
        print("[+] Text ingested successfully.")
    else:
        print("[!] No text entered.")

def ingest_from_file():
    print("\n📄 [Ingest from File]")
    file_path = input("Enter the path to the file you want to ingest: ")
    try:
        with open(file_path, "r") as f:
            file_content = f.read()
            save_entry(f"file:{os.path.basename(file_path)}", "manual_feed", file_content)
            log_info(f"Ingested content from {file_path}.", module="ingest_text_manual")
            print(f"[+] Content from '{os.path.basename(file_path)}' ingested successfully.")
    except FileNotFoundError:
        log_error(f"File not found: {file_path}", module="ingest_text_manual")
        print(f"[!] Error: File not found at '{file_path}'.")
    except Exception as e:
        log_error(f"Error reading file '{file_path}': {e}", module="ingest_text_manual")
        print(f"[!] Error reading file: {e}")

if __name__ == "__main__":
    log_info("Manual Ingestion script started.", module="ingest_text_manual")
    while True:
        print("\nChoose ingestion method:")
        print("1. Enter text manually")
        print("2. Ingest from file")
        print("3. Back to main menu")
        choice = input("Enter your choice [1-3]: ")
        if choice == '1':
            ingest_manual_text()
        elif choice == '2':
            ingest_from_file()
        elif choice == '3':
            break
        else:
            print("[!] Invalid choice.")


__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    allowed_user = "David Louis-Charles"
    return allowed_user in __author_id__
