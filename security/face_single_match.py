# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

import face_recognition
import os
import sys

KNOWN_FACES_DIR = "security/known_faces"
ALLOWED_EXTENSIONS = (".jpg", ".jpeg", ".png")

def recognize_face(image_to_check):
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
                    known_image = face_recognition.load_image_file(img_path)
                    encoding = face_recognition.face_encodings(known_image)[0]
                    known_encodings.append(encoding)
                    known_names.append(name)
                except:
                    continue

    try:
        unknown_image = face_recognition.load_image_file(image_to_check)
        unknown_face_encodings = face_recognition.face_encodings(unknown_image)
    except Exception as e:
        print(f"[❌] Error loading target image: {e}")
        return

    if not unknown_face_encodings:
        print("[❌] No faces found in the input image.")
        return

    for unknown_face_encoding in unknown_face_encodings:
        matches = face_recognition.compare_faces(known_encodings, unknown_face_encoding)
        if True in matches:
            match_index = matches.index(True)
            print(f"[✅] Match found: {known_names[match_index]}")
        else:
            print("[❌] No match found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python face_single_match.py <image_path>")
        sys.exit(1)
    recognize_face(sys.argv[1])


__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    allowed_user = "David Louis-Charles"
    return allowed_user in __author_id__
