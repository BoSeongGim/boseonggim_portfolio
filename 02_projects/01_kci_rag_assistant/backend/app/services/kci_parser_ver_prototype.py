# backend/app/services/kci_parser.py
import xml.etree.ElementTree as ET
from typing import List
import httpx
from langchain_core.documents import Document

class KCIParser:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://open.kci.go.kr/po/openapi/openApiSearch.kci"

    async def search_to_documents(self, keyword: str, display_count: int = 10) -> List[Document]:
        """KCI API를 호출하여 XML 응답을 LangChain Document 리스트로 변환합니다."""
        params = {
            "apiCode": "articleSearch", #[cite: 2]
            "key": self.api_key,        #[cite: 2]
            "title": keyword,           #[cite: 2]
            "displayCount": display_count #[cite: 2]
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(self.base_url, params=params)
            response.raise_for_status()
            
        # XML 파싱 시작 (KCI 응답 규격 반영)
        root = ET.fromstring(response.content)
        documents = []

        # <record> 엘리먼트 순회
        for record in root.findall(".//record"): #[cite: 2]
            # 1. 논문 제목 추출
            title_element = record.find(".//article-title") #[cite: 2]
            title = title_element.text if title_element is not None else "Unknown Title"

            # 2. 초록(Abstract) 추출 -> Page Content로 활용
            abstract_element = record.find(".//abstract") #[cite: 2]
            abstract = abstract_element.text if abstract_element is not None else ""

            # 3. 메타데이터 추출 -> Vector DB 필터링 및 RAG 출처 표기용
            journal_name = record.find(".//journal-name").text if record.find(".//journal-name") is not None else "" #[cite: 2]
            pub_year = record.find(".//pub-year").text if record.find(".//pub-year") is not None else "" #[cite: 2]
            
            authors = []
            for author in record.findall(".//author"): #[cite: 2]
                if author.text:
                    authors.append(author.text.strip())
            
            # LangChain 표준 Document 객체 생성
            doc = Document(
                page_content=abstract,  # LLM이 참고할 실질적인 지식 텍스트
                metadata={
                    "title": title,
                    "authors": ", ".join(authors),
                    "journal": journal_name,
                    "year": pub_year,
                    "source": "KCI"
                }
            )
            documents.append(doc)

        return documents

# 로컬 독립 테스트용 코드 (main)
if __name__ == "__main__":
    import asyncio

    async def test():
        # 발급받으신 인증키 입력
        API_KEY = "90862859" #[cite: 2]
        parser = KCIParser(api_key=API_KEY)
        
        print("KCI Open API 검색 테스트 시작...")
        docs = await parser.search_to_documents(keyword="인공지능", display_count=2)
        
        for i, doc in enumerate(docs):
            print(f"\n--- Document {i+1} ---")
            print(f"Title: {doc.metadata['title']}")
            print(f"Authors: {doc.metadata['authors']}")
            print(f"Content Snippet: {doc.page_content[:100]}...")

    asyncio.run(test())