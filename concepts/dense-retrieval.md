---
type: Concept
title: Dense Retrieval / Vector Search
description: 질의와 문서 청크를 동일한 벡터 공간에 임베딩한 뒤 근사 최근접 이웃(ANN) 검색으로 의미적으로 가까운 항목을 찾는 검색 방식으로, Karpukhin et al.(2020)의 DPR이 대표적이며 GraphRAG가 보강하는 기본 RAG 검색기다.
tags: [dense-retrieval, retrieval, text-embedding, vector-search, foundational]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2004.04906
authors: [Vladimir Karpukhin, Barlas Oğuz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih]
year: 2020
venue: EMNLP 2020
arxiv: "2004.04906"
---

# Dense Retrieval / Vector Search

Dense Retrieval(밀집 검색)는 질의와 문서 청크를 같은 벡터 공간에 임베딩한 뒤, 벡터 간 유사도(보통 내적 또는 코사인)를 기준으로 가장 가까운 항목을 찾는 검색 방식이다. 단어 일치에 의존하는 희소(sparse) 검색과 달리, 표현이 달라도 의미가 비슷하면 가까운 벡터로 매핑되므로 어휘 불일치 문제에 강하다. 대규모 코퍼스에서는 근사 최근접 이웃(ANN) 검색으로 후보를 빠르게 좁힌다. Karpukhin et al.(2020)이 제안한 DPR(Dense Passage Retrieval)이 대표 사례다.

## 정의

Dense Retrieval는 두 개의 인코더(주로 질의용·문서용)를 사용해 텍스트를 고정 차원의 [밀집 벡터](text-embedding.md)로 변환한다. 검색 시점에는 질의 벡터와 미리 색인해 둔 문서 벡터들 사이의 유사도를 계산해 상위 k개를 반환한다. 코퍼스가 커지면 모든 벡터와의 정확한 비교가 비싸지므로 FAISS 같은 라이브러리의 ANN 색인으로 근사 검색을 수행한다. 검색 단위가 되는 텍스트 조각은 [Text Chunking (청킹)](text-chunking.md)으로 미리 분할한다.

## GraphRAG에서 중요한 이유

Dense Retrieval는 표준 [RAG (검색 증강 생성)](retrieval-augmented-generation.md)의 기본 검색기이며, 대부분의 [GraphRAG (the paradigm)](graph-rag.md) 시스템도 이를 출발점으로 삼는다. 다만 벡터 유사도만으로는 여러 문서에 흩어진 근거를 잇는 [Multi-hop Reasoning (멀티홉 추론)](multi-hop-reasoning.md)이나 전역 요약 질의에 약하다. GraphRAG는 벡터 검색으로 진입점(엔티티·청크)을 찾은 뒤 [Knowledge Graph](knowledge-graph.md) 위의 탐색으로 이를 확장하거나, 그래프 구조와 결합한 [Hybrid Retrieval](../techniques/hybrid-retrieval.md)로 약점을 보완한다.

## 실제 활용

Dense Retrieval는 개방형 질의응답, 사내 문서 검색, 시맨틱 검색 엔진 등에서 폭넓게 쓰인다. 실무에서는 BM25 같은 희소 검색과 점수를 결합하는 하이브리드 구성이 흔하며, [HippoRAG](../methods/hipporag.md)나 [LightRAG](../methods/lightrag.md) 같은 시스템도 벡터 색인을 그래프 신호와 함께 사용한다.

## 관련 항목
- [Retrieval-Augmented Generation (RAG)](retrieval-augmented-generation.md) — Dense Retrieval를 표준 검색기로 사용하는 상위 패러다임
- [Text Embedding (텍스트 임베딩)](text-embedding.md) — 질의와 문서를 벡터로 표현해 밀집 검색을 가능하게 하는 기반 기술
- [Text Chunking (청킹)](text-chunking.md) — 벡터로 색인할 검색 단위를 만드는 전처리 단계
- [GraphRAG (the paradigm)](graph-rag.md) — 벡터 검색을 그래프 구조로 보강하는 패러다임
- [Hybrid Retrieval](../techniques/hybrid-retrieval.md) — 밀집·희소·그래프 신호를 결합해 검색 품질을 높이는 기법
- [Knowledge Graph](knowledge-graph.md) — 벡터 검색의 진입점을 확장하는 구조화된 지식 표현
- [Multi-hop Reasoning (멀티홉 추론)](multi-hop-reasoning.md) — 순수 벡터 검색이 취약하고 GraphRAG가 보완하는 과제
- [HippoRAG](../methods/hipporag.md) — 벡터 색인과 그래프 탐색을 결합하는 대표 시스템

## 참고문헌
- Karpukhin, V., Oğuz, B., Min, S., Lewis, P., Wu, L., Edunov, S., Chen, D., & Yih, W. (2020). *Dense Passage Retrieval for Open-Domain Question Answering*. EMNLP 2020. arXiv:2004.04906 — https://arxiv.org/abs/2004.04906
