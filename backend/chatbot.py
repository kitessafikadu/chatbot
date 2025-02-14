from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("GEMINI_API_KEY"))

def get_chatbot_response(user_input: str):
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Change model if needed
            messages=[
                {"role": "system", "content": "You are a helpful e-commerce chatbot."},
                {"role": "user", "content": user_input},
            ]
        )
        return completion.choices[0].message.content  
    except Exception as e:
        print(f"❌ OpenAI API Error: {e}")  # Prints the actual error in the terminal
        return str(e)  # Sends error to the frontend for debugging
