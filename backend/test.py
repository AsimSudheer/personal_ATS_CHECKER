import spacy
from pathlib import Path
from pypdf import PdfReader


folder_path = Path(r"C:/Users/Asim/Documents/projects/ATS_resume/backend/uploads")
file_name = "Ai_eng_resume.pdf"

full_path = folder_path/file_name

reader = PdfReader(full_path)

raw_text = ""
for page in reader.pages:
    raw_text += page.extract_text()

try:

    nlp = spacy.load("en_core_web_sm")


    doc = nlp(raw_text)


    print("spacy installed successfully")
    print("the extractted entities are:")
    for ent in doc.ents:
        print(f"-{ent.text}({ent.label_})")


except Exception as e:
    print("error occured")
    print(e) 
