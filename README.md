# LLMOps-Architecture

This project demonstrates a modern MLOps architecture tailored for LLMOps (Large Language Model Operations) using Google Gemini, LangChain, FastAPI, and modular agentic design. It provides a reference implementation for building, deploying, and operating LLM-powered applications with production best practices.

## Features

- **Agentic Orchestration**: Modular agent and tool design using LangChain and custom Python tools.
- **API-First**: FastAPI-based REST API for LLM-powered chat and tool invocation.
- **Configurable**: Environment-based configuration using Pydantic and `.env` files.
- **Extensible Tools**: Easily add new tools for LLMs to use (e.g., calculator, search, etc.).
- **Production Ready**: Structured logging, health checks, and test coverage.

## Architecture Overview

```
User ──▶ FastAPI REST API ──▶ Orchestrator Agent ──▶ LLM (Google Gemini) ──▶ Tools (Python functions)
```

- **API Layer**: Exposes endpoints for chat and health checks.
- **Agent Layer**: Orchestrates LLM calls and tool selection.
- **Tool Layer**: Implements Python functions (e.g., calculator) that the LLM can invoke.
- **Config Layer**: Manages environment variables and secrets.

## Project Structure

```
src/
  app/
	 api/           # FastAPI endpoints
	 agents/        # Orchestrator logic
	 tools/         # Custom tools for LLM
	 core/          # Configuration and settings
tests/             # API and agent tests
data/              # Data and vector DBs (if needed)
config/            # Configuration files
```

## Quickstart

1. **Install dependencies**
	```bash
	pip install -r requirements.txt
	# or use pyproject.toml with poetry/pip
	```

2. **Set up environment variables**
	- Copy `.env.example` to `.env` and add your `GEMINI_API_KEY` and other settings.

3. **Run the API server**
	```bash
	uvicorn src.app.api.main:app --reload
	```

4. **Test the API**
	- Health check: `GET /health`
	- Chat: `POST /chat` with `{ "message": "What is 10 times 10?" }`

## Example Tool: Calculator

The LLM can invoke Python tools, such as a calculator:

```python
@tool
def multiply(a: int, b: int) -> int:
	 """Multiply two integers together."""
	 return a * b
```

## Extending the Project

- Add new tools in `src/app/tools/` and register them in the orchestrator.
- Add new API endpoints in `src/app/api/main.py`.
- Update configuration in `src/app/core/config.py`.

## Testing

Run tests with:
```bash
pytest
```

## Dependencies

- FastAPI
- LangChain
- Google Gemini (via `langchain-google-genai`)
- Pydantic
- Uvicorn

