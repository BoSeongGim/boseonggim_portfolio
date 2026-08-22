import xml.etree.ElementTree as ET
from typing import List, Optional
import httpx
from langchain_core.documents import Document
from app.core.config import settings

class KCIParser:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or settings.KCI_API_KEY
        self.base_url = settings.KCI_BASE_URL

    def parse_xml_to_documents(self, xml_content: bytes) -> List[Document]:
        """XML 바이트 데이터를 파싱하여 LangChain Document 리스트로 반환합니다 (네트워크 무관)."""
        root = ET.fromstring(xml_content)
        documents = []

        for record in root.findall(".//record"):
            title_element = record.find(".//article-title")
            title = title_element.text if title_element is not None and title_element.text else "Unknown Title"

            abstract_element = record.find(".//abstract")
            abstract = abstract_element.text if abstract_element is not None and abstract_element.text else ""

            journal_name = record.find(".//journal-name").text if record.find(".//journal-name") is not None else ""
            pub_year = record.find(".//pub-year").text if record.find(".//pub-year") is not None else ""
            
            authors = [
                author.text.strip()
                for author in record.findall(".//author")
                if author.text and author.text.strip()
            ]

            doc = Document(
                page_content=abstract,
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

    async def search_to_documents(self, keyword: str, display_count: int = 10) -> List[Document]:
        """KCI API를 비동기 호출하여 검색 결과를 Document 리스트로 변환합니다."""
        if not self.api_key:
            raise ValueError("KCI API Key가 설정되지 않았습니다.")

        params = {
            "apiCode": "articleSearch",
            "key": self.api_key,
            "title": keyword,
            "displayCount": display_count
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(self.base_url, params=params, timeout=10.0)
            response.raise_for_status()

        return self.parse_xml_to_documents(response.content)