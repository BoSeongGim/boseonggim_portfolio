from typing import Dict, Any, List
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document
from app.services.vector_store import LocalVectorStore

class KCIRAGChain:
    def __init__(self, vector_store: LocalVectorStore, base_url: str = "http://localhost:1234/v1"):
        self.vector_store = vector_store
        
        # model 파라미터를 LM Studio 식별자에 맞게 'llama3.1'로 지정
        self.llm = ChatOpenAI(
            base_url=base_url,
            api_key="not-needed",
            temperature=0.2,
            model="llama3.1"
        )
        
        # 학술 RAG 전용 프롬프트 템플릿
        self.prompt = ChatPromptTemplate.from_template(
            """당신은 KCI 학술 논문을 분석하는 전문 AI 연구 비서입니다.
반드시 아래 제공된 [참고 논문 자료]만을 바탕으로 사용자의 질문에 한국어로 정확하게 답변하세요.
답변 끝에는 반드시 참고한 논문의 제목, 저자, 발행연도를 [출처]로 명시하세요.

[참고 논문 자료]
{context}

[사용자 질문]
{question}

[답변]"""
        )
        self.chain = self.prompt | self.llm | StrOutputParser()

    def _format_docs(self, docs: List[Document]) -> str:
        formatted = []
        for i, doc in enumerate(docs, 1):
            title = doc.metadata.get("title", "제목 없음")
            authors = doc.metadata.get("authors", "저자 미상")
            year = doc.metadata.get("year", "연도 미상")
            journal = doc.metadata.get("journal", "")
            formatted.append(
                f"[{i}] 제목: {title} | 저자: {authors} | 학회지: {journal} ({year})\n내용: {doc.page_content}"
            )
        return "\n\n".join(formatted)

    def answer_query(self, query: str, top_k: int = 2) -> Dict[str, Any]:
        """질문을 받아 관련 문서를 검색하고 RAG 답변을 반환합니다."""
        retrieved_docs = self.vector_store.similarity_search(query, k=top_k)
        context_str = self._format_docs(retrieved_docs)
        
        response_text = self.chain.invoke({
            "context": context_str,
            "question": query
        })
        
        return {
            "query": query,
            "answer": response_text,
            "source_documents": [doc.metadata for doc in retrieved_docs]
        }