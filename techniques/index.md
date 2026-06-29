# 기법 (Techniques)

그래프 구축, 커뮤니티 탐지, 그래프 순회, GNN 등 여러 GraphRAG 시스템이 공유하는 재사용 가능한 구성 요소와 알고리즘.

이 섹션에는 12개의 노트가 있습니다.

- [Community Detection (Leiden)](community-detection.md) — 그래프를 밀접하게 연결된 노드 집합인 커뮤니티로 분할하는 기법으로, Microsoft GraphRAG는 Traag, Waltman, van Eck(2019)이 제안한 Leiden 알고리즘을 사용한다.
- [Community Summarization](community-summarization.md) — 그래프에서 탐지된 계층적 커뮤니티마다 LLM으로 '보고서'를 사전 생성하고, 이 요약들을 맵리듀스로 결합해 전역적 질의에 답하는 GraphRAG의 색인·검색 기술이다.
- [DRIFT Search](drift-search.md) — 전역 검색의 커뮤니티 요약과 국소 검색의 엔터티 중심 탐색을 결합해, 광범위한 개관에서 출발하여 후속 질문으로 세부를 파고드는 Microsoft GraphRAG의 반복적 질의 기법이다.
- [Entity & Relationship Extraction](entity-relationship-extraction.md) — 텍스트 청크에서 LLM 프롬프트로 유형이 부여된 개체와 그 사이의 관계(및 주장)를 추출하여 지식 그래프의 트리플을 만드는 기법이며, 회수율을 높이기 위해 글리닝/다중 라운드 추출을 사용한다.
- [Graph Neural Network (GNN)](graph-neural-network.md) — 그래프 구조 위에서 이웃 노드의 정보를 반복적으로 집계해 노드·엣지·부분그래프의 표현을 학습하는 신경망 계열로, GraphRAG에서는 부분그래프 인코딩과 노드 랭킹/검색에 활용된다.
- [Graph Traversal Reasoning](graph-traversal-reasoning.md) — LLM을 에이전트로 삼아 지식 그래프의 관계 경로를 반복적으로 탐색하거나 미리 계획해 따라가면서, 그 경로에 모인 근거로 멀티홉 질문에 답하는 GraphRAG 추론 기법이다.
- [Hierarchical Clustering](hierarchical-clustering.md) — 청크나 그래프 노드를 재귀적으로 군집화·요약해 여러 추상화 수준을 갖는 트리(RAPTOR)나 계층적 커뮤니티(GraphRAG)를 구성하는 색인 기법이다.
- [Hybrid Retrieval](hybrid-retrieval.md) — 벡터(밀집) 검색, 키워드(희소) 검색, 그래프 탐색 등 서로 다른 검색 신호를 결합해 재현율과 정밀도를 함께 끌어올리는 검색 기법이다.
- [Knowledge Graph Construction](knowledge-graph-construction.md) — LLM으로 비정형 텍스트에서 개체와 관계를 추출해 노드·엣지로 연결된 KG 색인을 만드는 과정으로, GraphRAG의 인덱싱 단계에 해당한다.
- [Local vs Global Search](local-and-global-search.md) — Microsoft GraphRAG의 두 가지 질의 모드로, 지역(local) 검색은 특정 엔터티 주변의 이웃과 근거를 모아 답하고, 전역(global) 검색은 커뮤니티 보고서를 맵리듀스로 결합해 말뭉치 전반을 아우르는 질문에 답한다.
- [Personalized PageRank](personalized-pagerank.md) — 시드 노드 집합에서 출발하는 랜덤 워크의 정상 분포로 그래프 노드를 랭킹하는 PageRank 변형으로, HippoRAG 등 GraphRAG 기법에서 질의에 정박한 시드로부터 구절·노드를 점수화하는 데 쓰인다.
- [Subgraph Extraction](subgraph-extraction.md) — 질의와 관련된 부분그래프(에고그래프)를 그래프에서 선택해 LLM에 제공하는 GraphRAG 검색 기법으로, G-Retriever의 PCST 최적화나 SubgraphRAG의 트리플 점수화처럼 큰 그래프를 컨텍스트에 맞는 크기로 추리는 데 쓰인다.

---

[← 위키 홈](../index.md)
