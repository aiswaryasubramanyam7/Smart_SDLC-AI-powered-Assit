import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("IBM_API_KEY")
URL = os.getenv("IBM_URL")

def ask_watsonx(prompt, model_id="granite-13b-chat-v1"):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model_id": model_id,
        "input": prompt,
        "parameters": {
            "decoding_method": "greedy",
            "max_new_tokens": 200
        }
    }
    response = requests.post(f"{URL}/ml/v1/text/generation", headers=headers, json=data)
    return response.json()['results'][0]['generated_text']
