from fastapi import FastAPI
from app.api.v1.rag import router as rag_router

app = FastAPI(
    title="KCI Academic RAG Assistant API",
    description="KCI Open API와 로컬 Llama 3.1을 연동한 학술 연구 보조 RAG 백엔드",
    version="1.0.0"
)

app.include_router(rag_router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "KCI RAG Backend"}