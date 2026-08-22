import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    KCI_API_KEY: str = os.getenv("KCI_API_KEY", "")
    KCI_BASE_URL: str = "https://open.kci.go.kr/po/openapi/openApiSearch.kci"

    class Config:
        case_sensitive = True

settings = Settings()