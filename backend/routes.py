from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from chatbot import get_chatbot_response  # Ensure chatbot.py is in the same directory

chatbot_router = APIRouter()

# Define a request model for receiving messages
class ChatRequest(BaseModel):
    user_message: str

@chatbot_router.post("/chat")
def chat(request: ChatRequest, response_func=Depends(get_chatbot_response)):
    """API endpoint to chat with the Gemini-powered chatbot."""
    try:
        if not request.user_message:
            raise HTTPException(status_code=400, detail="User message is required")
        
        bot_response = response_func(request.user_message)
        return {"response": bot_response}
    
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
