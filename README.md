# 🧠 SuperBrain AI – Offline, Ethical, Research-Driven AI Platform (V1)

> A local-first AI platform combining popular cloud models with uncensored local LLMs for empowered, responsible research.

---

## 🚀 What Is SuperBrain AI?

**SuperBrain AI** is a privacy-first, modular AI ecosystem designed to run fully **offline on your local machine**.
It integrates powerful local LLMs (via **Ollama**) and connects to leading APIs like GPT-4, Claude, Gemini, and Groq — enabling you to:

* ✅ Conduct advanced, unrestricted research
* ✅ Maintain full control of your data
* ✅ Grow your AI’s knowledge over time

SuperBrain is designed as a **personal intelligence platform**, empowering ethical researchers, analysts, and developers to explore freely while protecting privacy and respecting responsible use.

---

## 🔍 Why Local & Uncensored?

Most online AI tools are censored, rate-limited, and surveilled.

With SuperBrain:

* You run uncensored local models like **TinyLLaMA**, **LLaMA2-Uncensored**, and **Mistral**, enabling deep research, sensitive exploration, or intelligence work that cloud filters often block.
* Everything runs locally — you **own your tools and your data**.

🛡️ SuperBrain is built for ethical use only. Misuse, abuse, or unethical application goes against the spirit of this platform.

---

## ✅ Core Features

* 🔌 **Multi-AI Assistant Hub**

  * GPT-4, Claude, Gemini, Groq (API)
  * TinyLLaMA, LLaMA2, Mistral, Phi (local via Ollama)

* 🧠 **Memory System + RAG Recall**

  * All answers (from cloud or local) are saved and indexed
  * Your local AI **learns over time** by recalling past answers

* 🕵️ **Dark Web & Surface Web Scraper**

  * TOR-enabled `.onion` + open web scraping

* 📚 **Document Ingestion**

  * Feed PDF, TXT, or DOCX files into memory

* 🧑‍💻 **Facial Recognition Agent**

  * Offline image matching using your own data set

* 🔐 **Encrypted Memory Mode (Optional)**

  * AES encryption with passphrase-based key

* 🧹 **Plugin System**

  * Drop in Python tools to extend the AI with your own features

* 📍 **Portable & USB Bootable**

  * Deploy SuperBrain from a flash drive with zero cloud setup

* ↺ **Versioned, Self-Updating Architecture**

  * Built-in `version.txt`, `update_check.py`, and updater script

---

## 🔐 Secure Assistant Setup

Each SuperBrain assistant (OpenAI, Claude, Gemini, Groq) supports **encrypted API key storage**:

✅ No more retyping  
✅ Reuses your saved key  
✅ Detects invalid keys and prompts again  
✅ Fully offline-safe

### How it works:

- The first time you launch an assistant, you paste your API key.
- It’s encrypted using your Linux/macOS username and stored in your home folder (e.g. `~/.openai_api.enc`).
- If the key is ever invalid (expired or revoked), SuperBrain prompts you for a new one.
- You can **manually clear all stored keys** using:

python3 clear_keys.py

🔐 Your keys are never shared, stored in plain text, or uploaded anywhere.
Everything stays 100% local, protected with cryptography.Fernet.
---

## 💻 Installation

### 🐧 On Linux / WSL / Kali / Ubuntu:

chmod +x launch_ai_portable.sh
./launch_ai_portable.sh

### 🍏 On macOS:

chmod +x launch_macOS.sh
./launch_macOS.sh

---

## 🧠 How the AI Learns Over Time

Every answer from GPT-4, Claude, Gemini, Groq, and your local models is:

* Logged to memory with timestamp + source
* Used in **semantic search (RAG)** to answer future prompts
* Encrypted (if enabled) to protect your research

This means:

> The more you use SuperBrain, the **smarter and more personalized** your local AI becomes.

---

## 🛡 Ethics Statement

SuperBrain gives you powerful, unrestricted tools — and **you are responsible for how you use them**.

This project:

* Encourages **truth-seeking, research, and innovation**
* Does **not support disinformation, illegal, or unethical use**
* Empowers responsible users to build, investigate, and understand

---

## 🦮 Authorship & License

**SuperBrain AI Platform**
Created by **David Louis-Charles** (GitHub: [KatchDaVizion](https://github.com/KatchDaVizion))
© 2025 – All Rights Reserved – MIT Licensed

Embedded authorship signature:

__author_id__ = "KatchDaVizion_2025_DLC_SIG"
def check_license():
    return "David Louis-Charles" in __author_id__

Uses pretrained models from [face\_recognition\_models](https://github.com/ageitgey/face_recognition_models) by Adam Geitgey (MIT License).

---

## 📦 Distribution

* GitHub Repo: [github.com/KatchDaVizion/SuperBrain\_AI](https://github.com/KatchDaVizion/SuperBrain_AI)
* Gumroad Pro Version (coming soon)
* USB Boot Image (available upon request)

---

## 🙌 Community & Support

🛠 Issues welcome • 🤝 Contributions invited
💬 Feedback? Feature ideas? Bug reports? Let’s connect.

Built for privacy-first intelligence by **David Louis-Charles**
**[https://github.com/KatchDaVizion](https://github.com/KatchDaVizion)**
\#OpenSource #LocalAI #CyberSecurity #OSINT #AI #UncensoredLLM #PrivacyTech
