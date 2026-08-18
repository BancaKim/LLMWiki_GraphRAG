# 방법론 (Methods)

Microsoft GraphRAG부터 경량·KG 추론 계열까지, 구체적인 GraphRAG 시스템과 이를 제안한 논문.

이 섹션에는 33개의 노트가 있습니다.

- [AGRAG](agrag.md) — LLM 기반 엔터티 추출을 n-gram·TF-IDF 통계 방식으로 대체해 색인 단계의 환각을 없애고, 검색을 최소 비용 최대 영향(MCMI) 부분 그래프 생성 문제로 정식화한 그래프 RAG 기법이다.
- [Deep GraphRAG](deep-graphrag.md) — 전역 검색의 포괄성과 지역 검색의 효율성 사이의 상충을 계층적 global-to-local 3단계 검색으로 절충하고, DW-GRPO 강화학습으로 소형 LLM이 지식 통합을 담당하도록 한 GraphRAG 기법이다.
- [EA-GraphRAG](ea-graphrag.md) — 질의의 구문적 복잡도를 점수화해 단순한 질의는 밀집 RAG로, 복잡한 질의는 그래프 검색으로 보내고 경계 사례는 융합하는 적응적 라우팅 프레임워크다.
- [G-Retriever](g-retriever.md) — 텍스트 속성을 가진 그래프에 대한 질의응답을 위해 GNN, LLM, RAG를 결합한 기법으로, Prize-Collecting Steiner Tree로 관련 부분그래프를 검색하고 소프트 프롬프팅으로 LLM에 주입한다.
- [GFM-RAG](gfm-rag.md) — GFM-RAG는 대규모로 사전학습한 그래프 파운데이션 모델(GFM)을 검색기로 삼아 그래프 인덱스 위에서 질의-지식 관계를 추론하고, 파인튜닝 없이 미지의 데이터셋에 zero-shot으로 적용되는 최초의 GFM 기반 RAG 방법이다.
- [GNN-RAG](gnn-rag.md) — GNN(그래프 신경망)을 지식 그래프 위의 검색기로, LLM을 답변 생성기로 결합한 KGQA 기법으로, GNN이 질문 개체에서 후보 답변으로 이어지는 추론 경로를 뽑아 LLM에게 전달한다.
- [GRAG](grag.md) — 개별 문서 대신 텍스트 부분그래프(subgraph)를 검색하고 그 위상 정보를 LLM 생성에 통합하는 그래프 기반 RAG 기법(Hu et al., 2024).
- [GraphReader](graphreader.md) — 긴 텍스트를 key element와 atomic fact로 이루어진 그래프로 구조화한 뒤, LLM 에이전트가 이 그래프를 자율적으로 탐색하며 멀티홉 질문에 답하도록 하는 graph 기반 장문 처리 기법이다.
- [GraphSearch](graphsearch.md) — GraphSearch는 검색 과정을 6개 모듈로 나눈 에이전틱 심층 검색 워크플로로, 텍스트 청크에는 의미 질의를 구조적 그래프에는 관계 질의를 던지는 이중 채널 전략으로 GraphRAG의 얕은 검색 문제를 완화한다.
- [HippoRAG](hipporag.md) — 인간 장기 기억의 해마 색인 이론에서 착안한 GraphRAG 기법으로, 코퍼스로부터 지식 그래프를 구축하고 Personalized PageRank를 실행해 여러 문서에 흩어진 근거를 단일 검색 단계로 모은다.
- [HippoRAG 2](hipporag-2.md) — HippoRAG를 확장하여 패시지를 지식 그래프에 더 깊이 통합하고 밀집 검색으로 시드를 부여한 Personalized PageRank를 사용함으로써, 사실·의미파악·연상 기억 과제 전반에서 인간의 장기 기억에 더 가깝게 접근하려는 GraphRAG 기반 검색 증강 생성 방법이다.
- [HyperGraphRAG](hypergraphrag.md) — 지식을 하이퍼그래프로 표현해 이진 관계를 넘어 n-항(n-ary) 관계 사실을 하이퍼엣지로 담고, 하이퍼그래프 구축·검색·생성 파이프라인으로 다중 도메인에서 표준 RAG와 그래프 RAG를 능가하는 그래프 기반 RAG 방법.
- [KAG (Knowledge Augmented Generation)](kag.md) — 지식 그래프와 벡터 검색을 결합해 LLM과 KG를 양방향으로 강화하는, 법률·의료·행정 등 전문 도메인 지식 서비스용 프레임워크다.
- [KAPING](kaping.md) — 질문에서 추출한 개체 주변의 지식 그래프 트리플을 의미 유사도로 골라 프롬프트에 덧붙임으로써, 별도 학습 없이 LLM의 영샷 지식 그래프 질의응답 성능을 끌어올리는 프레임워크다.
- [Knowledge Graph Prompting (KGP)](kgp.md) — 여러 문서 위에 지식 그래프를 구성하고 LM 기반 그래프 탐색기로 근거 문단을 모아 LLM의 다중 문서 질의응답(MD-QA)을 돕는 그래프 기반 프롬프팅 기법(Wang et al., 2024).
- [LazyGraphRAG](lazygraphrag.md) — LLM 기반 사전 요약을 색인 단계에서 생략하고 NLP 명사구 추출로 가벼운 그래프 색인을 만든 뒤, 질의 시점에 LLM 요약과 관련성 평가를 지연 수행하여 vector RAG 수준의 색인 비용으로 국소·전역 질의를 처리하는 그래프 기반 RAG 기법.
- [LightRAG](lightrag.md) — 코퍼스에서 구축한 KG 인덱싱과 이중 수준(저수준·고수준) 검색을 결합하고 증분 그래프 갱신을 지원하는 그래프 기반 RAG 방법.
- [LinearRAG](linearrag.md) — 관계 추출을 배제한 계층 그래프 Tri-Graph를 코퍼스 크기에 선형으로 구축해, 대규모 코퍼스에서도 저비용·고신뢰 인덱싱과 정밀한 구절 검색을 제공하는 그래프 기반 RAG 프레임워크.
- [LogicRAG](logicrag.md) — 색인 단계에서 그래프를 미리 구축하지 않고 질의 시점에 하위 문제 간 논리 의존 구조를 동적으로 생성해 그 순서대로 검색과 추론을 수행하는 그래프 기반 RAG의 대안 프레임워크.
- [MedGraphRAG](medgraphrag.md) — 의료 도메인을 위한 GraphRAG 프레임워크로, 삼중 그래프 구성(Triple Graph Construction)과 U-retrieval을 통해 LLM이 근거 기반의 안전한 의료 응답을 생성하도록 돕는다.
- [MemGraphRAG](memgraphrag.md) — 공유 메모리로 전역 컨텍스트를 유지하는 협업 에이전트 사회로 고품질 그래프를 구축하고, 이에 맞춘 메모리 인지 계층적 검색을 수행하는 그래프 기반 RAG 프레임워크.
- [Microsoft GraphRAG](microsoft-graphrag.md) — 텍스트 말뭉치에서 LLM으로 엔터티 지식 그래프를 구축하고 커뮤니티 단위로 사전 요약하여, 전역적 sensemaking 질의를 query-focused summarization 방식으로 답하는 그래프 기반 RAG 기법.
- [MiniRAG](minirag.md) — 텍스트와 엔터티를 하나의 의미 인지 이질 그래프로 통합하고 경량 위상 강화 검색을 써서 소형 언어모델로도 잘 작동하도록 설계된 극도로 단순한 그래프 기반 RAG 방법.
- [NodeRAG](noderag.md) — 엔터티·의미 단위·고수준 요약·이벤트를 서로 다른 유형의 노드로 구분하는 이질적 그래프 구조로 그래프 기반 RAG를 재설계한 그래프 중심 프레임워크.
- [PathRAG](pathrag.md) — 질의 관련 노드들 사이의 핵심 관계 경로에 집중하고 흐름 기반 가지치기로 잡음과 토큰 소비를 줄이는 그래프 기반 RAG 방법.
- [ProgRAG](prograg.md) — 복잡한 질문을 하위 질문으로 분해하고 부분 추론 경로를 점진적으로 확장하면서 불확실성 인지 가지치기로 근거를 정제하는 환각 저항형 멀티홉 KGQA 프레임워크.
- [RAPTOR](raptor.md) — 텍스트 청크를 재귀적으로 임베딩·클러스터링·요약하여 상향식 트리를 구축하고, 추론 시 서로 다른 추상화 수준에서 정보를 검색하는 트리 기반 검색 기법이다.
- [Reasoning on Graphs (RoG)](reasoning-on-graphs.md) — RoG는 LLM과 지식 그래프를 결합해 관계 경로를 계획으로 생성하고 이를 따라 추론 경로를 검색·추론함으로써 충실하고 해석 가능한 추론을 수행하는 KGQA 방법이다.
- [StructGPT](structgpt.md) — 전용 인터페이스로 구조화 데이터에서 근거를 모으고 LLM이 그 위에서 추론하도록 분리한, 반복적 읽기-추론(IRR) 기반의 범용 구조화 데이터 추론 프레임워크다.
- [SubgraphRAG](subgraphrag.md) — 경량 MLP 검색기와 방향성 거리 인코딩(DDE)으로 지식 그래프에서 유연한 크기의 부분그래프를 검색하고, 이를 LLM에 제공해 추론·답변하게 하는 KG 기반 RAG 방법이다.
- [Think-on-Graph (ToG)](think-on-graph.md) — LLM을 에이전트로 삼아 지식 그래프 위에서 빔 서치로 추론 경로를 반복 탐색하고, 검색한 지식에 근거해 답을 도출하는 학습이 필요 없는 LLM-KG 통합 추론 기법이다.
- [Think-on-Graph 2.0](think-on-graph-2.md) — 지식 그래프로 문서를 개체 단위로 연결하고 문서를 개체의 맥락으로 활용하여, 구조화된 지식과 비구조화된 텍스트를 긴밀히 결합한 채 반복적으로 검색하는 하이브리드 GraphRAG 추론 프레임워크다.
- [Youtu-GraphRAG](youtu-graphrag.md) — Youtu-GraphRAG는 그래프 스키마 설계·구축·검색·추론을 공통 스키마를 매개로 하나의 에이전트 체계로 수직 통합하여, 복잡한 다단계 질의에 대한 그래프 검색 증강 추론을 일관되게 수행하는 프레임워크다.

---

[← 위키 홈](../index.md)
