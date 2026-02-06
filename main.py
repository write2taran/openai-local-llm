from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from ollama_wrapper import chat
import time
import uuid

app = FastAPI()


# --------- OpenAI-style request models ---------

class Message(BaseModel):
    role: str
    content: str


class ChatCompletionRequest(BaseModel):
    model: str
    messages: List[Message]


# --------- Endpoint ---------

@app.post("/v1/chat/completions")
async def chat_completions(body: ChatCompletionRequest):
    start_time = time.time()

    output = chat([m.dict() for m in body.messages])
    elapsed = time.time() - start_time

    return {
        "id": f"chatcmpl-{uuid.uuid4().hex}",
        "object": "chat.completion",
        "created": int(time.time()),
        "model": body.model,
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": output
                },
                "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0
        },
        "local_inference_time_sec": round(elapsed, 2)
    }
