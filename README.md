# 🤖 Chatbot

A smart chatbot built with **React, Tailwind CSS, FastAPI, and Gemini API**. This chatbot provides intelligent responses and can be integrated into various applications for automated conversations.

## ✨ Features
- ⚡ Real-time chat functionality
- 🎨 User-friendly interface with Tailwind CSS
- 🚀 Backend powered by FastAPI
- 🧠 AI-powered responses using Gemini API
- 🎯 Efficient state management in React

## 🛠 Tech Stack
### 🖥 Frontend:
- ⚛ **React**: Component-based UI development
- 🎨 **Tailwind CSS**: Modern and responsive styling

### ⚙ Backend:
- ⚡ **FastAPI**: High-performance backend with Python
- 🤖 **Gemini API**: AI-driven chatbot intelligence

## 📦 Installation & Setup
### 📌 Prerequisites
Ensure you have the following installed:
- 🟢 Node.js & npm (for frontend)
- 🐍 Python & FastAPI (for backend)

### 💻 Frontend Setup
```bash
# 📥 Clone the repository
git clone https://github.com/kitessafikadu/chatbot.git
cd chatbot/frontend

# 📦 Install dependencies
npm install

# 🚀 Start the development server
npm run dev
```

### ⚙ Backend Setup
```bash
cd chatbot/backend

# 🏗 Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# 📦 Install dependencies
pip install -r requirements.txt

# 🚀 Run the FastAPI server
uvicorn main:app --reload
```

## ⚙ Configuration
Create a `.env` file in the backend directory to store your API key:
```env
GEMINI_API_KEY=your_api_key_here
```

## 🚀 Usage
1. Start both frontend and backend servers.
2. 🤖 Interact with the chatbot and enjoy AI-powered responses!


