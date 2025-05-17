# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

from datetime import datetime
import os
from PyPDF2 import PdfReader
from utils.memory import save_entry  # Make sure this exists and is properly imported

def ingest_text_file(file_path):
    print(f"[+] Ingesting text file: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if len(line) > 10:
                save_entry(source=os.path.basename(file_path), content=line, timestamp=datetime.now().isoformat())

def ingest_pdf_file(file_path):
    print(f"[+] Ingesting PDF file: {file_path}")
    reader = PdfReader(file_path)
    for page in reader.pages:
        text = page.extract_text()
        if text:
            for paragraph in text.split("\n"):
                paragraph = paragraph.strip()
                if len(paragraph) > 10:
                    save_entry(source=os.path.basename(file_path), content=paragraph, timestamp=datetime.now().isoformat())

def bulk_ingest(folder_path):
    print(f"[+] Bulk ingesting from: {folder_path}")
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        if file.endswith(".txt"):
            ingest_text_file(full_path)
        elif file.endswith(".pdf"):
            ingest_pdf_file(full_path)
        else:
            print(f"[-] Unsupported file type: {file}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python ingest_knowledge.py <folder_path>")
        exit(1)
    folder = sys.argv[1]
    bulk_ingest(folder)


__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    allowed_user = "David Louis-Charles"
    return allowed_user in __author_id__
