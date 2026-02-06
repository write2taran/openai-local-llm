from ollama_wrapper import chat

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Explain what an LLM is in one paragraph."}
]

response = chat(messages)
print(response)
