from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from chatbot import get_chatbot_response

chatbot_router = APIRouter()

# Define a request model for JSON input
class ChatRequest(BaseModel):
    user_message: str

@chatbot_router.post("/chat")
def chat(request: ChatRequest):
    """API endpoint to chat with the Gemini-powered chatbot."""
    try:
        print(f"📩 Received user message: {request.user_message}")  # Debugging

        if not request.user_message:
            raise HTTPException(status_code=400, detail="User message is required")
        
        bot_response = get_chatbot_response(request.user_message)

        print(f"📤 Sending bot response: {bot_response}")  # Debugging
        return {"response": bot_response}
    
    except Exception as e:
        print(f"❌ Internal Server Error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
