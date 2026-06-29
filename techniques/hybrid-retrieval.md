---
type: Technique
title: Hybrid Retrieval
description: 벡터(밀집) 검색, 키워드(희소) 검색, 그래프 탐색 등 서로 다른 검색 신호를 결합해 재현율과 정밀도를 함께 끌어올리는 검색 기법이다.
tags: [graphrag, retrieval, dense-retrieval, knowledge-graph, dual-level-retrieval]
timestamp: 2026-06-29
---

# Hybrid Retrieval

하이브리드 검색(Hybrid Retrieval)은 의미 기반의 벡터 검색, 어휘 기반의 키워드 검색, 그래프 구조 탐색처럼 성격이 다른 검색 신호를 하나의 파이프라인에서 결합하는 기법이다. 각 방식이 가진 약점을 서로 보완하여, 단일 신호만 쓸 때보다 재현율(recall)과 정밀도(precision)를 함께 높이는 것을 목표로 한다. [GraphRAG](../concepts/graph-rag.md) 계열에서는 특히 벡터 임베딩과 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)의 관계 구조를 결합하는 형태로 자주 쓰인다.

## 개념

[Dense Retrieval / Vector Search](../concepts/dense-retrieval.md)는 의미적으로 유사한 내용을 잘 찾지만, 드문 고유명사나 정확한 키워드 일치에는 약하다. 반대로 BM25 같은 희소(키워드) 검색은 정확한 용어 매칭에 강하나 동의어나 의역을 놓친다. 그래프 탐색은 명시적 관계를 따라가 [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md)에 필요한 연결된 근거를 모은다. 하이브리드 검색은 이 상호 보완성을 활용해 어느 한 방식이 놓치는 문서를 다른 방식이 메우도록 한다.

## 동작 방식

여러 검색기를 병렬로 실행한 뒤 그 결과를 하나의 순위로 통합하는 것이 핵심이다. 통합 방식으로는 점수를 가중 합산하거나, 순위를 결합하는 Reciprocal Rank Fusion(RRF), 또는 1차 후보를 모은 뒤 재정렬(re-ranking)하는 방법 등이 쓰인다. 그래프 신호를 섞는 경우에는 [Text Embedding (텍스트 임베딩)](../concepts/text-embedding.md)으로 찾은 진입 노드에서 출발해 이웃 엔터티와 관계로 [Subgraph Extraction](subgraph-extraction.md)을 수행하고, 그 구조적 근거를 벡터·키워드 결과와 함께 컨텍스트로 제공한다.

## GraphRAG에서의 활용

[LightRAG](../methods/lightrag.md)의 이중 수준(dual-level) 검색이 대표적 사례로, 특정 엔터티를 겨냥하는 저수준 키와 넓은 주제를 겨냥하는 고수준 키를 함께 만들어 그래프 위의 벡터 검색과 이웃 확장을 결합한다. [Microsoft GraphRAG](../methods/microsoft-graphrag.md)의 [Local vs Global Search](local-and-global-search.md)에서도 지역 검색이 엔터티 임베딩과 그래프 이웃, 원문 청크를 함께 끌어와 하이브리드적 컨텍스트를 구성한다. 이러한 신호 결합은 근거의 폭을 넓혀 [환각 (Hallucination)](../concepts/hallucination.md)을 줄이는 데 기여한다.

## 관련 항목
- [LightRAG](../methods/lightrag.md) — 이중 수준 검색으로 벡터와 그래프 신호를 결합한 대표 사례.
- [Dense Retrieval / Vector Search](../concepts/dense-retrieval.md) — 하이브리드 검색이 결합하는 의미 기반 검색 축.
- [Subgraph Extraction](subgraph-extraction.md) — 그래프 신호를 검색에 끌어오는 핵심 단계.
- [Local vs Global Search](local-and-global-search.md) — 지역 검색에서 여러 근거를 결합하는 GraphRAG 질의 모드.
- [Text Embedding (텍스트 임베딩)](../concepts/text-embedding.md) — 벡터 검색과 그래프 진입 노드 매칭의 기반.
- [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md) — 그래프 탐색 신호가 보강하는 추론 유형.
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — 하이브리드 검색이 적용되는 상위 패러다임.
- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md) — 하이브리드 검색이 검색 단계를 강화하는 큰 틀.
