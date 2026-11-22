import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

with open("personas/riva.json", "r", encoding="utf-8") as f:
    persona = json.load(f)


prompt = f"""
Name: {persona['name']}
Gender: {persona['gender']}
Owner: {persona['owner']}
Role: {persona['role']}
Behaviour: {persona['behavior']}
System_prompt: {persona['system_prompt']}
"""

url = ""
api_key = os.getenv("GEMINI_API_KEY")
headers = {"Content-Type": "application/json", "x-goog-api-key": api_key}

if not api_key:
    print("API not present")
    exit()

history = []

models = ["gemini-2.5-flash", "gemini-2.5-flash-lite", "gemini-2.0-flash"]

while True:
    user_input = input("You: ")

    if user_input == "/quit":
        break
    else:
        for model in models:
            url = f"[https://generativelanguage.googleapis.com/v1beta/models/](https://generativelanguage.googleapis.com/v1beta/models/){model}:generateContent"

        history.append({"role": "user", "parts": [{"text": user_input}]})
        data = {
            "system_instruction": {"parts": [{"text": prompt}]},
            "contents": history,
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code != 200:
            print("Status Code: ", response.status_code, response.text)
            history.pop()
            continue
        result = response.json()
        reply = result["candidates"][0]["content"]["parts"][0]["text"]
        print("Riva:", reply)
        history.append({"role": "model", "parts": [{"text": reply}]})
