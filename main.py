import os
from dotenv import load_dotenv
from models import get_reply
from persona import load_persona

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("API key not found.")
    exit()

prompt = load_persona()
history = []

while True:
    user_input = input("You: ")

    if user_input == "/quit":
        break
    elif user_input == "/help":
        print("Please select the command:")
        continue
    elif user_input == "/help":
        print("")
    history.append({"role": "user", "parts": [{"text": user_input}]})
    reply = get_reply(history, prompt, api_key)

    if reply is None:
        history.pop()
        continue

    print("Riva:", reply)
    history.append({"role": "model", "parts": [{"text": reply}]})
