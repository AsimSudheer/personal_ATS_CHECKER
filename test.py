
import pdfplumber
from pathlib import Path

file_path = Path(r"C:\Users\Asim\Documents\projects\ATS_resume\backend\uploads\Ai_eng_resume.pdf")

parser = pdfplumber.open(file_path)

text = ""

for page in parser.pages:
    text += page.extract_text()

print(text)