from typing import List
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

class LocalVectorStore:
    def __init__(self, collection_name: str = "kci_academic_papers"):
        self.collection_name = collection_name
        # 다국어/한국어 성능이 우수한 경량 로컬 임베딩 모델 (CPU/GPU 자동 할당)
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        )
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=300,
            chunk_overlap=50
        )
        self.vector_db = None

    def create_and_populate(self, documents: List[Document]) -> Chroma:
        """KCI Document 리스트를 청킹하고 벡터화하여 로컬 Chroma DB에 적재합니다."""
        if not documents:
            raise ValueError("적재할 Document 리스트가 비어 있습니다.")

        # 텍스트 청킹 (학술 초록 단위 최적화)
        split_docs = self.text_splitter.split_documents(documents)

        # Chroma 인메모리/로컬 벡터 저장소 생성
        self.vector_db = Chroma.from_documents(
            documents=split_docs,
            embedding=self.embeddings,
            collection_name=self.collection_name
        )
        return self.vector_db

    def similarity_search(self, query: str, k: int = 3) -> List[Document]:
        """쿼리와 가장 유사한 상위 k개의 문서를 검색합니다."""
        if self.vector_db is None:
            raise RuntimeError("Vector Store가 초기화되지 않았습니다. create_and_populate를 먼저 호출하세요.")
        return self.vector_db.similarity_search(query, k=k)