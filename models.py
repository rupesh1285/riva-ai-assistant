import requests
import time

MODELS = [
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
    "gemini-2.0-flash",
    "gemini-2.0-flash-lite",
]
current_idx = 0
last_switch_time = 0
COOLDOWN_SECONDS = 300


def get_reply(history, prompt, api_key):
    global current_idx, last_switch_time

    headers = {"Content-Type": "application/json", "x-goog-api-key": api_key}
    data = {
        "system_instruction": {"parts": [{"text": prompt}]},
        "contents": history,
    }

    if current_idx > 0 and time.time() - last_switch_time >= COOLDOWN_SECONDS:
        current_idx = 0
        print("Cooldown finished. Retrying primary model...")

    while current_idx < len(MODELS):
        model = MODELS[current_idx]
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            result = response.json()
            return result["candidates"][0]["content"]["parts"][0]["text"]
        elif response.status_code == 429:
            print(f"{model} limit hit! Switching to the next model...")
            current_idx += 1
            last_switch_time = time.time()
        else:
            print("Error:", response.status_code, response.text)
            return None

    print("All models exhausted for today!")
    return None


def get_current_model():
    if current_idx < len(MODELS):
        return MODELS[current_idx]
    return "None (all models exhausted)"
