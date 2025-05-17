# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

import os
import face_recognition
import cv2
import zipfile
import datetime
import json

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KNOWN_DIR = os.path.join(BASE_DIR, "known_faces")
UNKNOWN_DIR = os.path.join(BASE_DIR, "unknown_faces")
MEMORY_FILE = os.path.join(BASE_DIR, "memory_db.json")

# Unzip face packs
for file in os.listdir(KNOWN_DIR):
    if file.endswith(".zip"):
        zip_path = os.path.join(KNOWN_DIR, file)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(KNOWN_DIR)
        os.remove(zip_path)

# Load known faces
known_encodings = []
known_names = []

for file in os.listdir(KNOWN_DIR):
    if file.lower().endswith((".jpg", ".jpeg", ".png")):
        image_path = os.path.join(KNOWN_DIR, file)
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)
        if encoding:
            known_encodings.append(encoding[0])
            known_names.append(os.path.splitext(file)[0])

# Process unknown faces
for file in os.listdir(UNKNOWN_DIR):
    if file.lower().endswith((".jpg", ".jpeg", ".png")):
        image_path = os.path.join(UNKNOWN_DIR, file)
        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)
        img = cv2.imread(image_path)

        for (top, right, bottom, left), encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_encodings, encoding)
            name = "Unknown"

            if True in matches:
                name = known_names[matches.index(True)]

            timestamp = datetime.datetime.now().isoformat()
            print(f"[{timestamp}] Match found: {name}")
            # Save to memory
            entry = {
                "source": "Face Recognition",
                "timestamp": timestamp,
                "matched_name": name,
                "file": file
            }

            if os.path.exists(MEMORY_FILE):
                with open(MEMORY_FILE, "r") as f:
                    data = json.load(f)
            else:
                data = []

            data.append(entry)
            with open(MEMORY_FILE, "w") as f:
                json.dump(data, f, indent=4)

            # Draw on face
            cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(img, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1)

        # Display result
        cv2.imshow("Face Recognition", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    allowed_user = "David Louis-Charles"
    return allowed_user in __author_id__
