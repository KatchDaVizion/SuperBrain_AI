# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

import face_recognition
import os
import sys
import cv2

KNOWN_DIR = "security/faces/known"

def load_known_faces():
    encodings, names = [], []
    for name in os.listdir(KNOWN_DIR):
        person_dir = os.path.join(KNOWN_DIR, name)
        if os.path.isdir(person_dir):
            for file in os.listdir(person_dir):
                if file.endswith((".jpg", ".jpeg", ".png")):
                    path = os.path.join(person_dir, file)
                    image = face_recognition.load_image_file(path)
                    try:
                        enc = face_recognition.face_encodings(image)[0]
                        encodings.append(enc)
                        names.append(name)
                    except IndexError:
                        print(f"[!] No face in {file}")
    return encodings, names

def match_single_face(image_path):
    known_encodings, known_names = load_known_faces()
    image = face_recognition.load_image_file(image_path)
    locations = face_recognition.face_locations(image)
    encodings = face_recognition.face_encodings(image, locations)

    image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    for (top, right, bottom, left), encoding in zip(locations, encodings):
        results = face_recognition.compare_faces(known_encodings, encoding)
        name = "Unknown"
        if True in results:
            name = known_names[results.index(True)]
        print(f"[🧠] Match found: {name}")
        cv2.rectangle(image_bgr, (left, top), (right, bottom), (255, 0, 0), 2)
        cv2.putText(image_bgr, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    cv2.imshow("Single Match", image_bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python single_face_match.py <image_path>")
        sys.exit(1)
    match_single_face(sys.argv[1])


__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    allowed_user = "David Louis-Charles"
    return allowed_user in __author_id__
