boseonggim\_portfolio/

├── projects/

│   └── kci-rag-system/

│       ├── README.md               # 아키텍처 다이어그램 및 기술 트레이드오프 문서

│       ├── frontend/               # React 또는 Flutter 소스 코드 (보안 위험 없음)

│       └── backend/

│           ├── main.py             # FastAPI 엔드포인트 정의

│           ├── schemas/            # Pydantic 기반 요청/응답 규격

│           └── core/

│               ├── base\_rag.py     # LangChain 추상 베이스 클래스 (ABC)

│               └── mock\_service.py # API 키 없이 작동 가능한 모의 구동 서비스

