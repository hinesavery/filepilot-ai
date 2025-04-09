import os
from openai import OpenAI
from dotenv import load_dotenv
import re

# Load API key from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def clean_folder_name(name):
    # Remove unwanted characters and trim
    return re.sub(r'[^\w\-\s]', '', name.strip().title()) or "Unsorted"

def suggest_folder(file_name):
    prompt = f"""
You are an intelligent assistant for organizing digital files.

Based ONLY on the file name below, suggest a clean, clear folder name.
Give the answer in 1 or 2 words, no punctuation.

File name: {file_name}
Suggested folder:
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful file-organizing assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=15
        )
        raw = response.choices[0].message.content
        print(f"🔍 RAW GPT RESPONSE for {file_name}:\n{raw}")
        folder = clean_folder_name(raw)
        print(f"🧠 Cleaned Suggestion for {file_name}: {folder}")
        return folder
    except Exception as e:
        print(f"❌ OpenAI error for {file_name}: {e}")
        return "Unsorted"
