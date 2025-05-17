# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

import face_recognition
import os
import json
from datetime import datetime

KNOWN_FACES_DIR = "security/known_faces"
UNKNOWN_FACES_DIR = "security/unknown_faces"
LOG_FILE = "logs/face_log.json"
ALLOWED_EXTENSIONS = (".jpg", ".jpeg", ".png")

def load_known_faces():
    known_encodings = []
    known_names = []

    for name in os.listdir(KNOWN_FACES_DIR):
        person_dir = os.path.join(KNOWN_FACES_DIR, name)
        if not os.path.isdir(person_dir):
            continue
        for filename in os.listdir(person_dir):
            if filename.lower().endswith(ALLOWED_EXTENSIONS):
                img_path = os.path.join(person_dir, filename)
                try:
                    image = face_recognition.load_image_file(img_path)
                    encoding = face_recognition.face_encodings(image)[0]
                    known_encodings.append(encoding)
                    known_names.append(name)
                except IndexError:
                    print(f"[⚠️] No face found in {filename}")
                except Exception as e:
                    print(f"[❌] Error loading {filename}: {e}")
    return known_encodings, known_names

def recognize_faces():
    known_encodings, known_names = load_known_faces()

    for filename in os.listdir(UNKNOWN_FACES_DIR):
        if not filename.lower().endswith(ALLOWED_EXTENSIONS):
            continue
        img_path = os.path.join(UNKNOWN_FACES_DIR, filename)
        image = face_recognition.load_image_file(img_path)
        unknown_encodings = face_recognition.face_encodings(image)

        for encoding in unknown_encodings:
            results = face_recognition.compare_faces(known_encodings, encoding)
            match_name = "Unknown"
            if True in results:
                match_name = known_names[results.index(True)]

            print(f"[🧠] Match found: {match_name}")
            log_entry = {
                "timestamp": str(datetime.now()),
                "image": filename,
                "match": match_name
            }
            save_log(log_entry)

def save_log(entry):
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([entry], f, indent=2)
    else:
        with open(LOG_FILE, "r+") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
            data.append(entry)
            f.seek(0)
            json.dump(data, f, indent=2)

if __name__ == "__main__":
    recognize_faces()


__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    allowed_user = "David Louis-Charles"
    return allowed_user in __author_id__
