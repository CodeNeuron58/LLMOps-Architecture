from fastapi import FastAPI
from src.app.core.config import get_settings

app = FastAPI(title="GenAI Agentic API")
settings = get_settings()

@app.get("/health")
def health_check():
    return {
        "status": "online",
        "app_name": settings.APP_NAME,
        "mode": settings.ENV
    }