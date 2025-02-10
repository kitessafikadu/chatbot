from fastapi import APIRouter, HTTPException
from chatbot import get_chatbot_response

chatbot_router = APIRouter()

@chatbot_router.post("/chat")
def chat(user_message: str):
    try:
        if not user_message:
            raise HTTPException(status_code=400, detail="User message is required")
        
        bot_response = get_chatbot_response(user_message)
        return {"response": bot_response}
    
    except Exception as e:
        print(f"Error: {e}")  
        raise HTTPException(status_code=500, detail=str(e))
