from typing import List, Optional
from pydantic import BaseModel, Field

class RAGQueryRequest(BaseModel):
    keyword: str = Field(..., description="KCI 논문 검색 키워드", example="인공지능")
    display_count: int = Field(default=5, ge=1, le=20, description="수집할 논문 개수")
    question: str = Field(..., description="LLM에게 질의할 내용", example="수집된 논문의 핵심 내용을 요약해줘")
    top_k: int = Field(default=2, ge=1, le=5, description="참고할 상위 문서 개수")

class SourceDocument(BaseModel):
    title: Optional[str] = None
    authors: Optional[str] = None
    journal: Optional[str] = None
    year: Optional[str] = None
    source: Optional[str] = None

class RAGQueryResponse(BaseModel):
    query: str
    answer: str
    source_documents: List[SourceDocument]