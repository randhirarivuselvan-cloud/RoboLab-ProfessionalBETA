import os
from dotenv import load_dotenv
load_dotenv()

def env(name: str, default: str = "") -> str:
    return os.getenv(name, default)

AI_PROVIDER = env("AI_PROVIDER", "none").lower()
AI_MODEL = env("AI_MODEL")
AI_API_KEY = env("AI_API_KEY")
CORS_ORIGINS = [x.strip() for x in env("CORS_ORIGINS", "http://127.0.0.1:8000,http://localhost:8000").split(",") if x.strip()]
DATABASE_URL = env("DATABASE_URL", "sqlite:///./data/robolab.db")
