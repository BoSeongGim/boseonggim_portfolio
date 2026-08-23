# 🚀 KCI Open API-Based Local LLM & RAG Research Assistant System

This repository provides a hybrid RAG (Retrieval-Augmented Generation) pipeline environment integrating the KCI (Korea Citation Index) Open API with local AI inference infrastructure.
It maintains strict API key security and decoupled architecture while providing a full-stack research assistant powered by a local Llama 3.1 8B model.

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python 3.10+, FastAPI, LangChain
- **Vector DB**: ChromaDB (Local In-Memory / Persistent Vector Store)
- **Embedding**: HuggingFace (`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`)
- **Inference**: Local LLM (Llama 3.1 8B via LM Studio REST API)

## 📐 System Architecture

```mermaid
graph TD
    A[KCI Open API] -->|Ingestion| B[FastAPI Backend]
    B -->|Text Splitting| C[LangChain Pipeline]
    C -->|Vector Embedding| D[(Local Chroma DB)]
    
    E[Streamlit Dashboard] -->|User Query| B
    D -->|Context Retrieval| B
    B -->|Prompt Binding| F[LM Studio / Llama 3.1 8B]
    F -->|Inference Answer| E

    style D fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#ffffff
```

## 📂 Project Directory Structure

```text
├── backend/
│   ├── app/
│   │   ├── api/v1/       # FastAPI router endpoints (/api/v1/rag/query)
│   │   ├── core/         # RAG chain pipeline & configuration
│   │   ├── schemas/      # Pydantic request/response schemas
│   │   ├── services/     # KCI API Client & Vector DB management
│   │   └── main.py       # FastAPI application entrypoint
│   ├── tests/            # pytest unit and integration test suite
│   ├── run_e2e_rag.py    # Standalone E2E verification script
│   └── requirements.txt
├── frontend/
│   └── app.py            # Streamlit interactive UI dashboard
├── docs/                 # AI orchestration and audit log documentation
└── scripts/
    └── sync_to_public.ps1 # Public portfolio code sanitization script
```

## ⚙️ Quick Start (Local Execution)

### 1. Prerequisites (Launch LM Studio Local Server)
* Launch LM Studio and load the **Llama 3.1 8B (Q8_0)** model.
* Navigate to the **Developer (↔)** tab and start the `Local Server` (Default port: `1234`).

![Streamlit Dashboard UI](docs/images/1. Prerequisites (Launch LM Studio Local Server).png)

### 2. Virtual Environment Setup & Dependencies
```powershell
cd backend
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 3. Verification Suite (Micro V-Model Unit Tests)
```powershell
python -m pytest tests/ -v
```

### 4. Application Launch

* **Terminal 1 (FastAPI Backend):**
  ```powershell
  fastapi dev app/main.py
  ```
  *(Interactive API Docs: `http://127.0.0.1:8000/docs`)*

* **Terminal 2 (Streamlit Frontend):**
  ```powershell
  streamlit run ../frontend/app.py
  ```
  *(Web Dashboard: `http://localhost:8501`)*
