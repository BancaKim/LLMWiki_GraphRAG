# 방법론 (Methods)

Microsoft GraphRAG부터 경량·KG 추론 계열까지, 구체적인 GraphRAG 시스템과 이를 제안한 논문.

이 섹션에는 18개의 노트가 있습니다.

- [G-Retriever](g-retriever.md) — 텍스트 속성을 가진 그래프에 대한 질의응답을 위해 GNN, LLM, RAG를 결합한 기법으로, Prize-Collecting Steiner Tree로 관련 부분그래프를 검색하고 소프트 프롬프팅으로 LLM에 주입한다.
- [GNN-RAG](gnn-rag.md) — GNN(그래프 신경망)을 지식 그래프 위의 검색기로, LLM을 답변 생성기로 결합한 KGQA 기법으로, GNN이 질문 개체에서 후보 답변으로 이어지는 추론 경로를 뽑아 LLM에게 전달한다.
- [GRAG](grag.md) — 개별 문서 대신 텍스트 부분그래프(subgraph)를 검색하고 그 위상 정보를 LLM 생성에 통합하는 그래프 기반 RAG 기법(Hu et al., 2024).
- [GraphReader](graphreader.md) — 긴 텍스트를 key element와 atomic fact로 이루어진 그래프로 구조화한 뒤, LLM 에이전트가 이 그래프를 자율적으로 탐색하며 멀티홉 질문에 답하도록 하는 graph 기반 장문 처리 기법이다.
- [HippoRAG](hipporag.md) — 인간 장기 기억의 해마 색인 이론에서 착안한 GraphRAG 기법으로, 코퍼스로부터 지식 그래프를 구축하고 Personalized PageRank를 실행해 여러 문서에 흩어진 근거를 단일 검색 단계로 모은다.
- [HippoRAG 2](hipporag-2.md) — HippoRAG를 확장하여 패시지를 지식 그래프에 더 깊이 통합하고 밀집 검색으로 시드를 부여한 Personalized PageRank를 사용함으로써, 사실·의미파악·연상 기억 과제 전반에서 인간의 장기 기억에 더 가깝게 접근하려는 GraphRAG 기반 검색 증강 생성 방법이다.
- [KAPING](kaping.md) — 질문에서 추출한 개체 주변의 지식 그래프 트리플을 의미 유사도로 골라 프롬프트에 덧붙임으로써, 별도 학습 없이 LLM의 영샷 지식 그래프 질의응답 성능을 끌어올리는 프레임워크다.
- [Knowledge Graph Prompting (KGP)](kgp.md) — 여러 문서 위에 지식 그래프를 구성하고 LM 기반 그래프 탐색기로 근거 문단을 모아 LLM의 다중 문서 질의응답(MD-QA)을 돕는 그래프 기반 프롬프팅 기법(Wang et al., 2024).
- [LazyGraphRAG](lazygraphrag.md) — LLM 기반 사전 요약을 색인 단계에서 생략하고 NLP 명사구 추출로 가벼운 그래프 색인을 만든 뒤, 질의 시점에 LLM 요약과 관련성 평가를 지연 수행하여 vector RAG 수준의 색인 비용으로 국소·전역 질의를 처리하는 그래프 기반 RAG 기법.
- [LightRAG](lightrag.md) — 코퍼스에서 구축한 KG 인덱싱과 이중 수준(저수준·고수준) 검색을 결합하고 증분 그래프 갱신을 지원하는 그래프 기반 RAG 방법.
- [MedGraphRAG](medgraphrag.md) — 의료 도메인을 위한 GraphRAG 프레임워크로, 삼중 그래프 구성(Triple Graph Construction)과 U-retrieval을 통해 LLM이 근거 기반의 안전한 의료 응답을 생성하도록 돕는다.
- [Microsoft GraphRAG](microsoft-graphrag.md) — 텍스트 말뭉치에서 LLM으로 엔터티 지식 그래프를 구축하고 커뮤니티 단위로 사전 요약하여, 전역적 sensemaking 질의를 query-focused summarization 방식으로 답하는 그래프 기반 RAG 기법.
- [RAPTOR](raptor.md) — 텍스트 청크를 재귀적으로 임베딩·클러스터링·요약하여 상향식 트리를 구축하고, 추론 시 서로 다른 추상화 수준에서 정보를 검색하는 트리 기반 검색 기법이다.
- [Reasoning on Graphs (RoG)](reasoning-on-graphs.md) — RoG는 LLM과 지식 그래프를 결합해 관계 경로를 계획으로 생성하고 이를 따라 추론 경로를 검색·추론함으로써 충실하고 해석 가능한 추론을 수행하는 KGQA 방법이다.
- [StructGPT](structgpt.md) — 전용 인터페이스로 구조화 데이터에서 근거를 모으고 LLM이 그 위에서 추론하도록 분리한, 반복적 읽기-추론(IRR) 기반의 범용 구조화 데이터 추론 프레임워크다.
- [SubgraphRAG](subgraphrag.md) — 경량 MLP 검색기와 방향성 거리 인코딩(DDE)으로 지식 그래프에서 유연한 크기의 부분그래프를 검색하고, 이를 LLM에 제공해 추론·답변하게 하는 KG 기반 RAG 방법이다.
- [Think-on-Graph (ToG)](think-on-graph.md) — LLM을 에이전트로 삼아 지식 그래프 위에서 빔 서치로 추론 경로를 반복 탐색하고, 검색한 지식에 근거해 답을 도출하는 학습이 필요 없는 LLM-KG 통합 추론 기법이다.
- [Think-on-Graph 2.0](think-on-graph-2.md) — 지식 그래프로 문서를 개체 단위로 연결하고 문서를 개체의 맥락으로 활용하여, 구조화된 지식과 비구조화된 텍스트를 긴밀히 결합한 채 반복적으로 검색하는 하이브리드 GraphRAG 추론 프레임워크다.

---

[← 위키 홈](../index.md)
