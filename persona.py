import json


def load_persona(filepath="personas/riva.json"):
    with open(filepath, "r", encoding="utf-8") as f:
        persona = json.load(f)

    prompt = f"""
Name: {persona['name']}
Gender: {persona['gender']}
Owner: {persona['owner']}
Role: {persona['role']}
Behavior: {persona['behavior']}
System_prompt: {persona['system_prompt']}
"""
    return prompt
