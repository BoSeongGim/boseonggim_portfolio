import streamlit as st
import requests

st.set_page_config(
    page_title="KCI 학술 논문 RAG 연구 비서",
    page_icon="📚",
    layout="wide"
)

st.title("📚 KCI Open API 기반 로컬 RAG 연구 비서")
st.caption("Local Llama 3.1 8B (LM Studio) & HuggingFace Multilingual Embedding")

# 사이드바: 검색 및 RAG 파라미터 제어
with st.sidebar:
    st.header("⚙️ 검색 및 모델 설정")
    keyword = st.text_input("KCI 논문 검색 키워드", value="인공지능")
    display_count = st.slider("수집 논문 수", min_value=1, max_value=15, value=5)
    top_k = st.slider("참고할 유사 논문 수 (Top-K)", min_value=1, max_value=5, value=2)
    api_url = st.text_input("FastAPI 엔드포인트", value="http://127.0.0.1:8000/api/v1/rag/query")

# 메인 질의 입력 영역
st.subheader("💡 연구 질문 입력")
question = st.text_area(
    "수집된 논문을 바탕으로 질의할 내용을 입력하세요",
    value="수집된 논문의 주요 연구 주제와 핵심 결론을 요약해줘.",
    height=100
)

if st.button("🚀 RAG 분석 및 답변 생성", type="primary"):
    payload = {
        "keyword": keyword,
        "display_count": display_count,
        "question": question,
        "top_k": top_k
    }

    with st.spinner("KCI 논문 수집 및 로컬 LLM 추론 중..."):
        try:
            response = requests.post(api_url, json=payload, timeout=60)
            if response.status_code == 200:
                data = response.json()

                col1, col2 = st.columns([3, 2])

                # 좌측: 로컬 LLM RAG 답변
                with col1:
                    st.success("✅ 답변 생성 완료")
                    st.markdown("### 🤖 연구 비서 답변")
                    st.write(data["answer"])

                # 우측: 참고한 KCI 논문 메타데이터 카드
                with col2:
                    st.info("📚 참고된 논문 출처")
                    for i, src in enumerate(data.get("source_documents", []), 1):
                        with st.expander(f"[{i}] {src.get('title', '제목 없음')}", expanded=True):
                            st.write(f"**저자:** {src.get('authors', '정보 없음')}")
                            st.write(f"**학회지:** {src.get('journal', '정보 없음')}")
                            st.write(f"**발행년도:** {src.get('year', '정보 없음')}")
            else:
                st.error(f"서버 오류 ({response.status_code}): {response.text}")
        except Exception as e:
            st.error(f"연결 실패: {str(e)}")