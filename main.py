import os
import requests
from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
headers = {
    "Content-Type": "application/json", 
    "x-goog-api-key": api_key
}

if not api_key:
    print("API not present")
    exit()

history = []

while True:
    user_input = input("You: ")
        
    if user_input == "/quit":
        break
    else:
        history.append({"role": "user", "parts": [{"text": user_input}]})
        data = {
                "contents": history
            }
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        reply = result["candidates"][0]["content"]["parts"][0]["text"]
        print("Riva:", reply)
        history.append({"role": "model", "parts": [{"text": reply}]})


