#!/bin/bash
# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

# =============== CONFIGURATION ===============
PROJECT_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PYTHON_BIN="python3"
REQUIREMENTS_FILE="$PROJECT_ROOT/requirements.txt"
TOR_SERVICE_NAME="tor"
OS_TYPE=$(uname -s)
IS_WSL=$(grep -i microsoft /proc/version 2>/dev/null)
OLLAMA_PID_FILE="$PROJECT_ROOT/ollama.pid"
RESOURCE_MONITOR_PID_FILE="$PROJECT_ROOT/resource_monitor.pid"
VENV_DIR="$HOME/safe_venv"
# =============================================

echo -e "\n🧠 [SuperBrain AI Portable Launcher]"

# =============== OFFLINE DETECTION ===============
is_offline() {
    ping -q -c 1 -W 1 8.8.8.8 >/dev/null 2>&1 || return 0
    return 1
}

if is_offline; then
    echo "[🔌] Offline mode detected! Skipping updates and network checks."
    OFFLINE=true
else
    $PYTHON_BIN update_check.py
    OFFLINE=false
fi

# =============== ENVIRONMENT DETECTION ===============
echo "[+] Detecting environment and preparing system..."
OS_NAME=$(lsb_release -ds 2>/dev/null || grep PRETTY_NAME /etc/os-release | cut -d= -f2 | tr -d '"')
echo "[🌐] Detected OS: $OS_NAME"

# =============== VIRTUAL ENVIRONMENT ===============
if [ ! -d "$VENV_DIR" ]; then
    echo "[+] Creating virtual environment..."
    $PYTHON_BIN -m venv "$VENV_DIR"
fi

echo "[+] Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# =============== PIP UPGRADE ===============
if [ "$OFFLINE" = false ]; then
    echo "[+] Ensuring pip and setuptools are up to date..."
    pip install --upgrade pip setuptools --break-system-packages
fi

# macOS special case
if [[ "$OS_TYPE" == "Darwin" ]]; then
    echo "[🍏] macOS detected. Using brew for Tor if needed."
    if ! command -v tor &>/dev/null; then
        echo "[+] Installing Tor via brew..."
        brew install tor
    fi
fi

# =============== INSTALL REQUIREMENTS ===============
echo "[+] Installing dependencies from requirements.txt..."
while IFS= read -r package; do
    [[ -z "$package" || "$package" == \#* ]] && continue
    base_package=$(echo "$package" | sed 's/[<>=].*//')

    if ! pip show "$base_package" &>/dev/null; then
        echo "[📦] Installing: $package"
        pip install "$package" --break-system-packages || echo "[⚠️] Couldn't install: $package"
    fi

    [[ "$package" == openai* ]] && pip install openai==0.28 --break-system-packages

    if [[ "$package" == face_recognition* ]]; then
        sudo apt-get install -y cmake
        pip install dlib --no-cache-dir --force-reinstall --break-system-packages || echo "[⚠️] dlib failed manually, skipping for now."
    fi
done < "$REQUIREMENTS_FILE"

# =============== DAEMONS ===============
start_ollama() {
    echo "[+] Starting Ollama in the background..."
    ollama serve > /dev/null 2>&1 &
    echo $! > "$OLLAMA_PID_FILE"
    sleep 2
}

stop_ollama() {
    if [ -f "$OLLAMA_PID_FILE" ]; then
        OLLAMA_PID=$(cat "$OLLAMA_PID_FILE")
        echo "[+] Stopping Ollama (PID: $OLLAMA_PID)..."
        kill "$OLLAMA_PID" 2>/dev/null
        rm -f "$OLLAMA_PID_FILE"
    fi
}

start_resource_monitor() {
    echo "[+] Starting resource monitor in the background..."
    python3 utils/resource_monitor.py &
    echo $! > "$RESOURCE_MONITOR_PID_FILE"
}

stop_resource_monitor() {
    if [ -f "$RESOURCE_MONITOR_PID_FILE" ]; then
        RESOURCE_MONITOR_PID=$(cat "$RESOURCE_MONITOR_PID_FILE")
        echo "[+] Stopping resource monitor (PID: $RESOURCE_MONITOR_PID)..."
        kill "$RESOURCE_MONITOR_PID" 2>/dev/null
        rm -f "$RESOURCE_MONITOR_PID_FILE"
    fi
}

# =============== MAIN MENU ===============
echo ""
echo "🧠 Welcome to SuperBrain Launcher"
echo "----------------------------------"
echo "1. Run OpenAI Assistant"
echo "2. Run Claude Assistant"
echo "3. Run Gemini Assistant"
echo "4. Run Groq Assistant"
echo "5. Run Venice Assistant"
echo "6. Run Local LLM Assistant (Ollama)"
echo "    a) tinyllama"
echo "    b) llama2"
echo "    c) mistral"
echo "    d) phi-3"
echo "7. Run Multi-Model Assistant"
echo "8. Run Face Recognition Agent"
echo "9. Run Dark Web Scraper"
echo "10. Manual Document/Text Ingestion"
echo "11. Quit"
echo ""
read -p "Choose an assistant [1-11] or local LLM [a-z]: " choice

OLLAMA_RUNNING=false

case "$choice" in
    1) "$VENV_DIR/bin/python3" openai_assistant.py ;;
    2) "$VENV_DIR/bin/python3" Claude_assistant.py ;;
    3) "$VENV_DIR/bin/python3" gemini_assistant.py ;;
    4) "$VENV_DIR/bin/python3" groq_assistant.py ;;
    5) "$VENV_DIR/bin/python3" venice_assistant.py ;;
    6) start_ollama; OLLAMA_RUNNING=true; "$VENV_DIR/bin/python3" local_llm_assistant.py ;;
    6a) start_ollama; OLLAMA_RUNNING=true; "$VENV_DIR/bin/python3" local_llm_assistant.py tinyllama ;;
    6b) start_ollama; OLLAMA_RUNNING=true; "$VENV_DIR/bin/python3" local_llm_assistant.py llama2 ;;
    6c) start_ollama; OLLAMA_RUNNING=true; "$VENV_DIR/bin/python3" local_llm_assistant.py mistral ;;
    6d) start_ollama; OLLAMA_RUNNING=true; "$VENV_DIR/bin/python3" local_llm_assistant.py phi-3 ;;
    7) "$VENV_DIR/bin/python3" multi_ai_query.py ;;
    8) "$VENV_DIR/bin/python3" face_recognition_agent.py ;;
    9) "$VENV_DIR/bin/python3" scrapers/darkweb_scraper.py ;;
    10) "$VENV_DIR/bin/python3" utils/ingest_text_manual.py ;;
    11) echo "[👋] Exiting. Stay sharp." && deactivate && exit 0 ;;
    *) echo "[❌] Invalid choice. Exiting." ;;
esac

read -p "[🧹] Delete $VENV_DIR to save space? (y/n): " cleanup
if [[ "$cleanup" =~ ^[Yy]$ ]]; then
    deactivate
    rm -rf "$VENV_DIR"
    echo "[✅] Deleted: $VENV_DIR"
else
    echo "[📁] Keeping virtual environment for next session."
fi

deactivate
exit 0

export __author_id__="DLC-KDV-SuperBrain-2025"

