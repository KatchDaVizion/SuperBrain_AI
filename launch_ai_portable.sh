#!/bin/bash
#SuperBrain AI Platform
#Created by David Louis-Charles (GitHub: KatchDaVizion)
#© 2025 All Rights Reserved — https://github.com/KatchDaVizion


# ====================== CONFIG ======================
PROJECT_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PYTHON_BIN="python3"
REQUIREMENTS_FILE="$PROJECT_ROOT/requirements.txt"
TOR_SERVICE_NAME="tor"
OS_TYPE=$(uname -s)
IS_WSL=$(grep -i microsoft /proc/version 2>/dev/null)
OLLAMA_PID_FILE="$PROJECT_ROOT/ollama.pid"
RESOURCE_MONITOR_PID_FILE="$PROJECT_ROOT/resource_monitor.pid"
VENV_DIR="$HOME/safe_venv" # Assuming you always use the home venv now
# ====================================================

echo -e "\n🧠 [SuperBrain AI Portable Launcher]"
python3 update_check.py
echo "[+] Detecting environment and preparing system..."
OS_NAME=$(lsb_release -ds 2>/dev/null || grep PRETTY_NAME /etc/os-release | cut -d= -f2 | tr -d '"')
echo "[🌐] Detected OS: $OS_NAME"

# --- Create virtual environment if needed ---
if [ ! -d "$VENV_DIR" ]; then
    echo "[+] Creating virtual environment..."
    $PYTHON_BIN -m venv "$VENV_DIR"
fi

# --- Activate virtual environment ---
echo "[+] Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# ================== INSTALL BASICS ==================
echo "[+] Ensuring pip and setuptools are up to date..."
pip install --upgrade pip setuptools --break-system-packages

# macOS specific fallback for Tor and Python
if [[ "$OS_TYPE" == "Darwin" ]]; then
    echo "[🍏] macOS detected. Using brew for Tor if needed."
    if ! command -v tor &>/dev/null; then
        echo "[+] Installing Tor via brew..."
        brew install tor
    fi
fi

# ================== REQUIREMENTS =====================
echo "[+] Installing dependencies from requirements.txt..."
while IFS= read -r package; do
    [[ -z "$package" || "$package" == \#* ]] && continue
    base_package=$(echo "$package" | sed 's/[<>=].*//')
    if ! pip show "$base_package" &>/dev/null; then
        echo "[📦] Installing: $package"
        pip install "$package" --break-system-packages
    fi
done < "$REQUIREMENTS_FILE"


# ==================== START OLLAMA ===================
start_ollama() {
    echo "[+] Starting Ollama in the background..."
    ollama serve > /dev/null 2>&1 &
    echo $! > "$OLLAMA_PID_FILE"
    sleep 2 # Give Ollama a moment to start
}

stop_ollama() {
    if [ -f "$OLLAMA_PID_FILE" ]; then
        OLLAMA_PID=$(cat "$OLLAMA_PID_FILE")
        echo "[+] Stopping Ollama (PID: $OLLAMA_PID)..."
        kill "$OLLAMA_PID" 2>/dev/null
        rm -f "$OLLAMA_PID_FILE"
    fi
}

# ============ START RESOURCE MONITOR (OPTIONAL) =======
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


# ==================== MAIN MENU =====================
echo ""
echo "🧠 Welcome to SuperBrain Launcher"
echo "----------------------------------"
echo "1. Run OpenAI Assistant"
echo "2. Run Claude Assistant"
echo "3. Run Gemini Assistant"
echo "4. Run Groq Assistant"
echo "5. Run Local LLM Assistant (Ollama)"
echo "    a) tinyllama"
echo "    b) llama2"
echo "    c) mistral"
echo "    d) phi-3"
echo "    ..." # Ajouter d'autres modèles que tu as téléchargés
echo "6. Run Multi-Model Assistant"
echo "7. Run Face Recognition Agent"
echo "8. Run Dark Web Scraper"
echo "9. Manual Document/Text Ingestion"
echo "10. Quit"

read -p "Choose an assistant [1-10] or local LLM [a-z]: " choice
echo ""

OLLAMA_RUNNING=false
RESOURCE_MONITOR_RUNNING=false

case "$choice" in
    1) "$VENV_DIR/bin/python3" openai_assistant.py ;;
    2) "$VENV_DIR/bin/python3" Claude_assistant.py ;;
    3) "$VENV_DIR/bin/python3" gemini_assistant.py ;;
    4) "$VENV_DIR/bin/python3" groq_assistant.py ;;
    5) start_ollama; OLLAMA_RUNNING=true; "$VENV_DIR/bin/python3" local_llm_assistant.py ;;
    5a) start_ollama; OLLAMA_RUNNING=true; "$VENV_DIR/bin/python3" local_llm_assistant.py tinyllama ;;
    5b) start_ollama; OLLAMA_RUNNING=true; "$VENV_DIR/bin/python3" local_llm_assistant.py llama2 ;;
    5c) start_ollama; OLLAMA_RUNNING=true; "$VENV_DIR/bin/python3" local_llm_assistant.py mistral ;;
    5d) start_ollama; OLLAMA_RUNNING=true; "$VENV_DIR/bin/python3" local_llm_assistant.py phi-3 ;;
    6) "$VENV_DIR/bin/python3" multi_ai_query.py ;;
    7) "$VENV_DIR/bin/python3" face_recognition_agent.py ;;
    8) "$VENV_DIR/bin/python3" scrapers/darkweb_scraper.py ;;
    9) "$VENV_DIR/bin/python3" utils/ingest_text_manual.py ;;
    10) echo "[👋] Exiting. Stay sharp." && deactivate && exit 0 ;;
    *) echo "[❌] Invalid choice. Exiting." ;;
esac

# ============ CLEANUP PROMPT (OPTIONAL) ============
echo ""
DEACTIVATE_PROMPT=""

if "$OLLAMA_RUNNING"; then
    DEACTIVATE_PROMPT="$DEACTIVATE_PROMPT'Stop Ollama? (y/n): "
fi

if "$RESOURCE_MONITOR_RUNNING"; then
    DEACTIVATE_PROMPT="$DEACTIVATE_PROMPT'Stop Resource Monitor? (y/n): "
fi

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
