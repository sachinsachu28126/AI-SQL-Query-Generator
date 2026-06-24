import os
from dotenv import load_dotenv
import google.generativeai as genai
from prompt_templates import SYSTEM_PROMPT

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found in .env file"
    )

genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_sql(user_requirement):

    prompt = f"""
    {SYSTEM_PROMPT}

    User Requirement:
    {user_requirement}
    """

    try:
        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"ERROR: {str(e)}"