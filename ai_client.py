import os
import requests
from dotenv import load_dotenv

load_dotenv()

GRADIENT_API_URL = os.getenv("GRADIENT_API_URL")
GRADIENT_API_KEY = os.getenv("GRADIENT_API_KEY")

def get_ai_response(prompt: str):
    headers = {"Authorization": f"Bearer {GRADIENT_API_KEY}"}
    payload = {"prompt": prompt, "max_tokens": 150}
    response = requests.post(GRADIENT_API_URL, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json().get("text", "")
    else:
        return f"Error: {response.status_code}, {response.text}"
