# 🧠 Platform_SuperBrain — Portable AI Intelligence Framework

## Features
- Query multiple AIs: OpenAI, Claude, Gemini, Groq, Local LLMs
- Face recognition (batch + single match)
- TOR + Web scraper agents
- Text/document ingestion for memory
- Memory visualizer, deduplicator, and summarizer
- Self-updater
- Plugin system for modular AI tools

## Setup

1. Run the launcher:
```bash
./launch_ai_portable.sh


🔒 API Keys
OpenAI: https://platform.openai.com/account/api-keys

Claude: https://console.anthropic.com

Gemini: https://makersuite.google.com/app/apikey

Groq: https://console.groq.com
--------------------------------------------

Explanation of Each Menu Option
Option	Description
1. OpenAI Assistant	Connects to GPT-4 or GPT-3.5 via your OpenAI API. Uses it for powerful online reasoning.
2. Claude Assistant	Uses Anthropic’s Claude model via API. Good for summarization, long documents, and safe responses.
3. Gemini Assistant	Uses Google’s Gemini 1.5 API. Often better at reasoning or creative tasks.
4. Groq Assistant	Uses Groq’s LLMs (like Mixtral). Extremely fast inference from cloud API.
5. Local LLM Assistant (Ollama)	Uses models like TinyLlama, Phi-3, Gemma-2B, LLaMA-2 loaded locally on your system. Runs even offline.
6. Multi-Model Assistant	Queries all the online APIs and local LLMs in parallel, compares results, and saves all responses to memory.
7. Face Recognition Agent	Uses OpenCV and face_recognition to compare known and unknown face images and logs results.
8. Dark Web Scraper	Connects to .onion websites using Tor and scrapes content for keywords or patterns.
9. Manual Document/Text Ingestion	You can paste in raw text or load files (PDF, DOCX, TXT) to train the local memory module.
10. Quit	Exits the script.

------------------------------------------------------

Example: Add facts from a file
You can add a command like this in a script (ingest_knowledge.py):


save_entry(source=source, content=text, timestamp=timestamp)
print(f"[+] Knowledge added to memory.")
✅ Usage:
bash

python ingest_knowledge.py "The CIA World Factbook says Iran has over 86 million people as of 2024."
That text is now embedded and searchable in the assistant’s memory.

-------------------------------------------------------

The face_recognition_agent.py script:

Loads known faces (from images)

Scans and compares unknown images or webcam frames

Returns matches with names or "Unknown"

Optionally visualizes with OpenCV face boxes
