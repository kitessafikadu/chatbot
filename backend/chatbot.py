import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API Key from .env
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY is missing! Check your .env file.")

print(f"✅ Using API Key: {API_KEY[:5]}...")  # Print partial API key for debugging

# Configure Gemini API
genai.configure(api_key=API_KEY)

# Initialize the free-tier Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")  # Or "gemini-1.5-pro"

def get_chatbot_response(user_message: str):
    """Generate a response from Gemini AI based on user input."""
    try:
        print(f"📝 Sending message to Gemini: {user_message}")  # Debugging
        response = model.generate_content(user_message)
        print(f"✅ Response received: {response.text}")  # Debugging
        return response.text
    except Exception as e:
        print(f"❌ Gemini API Error: {e}")  # Log error
        return "Sorry, I couldn't process your request."
