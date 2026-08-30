import pdfplumber
from pathlib import Path


def extract_text_from_pdf(file_path):
    
    parser = pdfplumber.open(file_path)

    text = ""

    for page in parser.pages:
        text += page.extract_text()

    return text












    