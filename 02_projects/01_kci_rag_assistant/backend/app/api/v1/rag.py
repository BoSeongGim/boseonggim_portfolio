from fastapi import APIRouter, HTTPException, status
from app.schemas.rag import RAGQueryRequest, RAGQueryResponse
from app.services.kci_parser import KCIParser
from app.services.vector_store import LocalVectorStore
from app.core.rag_chain import KCIRAGChain

router = APIRouter(prefix="/rag", tags=["KCI RAG Service"])

@router.post("/query", response_model=RAGQueryResponse, status_code=status.HTTP_200_OK)
async def query_kci_rag(request: RAGQueryRequest):
    """KCI 논문 수집 -> 로컬 임베딩 -> 로컬 LLM 추론을 원스톱으로 수행하는 API입니다."""
    try:
        # 1. KCI 논문 수집
        parser = KCIParser()
        docs = await parser.search_to_documents(
            keyword=request.keyword,
            display_count=request.display_count
        )
        if not docs:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"'{request.keyword}' 키워드에 대한 논문 검색 결과가 없습니다."
            )

        # 2. 로컬 Vector DB 생성 및 적재
        vector_store = LocalVectorStore(collection_name="fastapi_kci_rag")
        vector_store.create_and_populate(docs)

        # 3. 로컬 LLM RAG 추론
        rag_chain = KCIRAGChain(vector_store=vector_store)
        result = rag_chain.answer_query(
            query=request.question,
            top_k=request.top_k
        )

        return result

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"RAG 파이프라인 처리 중 오류 발생: {str(e)}"
        )