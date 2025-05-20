# 🧠 SuperBrain AI – Offline, Ethical, Research-Driven AI Platform (V1.1)

> A modular AI research platform combining cloud intelligence with offline uncensored LLMs — encrypted, portable, and built for privacy-first users.

---

## 🚀 What Is SuperBrain AI?

**SuperBrain AI** is a **local-first**, privacy-respecting AI platform built for advanced research, investigation, and offline intelligence. You can run:

* ✅ API-powered agents like GPT-4, Claude, Gemini, and Groq
* ✅ Local LLMs like TinyLLaMA, LLaMA2, Mistral, Phi via **Ollama**
* ✅ Dark web scrapers, document ingestion, face recognition, and more

All while **logging results**, **storing memory**, and **growing your assistant’s knowledge over time**.

---

## 🔐 Multi-AI Query Assistant 

* 🔑 **Encrypted API Key Storage**
  * No more plaintext `.txt` files
  * Reuses keys from encrypted `~/.openai_api.enc`, etc.
  * Same system used in all single assistants

* 💾 **Automatic Memory Logging**
  * Every answer is saved with timestamp and source
  * Recalled by your local LLM for future answers

* 📊 **Tabular Answer View**
  * Get GPT-4, Claude, Gemini, and Groq answers **side-by-side**
  * Powered by the `tabulate` library for clean comparison

To launch:
python3 multi_ai_query.py

✅ Core Features
🧠 RAG Memory System – Learn over time

🔌 Multi-AI Query Hub – GPT-4, Claude, Gemini, Groq

💬 Local LLM Chat Interface – Ollama-powered

🕵️ Dark Web + Surface Scraper – .onion ready (Pro)

📚 PDF/TXT Ingestion to Memory – Feed your assistant (Pro)

🔐 Memory Encryption – Passphrase-based AES (Pro)

🧑‍  Facial Recognition Agent – Offline image matching (Pro)

🧹 Plugin Loader – Drop Python tools into /plugins

📀 USB Portable Launcher – Boot anywhere, work offline

↻ Self-Updating Scripts – Built-in version checks and updater

🧠 How the AI Learns Over Time
Each query from GPT-4, Claude, Gemini, Groq, and local LLMs is:

Timestamped

Stored in memory_db.json

Retrieved and used for context with semantic similarity

Optionally encrypted with passphrase protection

Your AI grows smarter with each interaction.

📦 Installation
🐧 Linux / WSL / Kali / Ubuntu:

chmod +x launch_ai_portable.sh

./launch_ai_portable.sh

🍏 macOS:

chmod +x launch_macOS.sh

./launch_macOS.sh

📂 LLM Download & RAM Estimates
SuperBrain supports all local LLMs available through Ollama. You can download and switch between models directly inside the assistant interface.

Model Name	Minimum RAM Required
tinyllama	1.7 GB
phi-3	3 GB
llama2 (7B)	6–8 GB
mistral	10–12 GB
mixtral (8x7B)	24+ GB

🧠 To download a new model:

Use '/download <model name>' to download any model on ollama : https://ollama.com/
🔁 To switch to a downloaded model:

'/model <number>' in the local assistant to run the model needed
⚠️ Note: Make sure your system has enough free RAM before switching to larger models. SuperBrain dynamically adjusts based on your available resources.


🔐 Encrypted API Key Storage
No plaintext keys. All assistants (and the multi-model assistant) now use:

Encrypted keys stored in your home dir (e.g., ~/.openai_api.enc)

Automatically reused on next run

Keys tied to your username for extra security

To reset all stored keys:

python3 clear_keys.py

🛡️ Ethics Statement
SuperBrain provides uncensored tools — it is your responsibility to use them ethically.

This project:

Supports intelligence, education, privacy, and cybersecurity

Rejects disinformation, illegal activity, abuse, and harm

Is licensed under MIT with fair-use principles

👮 Author & License
SuperBrain AI Platform
Created by David Louis-Charles
GitHub: github.com/KatchDaVizion
© 2025 – MIT License

Embedded signature:

__author_id__ = "KatchDaVizion_2025_DLC_SIG"
def check_license():
    return "David Louis-Charles" in __author_id__

🙌 Community & Distribution
📦 GitHub Repo: github.com/KatchDaVizion/SuperBrain_AI

🛍️ Gumroad Pro Version (coming soon)

💽 Bootable USB Version (upon request)

🛠 Feature suggestions, issues, and contributions welcome

🌐 Tags
#OfflineAI #UncensoredLLM #CyberSecurity #OSINT #PrivacyTech #LocalLLM #DarkWeb #ResearchAssistant #SuperBrainAI

