# 🧠 SuperBrain AI – Offline AI Research Platform (V1)

> Modular, encrypted, and assistant-powered intelligence OS – built for OSINT, cybersecurity, and privacy-first research.

---

## 🚀 What Is It?

**SuperBrain AI** is your plug-and-play, offline-capable AI assistant ecosystem.  
It runs fully on your machine, supports multiple local and API-based LLMs, and helps you search, analyze, and remember — without exposing your data to the cloud.

---

## ✅ Features

- 🔌 **Multi-AI Assistant Hub**  
  GPT-4, Claude, Gemini, Groq, TinyLLaMA, LLaMA2, Mistral (via Ollama)

- 🧠 **Memory System + RAG**  
  All prompts and answers saved, with semantic recall and feedback

- 🕵️ **Dark Web & Surface Web Scraper**  
  Scrapes `.onion` and surface URLs via TOR and DuckDuckGo

- 📚 **Document & PDF Ingestion**  
  Feed reports, text files, or notes directly into the AI’s memory

- 🧑‍💻 **Face Recognition Agent**  
  Compare webcam input to known image sets – all offline
This project uses pretrained models from [face_recognition_models](https://github.com/ageitgey/face_recognition_models) by Adam Geitgey, licensed under MIT.

- 🔐 **Encrypted Memory Mode** (Optional)  
  Choose to store memory encrypted with a passphrase

- 📦 **Modular Plugins Folder**  
  Drop in your own Python AI tools

- 💽 **USB Portable Deployment**  
  Launch from any Linux machine – great for OPSEC or travel

- 🔄 **Versioned & Self-Updating**  
  `version.txt`, auto-updater, and Git integration

---

## 💻 Installation

### 🐧 On Linux / WSL / Kali / Ubuntu:

chmod +x launch_ai_portable.sh
./launch_ai_portable.sh

🍏 On macOS:

chmod +x launch_macOS.sh
./launch_macOS.sh
The launcher will:

Create a virtual environment

Install dependencies

Start Ollama and Tor

Prompt you to pick your assistant

🛡 Memory Encryption (Optional)
On first run, choose:

pgsql
1. Enable memory encryption
2. Leave memory unencrypted
If enabled, memory is encrypted using AES and a passphrase-based key.

View later with:

python3 utils/decrypt_memory.py
🧠 Assistant Menu (from launcher)
Option	Assistant	Function
1	OpenAI Assistant	GPT-4 (API)
2	Claude Assistant	Claude 3 (API)
3	Gemini Assistant	Gemini Pro (API)
4	Groq Assistant	Groq Mixtral (API)
5a	TinyLLaMA (local)	Ollama model
5b	LLaMA2 (local)	Ollama model
5c	Mistral (local)	Ollama model
6	Multi-AI Battle Mode	Ask all at once
7	Face Recognition Agent	Offline image matching
8	Dark Web Scraper	Surface + .onion
9	Ingest Document / Text	Feed AI memory manually
10	Quit	Exit safely

🔄 Update

python3 update_check.py
./update_superbrain.sh
🧬 Authors & License

SuperBrain AI Platform  
Created by David Louis-Charles (GitHub: KatchDaVizion)  
© 2025 All Rights Reserved – MIT Licensed
Embedded authorship signature:

__author_id__ = "KatchDaVizion_2025_DLC_SIG"
def check_license():
    return "David Louis-Charles" in __author_id__
📦 Distribution
GitHub Repo

Gumroad (coming soon)

USB boot image available upon request

🙌 Support
🛠 Issues welcome • 🤝 Contributions invited
🔐 Designed for security researchers, OSINT analysts, and AI hackers
💡 Questions? Hit me up at https://github.com/KatchDaVizion

Built for privacy-first intelligence by David Louis-Charles
