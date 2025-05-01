import os
import requests
from dotenv import load_dotenv

load_dotenv()

def query_text_llm(prompt: str) -> str:
    url = os.environ["LLM_BASE"] + "/v1/chat/completions"
    token = os.environ["OPENAI_API_KEY"]  # or a custom API key

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "anvilgpt/gemma:latest",  # or another text LLM like gpt-4
        "messages": [
            {"role": "system", "content": "You are a helpful assistant for campus navigation."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        print("[ERROR] Text LLM API returned:", response.status_code)
        print("[DEBUG] Response text:", response.text)
        return "I couldn't process your request due to an API error."

    try:
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print("[ERROR] Failed to parse text LLM response:", e)
        return "There was a problem parsing the LLM response."
