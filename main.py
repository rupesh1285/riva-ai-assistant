import os
from dotenv import load_dotenv
from models import get_reply, get_current_model
from persona import load_persona

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("API key not found.")
    exit()

prompt = load_persona()
history = []

while True:
    user_input = input("You: ").strip()

    if user_input == "/quit":
        break
    elif user_input == "/help":
        print("Please select the command:")
        print(
            "/clear —  To wipe history to start a fresh conversation without restarting Riva"
        )
        print("/model —  To show which model is currently active")
        print("/history — To show the number of messages stored in memory")
        print("/persona — To show the Defined Behaviour of Agent")
        print("/quit — To exit the chat")
        continue
    elif user_input == "/clear":
        history.clear()
        continue
    elif user_input == "/model":
        model = get_current_model()
        print(model)
        continue
    elif user_input == "/history":
        print(len(history))
        continue
    elif user_input == "/persona":
        print(prompt)
        continue
    history.append({"role": "user", "parts": [{"text": user_input}]})
    reply = get_reply(history, prompt, api_key)

    if reply is None:
        history.pop()
        continue

    print("Riva:", reply)
    history.append({"role": "model", "parts": [{"text": reply}]})
