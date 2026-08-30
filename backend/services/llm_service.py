import json
import google.generativeai as genai

def create_json(text, api_key):
    genai.configure(api_key=api_key)
    
    
    model = genai.GenerativeModel('gemini-3.5-flash')

    prompt = f"""
    Extract the following information from this resume and return valid JSON:
    - technical_skills (list)
    - education (list with school, degree, year)
    - experience (list with company, position, duration)
    - projects (list with name, description)
    
    Resume text:
    {text}
    """
    
    response = model.generate_content(
        prompt,
        generation_config={"response_mime_type": "application/json"}
    )
    
    try:
        
        raw_text = response.text.strip()
        result = json.loads(raw_text)
        return result
    except Exception as e:
        print(f"DEBUG - Error parsing JSON: {e}")
        print(f"DEBUG - Response was: {response.text}")
        return {"error": str(e), "raw_response": response.text}


def perform_ats_check(resume_text, job_description, api_key):
    """
    Perform ATS (Applicant Tracking System) check
    Compares resume against job description and returns match analysis
    """
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-3.5-flash')
    
    prompt = f"""
    You are an ATS (Applicant Tracking System) expert. Analyze the resume against the job description and return a detailed JSON analysis.
    
    Resume:
    {resume_text}
    
    Job Description:
    {job_description}
    
    Return a JSON object with:
    1. match_score (0-100 percentage)
    2. matched_keywords (list of keywords from job description found in resume)
    3. missing_keywords (list of important keywords from job description NOT in resume)
    4. skills_match (object with required_skills list and matched_skills list)
    5. experience_match (brief assessment of experience level match)
    6. recommendations (list of specific suggestions to improve resume for this job)
    7. summary (one sentence overall assessment)
    
    Be thorough and specific in your analysis.
    """
    
    try:
        response = model.generate_content(
            prompt,
            generation_config={"response_mime_type": "application/json"}
        )
        
        raw_text = response.text.strip()
        result = json.loads(raw_text)
        return {"success": True, "ats_analysis": result}
    except Exception as e:
        print(f"DEBUG - Error in ATS check: {e}")
        print(f"DEBUG - Response was: {response.text if 'response' in locals() else 'No response'}")
        return {"success": False, "error": str(e)}