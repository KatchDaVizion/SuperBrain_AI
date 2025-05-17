#!/bin/bash
# ──────────────────────────────────────────────
# SuperBrain Auto-Updater by David Louis-Charles (KatchDaVizion)
# ──────────────────────────────────────────────
echo "[🧠] Checking for updates..."

if [ ! -d .git ]; then
  echo "[!] Git repo not initialized. Cannot pull updates."
  exit 1
fi

git stash
git pull origin main
echo "[✅] SuperBrain has been updated to the latest version."
