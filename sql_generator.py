import google.generativeai as genai
from prompt_templates import SYSTEM_PROMPT

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_sql(user_requirement):

    prompt = f"""
    {SYSTEM_PROMPT}

    User Requirement:
    {user_requirement}
    """

    response = model.generate_content(prompt)

    return response.text