import json
import google.generativeai as genai

def create_json(text, api_key):
    genai.configure(api_key=api_key)
    
    
    model = genai.GenerativeModel('gemini-3.6-flash')

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