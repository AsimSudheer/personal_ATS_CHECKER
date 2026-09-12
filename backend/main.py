import os
from fastapi import FastAPI, UploadFile, File,Form
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from services.pdf_services import extract_text_from_pdf
from services.llm_service import create_json, perform_ats_check
from dotenv import load_dotenv
from pydantic import BaseModel


app = FastAPI()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok = True)

load_dotenv()  

app.add_middleware(CORSMiddleware,
                allow_origins = ["http://localhost:5174"],
                allow_methods = ["*"],
                allow_headers = ["*"])

API_KEY = os.getenv("GEMINI_API_KEY")

@app.post("/uploads/")
async def upload_file(file: UploadFile = File(...),job_description: str = Form(...)):
    file_path = UPLOAD_DIR/file.filename

    with open(file_path,"wb") as f:
        f.write(await file.read())
    resume_text = extract_text_from_pdf(file_path)
     

    jd_text = job_description.strip()

    ats_score = perform_ats_check(resume_text,jd_text,API_KEY)

    return ats_score


