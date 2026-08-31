import os
from fastapi import FastAPI, UploadFile, File
from pathlib import Path
from services.pdf_services import extract_text_from_pdf
from services.llm_service import create_json, perform_ats_check
from dotenv import load_dotenv
from pydantic import BaseModel


app = FastAPI()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok = True)

load_dotenv()  

API_KEY = os.getenv("GEMINI_API_KEY")

@app.post("/uploads/")
async def upload_file(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR/file.filename

    with open(file_path,"wb") as f:
        f.write(await file.read())
    resume_text = extract_text_from_pdf(file_path)
    resume_generated_content = create_json(resume_text,API_KEY) 

    return resume_generated_content

class JobDescription(BaseModel):
    text : str

class ATSRequest(BaseModel):
    resume_text: str
    job_description: str

@app.post("/upload_jd/")
async def paste_job_description(data: JobDescription):
    char_length = len(data.text)
    raw_text = data.text.strip()
    job_desc = extract_text_from_pdf(raw_text) if raw_text.endswith('.pdf') else raw_text
    return {
        "status": "success",
        "job_description": job_desc,
        "length": char_length,

    }

@app.post("/ats_check/")
async def ats_checking(data: ATSRequest):
    main_result = perform_ats_check(data.resume_text, data.job_description, API_KEY)

    return main_result