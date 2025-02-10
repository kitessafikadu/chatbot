import { useState } from "react";
import axios from "axios";

const Chatbot = () => {
  const [messages, setMessages] = useState([
    { sender: "bot", text: "Hello! How can I assist you today?" },
  ]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return;

    const newMessages = [...messages, { sender: "user", text: input }];
    setMessages(newMessages);
    setInput("");

    try {
      const response = await axios.post("http://127.0.0.1:8000/chat", {
        user_message: input,
      });

      setMessages([
        ...newMessages,
        { sender: "bot", text: response.data.response },
      ]);
    } catch (error) {
      setMessages([
        ...newMessages,
        { sender: "bot", text: "Error: Unable to fetch response." },
      ]);
    }
  };

  return (
    <div className="w-full max-w-md mx-auto bg-gray-100 p-4 rounded-lg shadow-md">
      <div className="h-64 overflow-y-auto p-2 bg-white rounded">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={`my-2 p-2 rounded ${
              msg.sender === "user"
                ? "bg-blue-500 text-white ml-auto"
                : "bg-gray-300 text-black mr-auto"
            } max-w-xs`}
          >
            {msg.text}
          </div>
        ))}
      </div>

      <div className="flex items-center mt-4">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="flex-1 p-2 border border-gray-300 rounded-l"
          placeholder="Type a message..."
        />
        <button
          onClick={sendMessage}
          className="bg-blue-500 text-white px-4 py-2 rounded-r"
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default Chatbot;
