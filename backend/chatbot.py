import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_chatbot_response(user_input: str):
    response = openai.ChatCompletion.create(
         model="gpt-4o-mini",
        messages=[{"role": "system", "content": "You are a helpful e-commerce chatbot."},
                  {"role": "user", "content": user_input}]
    )
    return response["choices"][0]["message"]["content"]
