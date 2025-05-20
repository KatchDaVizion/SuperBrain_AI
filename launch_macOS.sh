#!/bin/bash
# SuperBrain AI macOS Launcher
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# Version: 1.0.1 | Updated: 2025-05-19

set -e

# =============== CONFIGURATION ===============
PROJECT_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PYTHON_BIN="python3"
REQUIREMENTS_FILE="$PROJECT_ROOT/requirements.txt"
OLLAMA_PID_FILE="$PROJECT_ROOT/ollama.pid"
VENV_DIR="$HOME/safe_venv"
# =============================================

echo -e "\n🧠 [SuperBrain AI macOS Launcher]"
echo "[+] Setting up environment on macOS..."

# =============== OFFLINE DETECTION ===============
is_offline() {
  ping -q -c 1 -W 1 8.8.8.8 >/dev/null 2>&1 || return 0
  return 1
}

if is_offline; then
  echo "[🔌] Offline mode detected. Skipping pip updates."
  OFFLINE=true
else
  python3 update_check.py || true
  OFFLINE=false
fi

# ========== Homebrew Setup ==========
if ! command -v brew &> /dev/null; then
  echo "🍺 Installing Homebrew..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
  eval "$(/opt/homebrew/bin/brew shellenv)"
else
  eval "$(/opt/homebrew/bin/brew shellenv)"
fi

# ========== Install System Packages ==========
echo "🧱 Installing required system packages..."
brew install cmake boost python libomp pkg-config openblas ffmpeg libjpeg tor || true
xcode-select --install || true

# ========== VENV Setup ==========
echo ""
read -p "[🧰] Use a safe venv in your HOME directory instead of local folder? (y/n): " use_home_venv
if [[ "$use_home_venv" =~ ^[Yy]$ ]]; then
  VENV_DIR="$HOME/safe_venv"
else
  VENV_DIR="$PROJECT_ROOT/venv"
fi
echo "[📁] Using virtual environment at: $VENV_DIR"

if [ ! -d "$VENV_DIR" ]; then
  echo "[+] Creating virtual environment..."
  $PYTHON_BIN -m venv "$VENV_DIR"
fi
source "$VENV_DIR/bin/activate"

# ========== Upgrade pip ==========
if [ "$OFFLINE" = false ]; then
  echo "[📦] Upgrading pip and setuptools..."
  pip install --upgrade pip setuptools wheel
fi

# ========== Install Python Requirements ==========
echo "[📜] Installing Python dependencies..."
while IFS= read -r package; do
  [[ -z "$package" || "$package" == \#* ]] && continue
  base_package=$(echo "$package" | sed 's/[<>=].*//')

  if ! pip show "$base_package" &>/dev/null; then
    echo "[📦] Installing: $package"
    pip install "$package" || echo "[⚠️] Couldn't install: $package"
  fi

  [[ "$package" == openai* ]] && pip install openai==0.28

  if [[ "$package" == face_recognition* ]]; then
    pip install dlib --no-cache-dir --force-reinstall || echo "[⚠️] dlib failed manually, skipping."
  fi
done < "$REQUIREMENTS_FILE"

# ========== Tor Setup ==========
echo "[🔒] Checking Tor..."
if ! command -v tor &>/dev/null; then
  echo "[+] Tor not found, installing via Homebrew..."
  brew install tor || echo "[❗] Please install Tor manually if this fails."
fi

echo "[🔄] Restarting Tor..."
pkill tor || true
nohup tor > /dev/null 2>&1 &
sleep 3

pgrep tor >/dev/null && echo "[🧅] Tor is running." || echo "[🔴] Tor failed to start."

# ========== Ollama Functions ==========
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

# ========== MAIN MENU ==========
echo ""
echo "🧠 Welcome to SuperBrain Launcher (macOS)"
echo "----------------------------------"
echo "1. Run OpenAI Assistant"
echo "2. Run Claude Assistant"
echo "3. Run Gemini Assistant"
echo "4. Run Groq Assistant"
echo "5. Run Local LLM Assistant (Ollama)"
echo "   a) tinyllama"
echo "   b) llama2"
echo "   c) mistral"
echo "   d) phi-3"
echo "6. Run Multi-Model Assistant"
echo "7. Run Face Recognition Agent"
echo "8. Run Dark Web Scraper"
echo "9. Manual Document/Text Ingestion"
echo "10. Quit"
echo ""

read -p "Choose an assistant [1-10] or local LLM [a-z]: " choice
echo ""

case "$choice" in
  1) python3 openai_assistant.py ;;
  2) python3 Claude_assistant.py ;;
  3) python3 gemini_assistant.py ;;
  4) python3 groq_assistant.py ;;
  5) start_ollama; python3 local_llm_assistant.py ;;
  5a) start_ollama; python3 local_llm_assistant.py tinyllama ;;
  5b) start_ollama; python3 local_llm_assistant.py llama2 ;;
  5c) start_ollama; python3 local_llm_assistant.py mistral ;;
  5d) start_ollama; python3 local_llm_assistant.py phi-3 ;;
  6) python3 multi_ai_query.py ;;
  7) python3 face_recognition_agent.py ;;
  8) python3 scrapers/darkweb_scraper.py ;;
  9) python3 utils/ingest_text_manual.py ;;
  10) echo "[👋] Exiting. Bye!" && deactivate && exit 0 ;;
  *) echo "[❌] Invalid choice. Exiting." ;;
esac

# ========== Optional Cleanup ==========
echo ""
if [[ "$use_home_venv" =~ ^[Yy]$ ]]; then
  read -p "[🧹] Delete $VENV_DIR to save space? (y/n): " cleanup
  if [[ "$cleanup" =~ ^[Yy]$ ]]; then
    deactivate
    rm -rf "$VENV_DIR"
    echo "[✅] Deleted: $VENV_DIR"
  else
    echo "[📁] Keeping virtual environment for next session."
  fi
fi

deactivate
export __author_id__="DLC-KDV-SuperBrain-2025"
exit 0
