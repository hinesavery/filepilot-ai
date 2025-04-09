import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for organizing files."},
            {"role": "user", "content": "Suggest a folder for 'vacation_photos_june2023.jpg'"}
        ]
    )
    print("✅ GPT response:", response.choices[0].message["content"].strip())
except Exception as e:
    print("❌ Error:", e)
