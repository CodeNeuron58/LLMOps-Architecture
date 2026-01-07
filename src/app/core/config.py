from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    # App Info
    APP_NAME: str = "GenAI Agent"
    ENV: str = "dev"

    # LLM Credentials
    GEMINI_API_KEY: str  # Required!
    MODEL_NAME: str = "gemini-3-flash-preview"

    # This tells Pydantic to read from a .env file
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

@lru_cache
def get_settings():
    settings = Settings()
    if not settings.GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY is not set in the environment or .env file.")
    return settings