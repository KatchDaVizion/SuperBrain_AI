# 🧠 SuperBrain AI – Offline, Ethical, Research-Driven AI Platform (V1.1)

> A modular AI research platform combining popular cloud models with offline uncensored LLMs — encrypted, portable, and built for privacy-first users.

---

## 🚀 What Is SuperBrain AI?

**SuperBrain AI** is a **local-first**, privacy-respecting AI platform built for advanced research, investigation, and offline intelligence. You can run:

✅ API-powered agents like GPT-4, Claude, Gemini, and Groq
✅ Local LLMs like TinyLLaMA, LLaMA2, Mistral, Phi via **Ollama**
✅ Dark web scrapers, document ingestion, face recognition, and more (Pro only)

Everything runs fully offline — and every answer is logged, learned, and improved over time through an encrypted memory system.

---

## 🔍 Why Use Uncensored Local Models?

Online AI tools are often:

* Filtered or politically limited
* Rate-limited or API-bound
* Logged and monitored by third parties

With SuperBrain, you:

* Own your data and tools
* Can run **uncensored models** like TinyLLaMA or Mistral for raw knowledge access
* Perform deeper research without censorship
* Are free to build intelligence with full autonomy

SuperBrain is designed for **ethical research** only. Misuse contradicts its mission.

---

## 🔐 Multi-AI Query Assistant (Research Mode)

SuperBrain includes a unique **multi-model querying script**:

```bash
python3 multi_ai_query.py
```

🧠 Ask one question → Get responses from **GPT-4, Claude, Gemini, and Groq** side-by-side.

### Benefits:

* 🔍 Instantly compare model reasoning styles
* 🧠 Save all results to memory (RAG-enhanced)
* 🔒 API keys are encrypted and reused automatically
* 📊 Tabulated output powered by `tabulate`

This supercharges your insight-building and allows **open research consensus discovery**.

---

## ✅ Core Features

* 🔌 **Multi-AI Hub** – GPT-4, Claude, Gemini, Groq (API) + Local LLMs (Ollama)
* 🧠 **Memory System + RAG Recall** – Past answers stored and reused semantically
* 🕵️ **Dark Web Scraper** – Tor-powered `.onion` access *(Pro)*
* 📚 **PDF/Document Ingestion** – Feed reports or notes into memory *(Pro)*
* 🧑‍💻 **Facial Recognition Agent** – Match images offline *(Pro)*
* 🔐 **Encrypted Memory Mode** – AES passphrase protection *(Pro)*
* 🧹 **Plugin Loader** – Drop in your own Python tools
* 📀 **USB Portable Launcher** – Run from a flash drive or SSD
* ↻ **Versioned, Auto-Updating Architecture**

---

## 📂 LLM Model Downloads & RAM Estimates

You can download any model from [ollama.com](https://ollama.com) directly inside SuperBrain:

```bash
/download phi3
/model 2  # switch model
```

| Model Name   | Minimum RAM Required |
| ------------ | -------------------- |
| TinyLLaMA    | 1.7 GB               |
| Phi-3        | 3 GB                 |
| LLaMA2 7B    | 6–8 GB               |
| Mistral      | 10–12 GB             |
| Mixtral 8x7B | 24+ GB               |

⚠️ **Always check available memory before switching models.** SuperBrain dynamically adjusts based on system RAM.

---

## 🔐 Secure Assistant Setup

All assistants (OpenAI, Claude, Gemini, Groq) use encrypted API key storage:

* 🔐 Keys saved to `~/.openai_api.enc`, etc.
* 🔁 Reused securely without plaintext
* 🧹 Delete all keys with: `python3 clear_keys.py`

---

## 💻 Installation

### 🐧 Linux / WSL / Kali / Ubuntu:

```bash
chmod +x launch_ai_portable.sh
./launch_ai_portable.sh
```

### 🍏 macOS:

```bash
chmod +x launch_macOS.sh
./launch_macOS.sh
```

---

## 🧠 How the AI Learns Over Time

Every assistant (local or API) stores results with:

* ⏱ Timestamp
* 📍 Source
* 🔍 Embedded content for future recall (RAG)

> The more you use SuperBrain, the smarter it gets.

---

## 🛡️ Ethics Statement

SuperBrain provides uncensored tools. That makes **your ethical responsibility** vital.

This platform:

* ✅ Promotes research, privacy, open exploration
* ❌ Prohibits illegal, unethical, or abusive use
* 🛡 Defends the right to study and investigate safely

Use it wisely. Empower, don't exploit.

---

## 👮 Author & License

**SuperBrain AI Platform**
Created by **David Louis-Charles** ([KatchDaVizion](https://github.com/KatchDaVizion))
© 2025 — MIT License

Embedded Signature:

```python
__author_id__ = "KatchDaVizion_2025_DLC_SIG"
def check_license():
    return "David Louis-Charles" in __author_id__
```

Includes models from [ageitgey/face\_recognition\_models](https://github.com/ageitgey/face_recognition_models) (MIT).

---

## 📦 Distribution

* 📂 GitHub: [github.com/KatchDaVizion/SuperBrain\_AI](https://github.com/KatchDaVizion/SuperBrain_AI)
* 🛍️ Gumroad Pro (coming soon)
* 💽 Bootable USB version available upon request

---

## 🙌 Community & Support

* 🛠 Issues welcome
* 🤝 Contributions encouraged
* 💬 Feedback always appreciated

> Built for ethical intelligence by David Louis-Charles.

**#OfflineAI #UncensoredLLM #CyberSecurity #OSINT #PrivacyTech #SuperBrainAI #RAG #DarkWebResearch #AI4Good**
