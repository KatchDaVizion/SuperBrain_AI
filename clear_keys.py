import os

key_files = {
    "OpenAI": "~/.openai_api.enc",
    "Claude": "~/.claude_api.enc",
    "Gemini": "~/.gemini_api.enc",
    "Groq": "~/.groq_api.enc"
}

print("🔐 SuperBrain Key Cleaner\n--------------------------")
for name, path in key_files.items():
    full_path = os.path.expanduser(path)
    if os.path.exists(full_path):
        try:
            os.remove(full_path)
            print(f"[🧹] Deleted {name} key file at {full_path}")
        except Exception as e:
            print(f"[!] Failed to delete {name}: {e}")
    else:
        print(f"[✔️] No key found for {name}.")

print("\n✅ Done. All saved keys cleaned.")
