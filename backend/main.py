from fastapi import FastAPI
from routes import chatbot_router

app = FastAPI()

app.include_router(chatbot_router)

@app.get("/")
def read_root():
    return {"message": "Chatbot API is running!"}
