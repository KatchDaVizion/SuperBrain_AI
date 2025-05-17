import requests

def get_local_version():
    with open("version.txt") as f:
        return f.read().strip()

def get_remote_version():
    url = "https://raw.githubusercontent.com/KatchDaVizion/SuperBrain_AI/main/version.txt"
    try:
        return requests.get(url, timeout=5).text.strip()
    except:
        return "unknown"

def check_for_updates():
    local = get_local_version()
    remote = get_remote_version()
    if local != remote:
        print(f"[🔄] Update available! Local: {local} → Remote: {remote}")
        print("Run ./update_superbrain.sh to update.")
    else:
        print("[✅] SuperBrain is up to date.")

if __name__ == "__main__":
    check_for_updates()
