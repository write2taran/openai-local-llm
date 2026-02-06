import requests

OLLAMA_CHAT_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "dolphin-mistral"


def chat(messages):
    """
    messages: list of dicts like OpenAI format
    returns: assistant text response
    """

    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "stream": False
    }

    response = requests.post(OLLAMA_CHAT_URL, json=payload, timeout=300)
    response.raise_for_status()

    data = response.json()
    return data["message"]["content"]

