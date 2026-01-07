from fastapi import FastAPI
from pydantic import BaseModel
from src.app.core.config import get_settings
from src.app.agents.orchestrator import run_agent

app = FastAPI(title="GenAI Agentic API")
settings = get_settings()

# We define a "Schema" for the request body
class ChatRequest(BaseModel):
    message: str
    
@app.get("/health")
def health_check():
    return {
        "status": "online",
        # "app_name": settings.APP_NAME,
        # "mode": settings.ENV
    }
    
@app.post("/chat")
async def chat(request: ChatRequest):
    # We call our orchestrator here
    response = run_agent(request.message)
    return {"reply": response}