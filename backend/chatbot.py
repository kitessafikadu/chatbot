import google.generativeai as genai
# from google import genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API Key from .env
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY is missing from environment variables!")

# Configure the Gemini API
genai.configure(api_key=API_KEY)

# Initialize the free-tier Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")  # Use "gemini-1.5-pro" if needed

def get_chatbot_response(user_message: str):
    """Generate a response from Gemini AI based on user input."""
    try:
        response = model.generate_content(user_message)
        return response.text  # Extract the AI-generated text
    except Exception as e:
        print(f"❌ Gemini API Error: {e}")
        return "Sorry, I couldn't process your request."
