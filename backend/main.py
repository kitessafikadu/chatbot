from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import chatbot_router

app = FastAPI()

app.include_router(chatbot_router)

# 🔹 Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.get("/")
def read_root():
    return {"message": "Chatbot API is running!"}
