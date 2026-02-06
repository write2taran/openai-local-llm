# openai-local-llm

Local OpenAI-compatible API gateway powered by Ollama, enabling drop-in replacement of cloud LLMs with on-device inference.

---

## Overview

`openai-local-llm` provides a **local, OpenAI-compatible HTTP API** for chat completions backed by **Ollama**.

It allows applications that already depend on OpenAI’s API to switch to **local, private LLM inference** with minimal or zero changes to application code.

This project focuses on **API compatibility and backend infrastructure**, not UI or prompt demos.

---

## Why This Project Exists

Many developers and teams want to:

- Reduce dependency on cloud-based LLM APIs
- Avoid recurring API costs
- Keep sensitive data on-device
- Experiment with local or on-prem LLMs
- Maintain compatibility with existing OpenAI-based codebases

This project addresses those needs by exposing a **stable OpenAI-style interface** over locally running models.

---

## What This Project Provides

- An OpenAI-compatible `/v1/chat/completions` endpoint
- Local inference via Ollama
- Drop-in compatibility with existing OpenAI SDKs
- Clean separation between API layer and inference runtime
- A lightweight backend suitable for local or internal deployments

This is **infrastructure**, not a chatbot application.

---

## Intended Audience

- Backend and platform engineers
- Developers currently using OpenAI APIs
- Teams exploring private or offline LLM inference
- Engineers learning how to wrap LLM runtimes behind stable APIs

---

## High-Level Architecture

```text
Client (OpenAI SDK / HTTP)
        |
        v
openai-local-llm API
(FastAPI, Python 3.11)
        |
        v
Ollama Runtime
(Local LLM Models)
```

Clients never interact with Ollama directly.  
All communication flows through the OpenAI-compatible API layer.

---

## Requirements

### System Requirements

- Windows, Linux, or macOS
- Python **3.11.x**
- Ollama installed and running

### Optional (Recommended)

- NVIDIA GPU for faster inference
- 16 GB system RAM for smooth use with 7B models

---

## Installing Dependencies

Install all required Python dependencies using:

```bash
py -3.11 -m pip install -r requirements.txt
```

This ensures all packages are installed explicitly for **Python 3.11**.

---

## Ollama Setup

Before running the API, ensure Ollama is installed and running.

1. Install Ollama from:  
   https://ollama.com

2. Start Ollama (tray icon should be visible on Windows).

3. Pull at least one model, for example:
   - `dolphin-mistral`
   - or any other supported Ollama model

Ollama handles:
- model loading
- GPU / CPU usage
- quantization
- inference execution

This project does **not** reimplement inference logic.

---

## Running the Service

- The API runs on **port 8000** by default
- Base URL:
  ```
  http://127.0.0.1:8000
  ```

Port `8000` is used because it is the standard FastAPI/Uvicorn default and avoids common conflicts.

A Swagger UI is available at:
```
http://127.0.0.1:8000/docs
```

> The Swagger UI is intended for debugging and inspection only.  
> Real usage is programmatic.

---

## How the API Is Used

Once running, the service can be used in three primary ways:

### 1. OpenAI SDK Compatibility
Existing OpenAI client libraries can be pointed to this service by changing the API base URL.

### 2. Direct HTTP Integration
Any language capable of making HTTP requests can call the API directly.

### 3. Zero-Code-Change Mode
Many applications only require environment variable changes to switch from OpenAI to local inference.

The API responds using the same structural conventions as OpenAI’s chat completions endpoint.

---

## Model Selection & Hardware Guidance

Model execution is entirely handled by **Ollama**.  
Switching models does not require changes to the API layer.

### If You Have Moderate or Strong Hardware

- 7B models provide a good balance of quality and performance
- Suitable for development and internal tools

### If You Have Limited Hardware

Consider smaller or more efficient models, such as:

- `phi`
- `tinyllama`
- `qwen2.5:3b`
- lower-precision or smaller quantized variants

These models:

- Require less VRAM
- Load faster
- Run well on CPUs or low-end GPUs
- Are ideal for laptops and entry-level systems

---

## Design Philosophy

- Prioritize compatibility over novelty
- Keep the API surface minimal and stable
- Avoid unnecessary abstraction layers
- Treat inference runtime as replaceable
- Optimize for clarity and inspectability

This project intentionally avoids UI layers, agents, or orchestration frameworks.

---

## Limitations

- Single-node, local deployment
- No authentication or rate limiting by default
- Token usage reporting is approximate
- Performance depends on the selected Ollama model

---

## License

MIT License
