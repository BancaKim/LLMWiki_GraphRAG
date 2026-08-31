# 개념 (Concepts)

검색 증강 생성, 임베딩, 지식 그래프, 그래프 기반 추론의 토대가 되는 핵심 개념.

이 섹션에는 13개의 노트가 있습니다.

- [Dense Retrieval / Vector Search](dense-retrieval.md) — 질의와 문서 청크를 동일한 벡터 공간에 임베딩한 뒤 근사 최근접 이웃(ANN) 검색으로 의미적으로 가까운 항목을 찾는 검색 방식으로, Karpukhin et al.(2020)의 DPR이 대표적이며 GraphRAG가 보강하는 기본 RAG 검색기다.
- [GraphRAG (the paradigm)](graph-rag.md) — 평면 벡터 색인 대신 그래프 또는 지식 그래프를 검색 인덱스로 사용하는 RAG 패러다임으로, 인덱싱 단계에서 그래프를 구축하고 질의 단계에서 지역 질문과 전역 질문을 그래프 구조로 답한다.
- [GraphRAG 보안과 지식 포이즈닝](graphrag-security.md) — GraphRAG의 그래프 색인 자체를 표적으로 삼는 지식 포이즈닝 공격과 그 방어 과제를 다루는 2025~2026년 연구 흐름을 정리한 개념 노트다.
- [Hallucination (환각)](hallucination.md) — LLM이 유창하지만 근거가 없거나 사실과 다른 내용을 그럴듯하게 생성하는 현상으로, 검색과 그래프 그라운딩으로 외부 근거를 제공해 완화한다.
- [Knowledge Graph QA (KGQA)](knowledge-graph-question-answering.md) — 지식 그래프(KG)에 담긴 구조화된 사실을 근거로 자연어 질문에 답하는 과제로, ToG·RoG·GNN-RAG 등 다수 그래프 추론 기법이 표준 평가 대상으로 삼는다.
- [Large Language Model (LLM)](large-language-model.md) — 대규모 텍스트로 사전학습된 트랜스포머 기반 생성 모델로, 다음 토큰을 예측하도록 학습되어 자연어를 이해·생성하지만 매개변수에 갇힌 지식과 제한된 컨텍스트 윈도 때문에 외부 지식 보강이 필요하다.
- [Multi-hop Reasoning (멀티홉 추론)](multi-hop-reasoning.md) — 하나의 구절에 답이 담겨 있지 않아 여러 사실과 관계를 단계적으로 연결해야 답할 수 있는 질의 유형으로, 평면 벡터 RAG가 약하고 그래프 구조가 보완하는 대표적 과제이다.
- [Query-Focused Summarization (QFS)](query-focused-summarization.md) — 사용자의 질의에 초점을 맞춰 하나의 문서나 말뭉치 전체를 요약하는 과제로, 특정 구절을 검색하는 대신 코퍼스를 종합해 답하며 Microsoft GraphRAG가 겨냥하는 전역 sensemaking의 핵심 문제 정의이다.
- [Retrieval-Augmented Generation (RAG)](retrieval-augmented-generation.md) — 외부 지식 소스에서 관련 정보를 검색해 LLM의 생성에 근거로 제공하는 패러다임으로, Lewis et al.(2020)이 NeurIPS에서 처음 정식화했으며 GraphRAG의 모태가 된다.
- [Text Chunking (청킹)](text-chunking.md) — 긴 문서를 검색·색인의 기본 단위가 되도록 작은 텍스트 조각으로 분할하는 전처리로, 청크 크기와 중첩의 트레이드오프가 검색 품질을 좌우하며 GraphRAG에서는 청크가 그래프의 노드로 쓰이기도 한다.
- [Text Embedding (텍스트 임베딩)](text-embedding.md) — 단어·문장·구절 등의 텍스트를 의미적 유사성이 거리로 반영되도록 고정 차원의 밀집 벡터로 사상한 표현으로, 유사도 검색과 그래프 노드·개체의 특징 벡터로 쓰인다.
- [온톨로지 기반·뉴로심볼릭 GraphRAG](neurosymbolic-graphrag.md) — LLM이 자유롭게 뽑아낸 그래프 대신 온톨로지·논리 제약 같은 명시적 심볼릭 구조를 검색과 추론에 결합하는 GraphRAG 연구 흐름으로, EMNLP·ICLR 등 주요 학회에 관련 논문이 게재되고 있다.
- [지식 그래프 (Knowledge Graph)](knowledge-graph.md) — 개체(entity)를 노드로, 개체 사이의 관계(relation)를 엣지로 표현하고 사실을 (주어, 술어, 목적어) 트리플로 저장하는 그래프 형태의 구조화된 지식 표현 방식이다.

---

[← 위키 홈](../index.md)
