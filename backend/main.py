import os
from fastapi import FastAPI, UploadFile, File
from pathlib import Path
from services.pdf_services import extract_text_from_pdf
from services.llm_service import create_json
from dotenv import load_dotenv
from pydantic import BaseModel


app = FastAPI()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok = True)

load_dotenv()  

API_KEY = os.getenv("GEMINI_API_KEY")

@app.post("/uploads/")
async def uplload_file(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR/file.filename

    with open(file_path,"wb") as f:
        f.write(await file.read())

    resume_text = extract_text_from_pdf(file_path)
    resume_generated_content = create_json(resume_text,API_KEY) 

    return resume_generated_content

class JobDescription(BaseModel):
    text : str

@app.post("/paste_JD/")

async def paste_job_description(data: JobDescription):
    char_length = len(data.text)
    
    return {
        "status": "success",
        "job_description": data.text,
        "length": char_length
    }