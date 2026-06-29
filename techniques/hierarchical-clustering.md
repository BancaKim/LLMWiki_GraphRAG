---
type: Technique
title: Hierarchical Clustering
description: 청크나 그래프 노드를 재귀적으로 군집화·요약해 여러 추상화 수준을 갖는 트리(RAPTOR)나 계층적 커뮤니티(GraphRAG)를 구성하는 색인 기법이다.
tags: [graphrag, clustering, hierarchical, retrieval, summarization]
timestamp: 2026-06-29
---

# Hierarchical Clustering

계층적 클러스터링(Hierarchical Clustering)은 데이터 항목을 여러 층위의 중첩된 군집으로 조직하는 기법군이다. RAG 맥락에서는 [청크 (Text Chunking)](../concepts/text-chunking.md)나 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)의 노드를 재귀적으로 묶고 각 군집을 요약하여, 하위 층은 세부 사실을 상위 층은 넓은 주제를 담는 트리 또는 계층적 커뮤니티를 만든다. 이렇게 사전 구성된 다단 추상화 색인은 질의의 폭에 맞는 적절한 일반화 수준에서 정보를 검색하도록 돕는다.

## 개념

핵심 목표는 단일 평면 색인이 아니라 여러 일반화 수준에서 질의할 수 있는 구조를 만드는 것이다. 군집화 방식은 응집형(작은 군집을 위로 병합)과 분할형(전체를 아래로 분할)으로 나뉘며, 군집마다 [LLM (Large Language Model)](../concepts/large-language-model.md)으로 요약을 생성해 상위 노드를 채운다는 점이 일반적 클러스터링과 다르다. 이 구조 덕분에 좁은 질의는 트리 하단의 구체적 노드에서, 넓은 [Query-Focused Summarization (QFS)](../concepts/query-focused-summarization.md)형 질의는 상단의 추상 요약에서 근거를 얻을 수 있다.

## 동작 방식

대표 구현인 [RAPTOR](../methods/raptor.md)는 청크를 [텍스트 임베딩 (Text Embedding)](../concepts/text-embedding.md)으로 변환한 뒤 소프트 군집화(GMM 기반)로 묶고, 각 군집을 LLM이 요약해 새 노드를 만든다. 이 요약 노드를 다시 임베딩·군집화·요약하는 과정을 토큰 수가 충분히 줄어들 때까지 반복하여 트리를 쌓는다. 그래프 기반 접근에서는 [커뮤니티 탐지 (Community Detection)](community-detection.md)를 여러 해상도로 적용해 다층 커뮤니티를 얻고, 각 층에 대해 [커뮤니티 요약 (Community Summarization)](community-summarization.md)을 수행한다. 검색 시에는 트리 전체를 펼쳐 보거나(collapsed), 루트에서 관련 가지를 따라 내려가는 방식으로 노드를 고른다.

## GraphRAG에서의 활용

[Microsoft GraphRAG](../methods/microsoft-graphrag.md)는 [지식 그래프 구축 (Knowledge Graph Construction)](knowledge-graph-construction.md) 후 그래프를 다층 커뮤니티로 분할하고 각 층을 요약함으로써, 계층적 클러스터링을 [전역·지역 검색 (Local vs Global Search)](local-and-global-search.md)의 색인 토대로 삼는다. 이렇게 만든 추상화 계층은 단순 [Dense Retrieval / Vector Search](../concepts/dense-retrieval.md)가 놓치는, 말뭉치 전반을 조망해야 하는 질문에 답하는 데 쓰인다. RAPTOR처럼 그래프 없이 청크만으로 트리를 만드는 변형도 존재하여, 계층적 클러스터링은 그래프 유무와 무관하게 다단 검색을 가능하게 하는 공통 토대다.

## 관련 항목
- [RAPTOR](../methods/raptor.md) — 청크를 재귀 군집화·요약해 검색 트리를 만드는 대표 기법.
- [Community Detection (Leiden)](community-detection.md) — 그래프를 다층 커뮤니티로 나누는 군집화 단계.
- [Community Summarization](community-summarization.md) — 각 계층 군집을 요약해 상위 노드를 채우는 후속 단계.
- [Microsoft GraphRAG](../methods/microsoft-graphrag.md) — 계층적 커뮤니티를 색인에 활용하는 대표 기법.
- [Local vs Global Search](local-and-global-search.md) — 계층 색인을 질의 폭에 맞춰 활용하는 검색 전략.
- [Query-Focused Summarization (QFS)](../concepts/query-focused-summarization.md) — 상위 추상화 층이 겨냥하는 질의 유형.
- [Text Embedding (텍스트 임베딩)](../concepts/text-embedding.md) — 군집화의 입력이 되는 벡터 표현.
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — 계층적 색인을 검색 단계에 포함하는 상위 패러다임.
