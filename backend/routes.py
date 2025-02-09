from fastapi import APIRouter, HTTPException
from chatbot import get_chatbot_response

chatbot_router = APIRouter()

@chatbot_router.post("/chat")
def chat(user_message: str):
    try:
        bot_response = get_chatbot_response(user_message)
        return {"response": bot_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
