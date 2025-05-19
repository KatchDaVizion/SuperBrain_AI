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

  * TOR-enabled `.onion` + open web scraping (Pro version only)

* 📚 **Document Ingestion**

  * Feed PDF, TXT, or DOCX files into memory (Pro only)

* 🧑‍💻 **Facial Recognition Agent**

  * Offline image matching using your own data set (Pro only)

* 🔐 **Encrypted Memory Mode (Optional)**

  * AES encryption with passphrase-based key (Pro only)

* 🧹 **Plugin System**

  * Drop in Python tools to extend the AI with your own features

* 📍 **Portable & USB Bootable**

  * Deploy SuperBrain from a flash drive with zero cloud setup

* ↺ **Versioned, Self-Updating Architecture**

  * Built-in `version.txt`, `update_check.py`, and updater script

---

## 📂 LLM Model Download & RAM Requirements

SuperBrain lets you download and use **any Ollama-supported local LLM** directly on your machine.

Just type `/download <model_name>` inside the Local LLM assistant (e.g., `/download phi3`).

**Switch between models anytime** with `/model <number>`.

**RAM usage examples**:

| Model        | Approx RAM Needed |
| ------------ | ----------------- |
| TinyLLaMA    | 1.7 GB            |
| Phi-3        | 3 GB              |
| LLaMA2 7B    | 6–8 GB            |
| Mistral 7B   | 10–12 GB          |
| Mixtral 8x7B | 24+ GB            |

🚨 Large models need significant system memory. Check your available RAM before switching.

---

## 🔐 Secure Assistant Setup

Each SuperBrain assistant (OpenAI, Claude, Gemini, Groq) supports **encrypted API key storage**:

📅 No more retyping
🔐 Reuses your saved key
🔔 Detects invalid keys and prompts again
💪 Fully offline-safe

### How it works:

* First-time use: paste your API key.
* SuperBrain encrypts it using your Linux/macOS username and saves to `~/.api.enc`.
* If a key fails, you’ll be prompted to re-enter it.
* Wipe all saved keys with:

python3 clear_keys.py

🔐 Your keys are never shared, stored in plain text, or uploaded. All data stays encrypted and local.

---

## 💻 Installation

### 🐈 On Linux / WSL / Kali / Ubuntu:

chmod +x launch_ai_portable.sh
./launch_ai_portable.sh

### 🍏 On macOS:

chmod +x launch_macOS.sh
./launch_macOS.sh

---

## 🧠 How the AI Learns Over Time

Each answer from GPT-4, Claude, Gemini, Groq, and local models is:

* Timestamped
* Logged to memory
* Reused in future queries through semantic search (RAG)
* Optionally encrypted

> The more you use SuperBrain, the smarter it becomes.

---

## 🛡️ Ethics Statement

SuperBrain gives you powerful, unrestricted tools — **you are responsible for how you use them.**

This project:

* Promotes ethical research, investigation, and innovation
* Prohibits disinformation, illegal activity, and unethical use
* Defends privacy and intelligence independence

---

## 👮 Authorship & License

**SuperBrain AI Platform**
Created by **David Louis-Charles** ([KatchDaVizion](https://github.com/KatchDaVizion))
️© 2025 — MIT License

Embedded authorship signature:

__author_id__ = "KatchDaVizion_2025_DLC_SIG"
def check_license():
    return "David Louis-Charles" in __author_id__

Includes MIT-licensed models from [ageitgey/face\_recognition\_models](https://github.com/ageitgey/face_recognition_models).

---

## 📦 Distribution

* GitHub Repo: [github.com/KatchDaVizion/SuperBrain\_AI](https://github.com/KatchDaVizion/SuperBrain_AI)
* Gumroad Pro Version (coming soon)
* USB Boot Image (available upon request)

---

## 🙌 Community & Support

* 🛠 Issues welcome
* 🤝 Contributions encouraged
* 💬 Feedback + collaboration invited

Built for privacy-first intelligence by **David Louis-Charles**
[https://github.com/KatchDaVizion](https://github.com/KatchDaVizion)

\#OpenSource #LocalAI #UncensoredLLM #CyberSecurity #OSINT #AI #PrivacyTech
