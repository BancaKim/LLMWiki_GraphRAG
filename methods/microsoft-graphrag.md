---
type: Method
title: Microsoft GraphRAG
description: 텍스트 말뭉치에서 LLM으로 엔터티 지식 그래프를 구축하고 커뮤니티 단위로 사전 요약하여, 전역적 sensemaking 질의를 query-focused summarization 방식으로 답하는 그래프 기반 RAG 기법.
tags: [graphrag, retrieval, knowledge-graph, query-focused-summarization, community-detection]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2404.16130
authors: [Darren Edge, Ha Trinh, Newman Cheng, Joshua Bradley, Alex Chao, Apurva Mody, Steven Truitt, Dasha Metropolitansky, Robert Osazuwa Ness, Jonathan Larson]
year: 2024
venue: arXiv preprint (Microsoft Research)
arxiv: "2404.16130"
---

# Microsoft GraphRAG

Microsoft GraphRAG는 비공개 텍스트 말뭉치에 대한 질의응답을 위해, 먼저 LLM(대규모 언어 모델)으로 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)를 구축한 뒤 관련 엔터티들의 커뮤니티로 분할하는 [그래프 기반 RAG](../concepts/graph-rag.md) 기법이다. "이 데이터셋의 주요 주제는 무엇인가?" 같은 *전역적(global) sensemaking* 질문을 표적으로 하는데, 이런 질문은 본질적으로 국소 검색이 아니라 [Query-Focused Summarization (QFS)](../concepts/query-focused-summarization.md) 과제이기 때문에 통상적인 [RAG (Retrieval-Augmented Generation)](../concepts/retrieval-augmented-generation.md)로는 잘 처리되지 않는다.

## 개요

표준 top-k 벡터 검색은 답이 소수의 [청크 (Text Chunking)](../concepts/text-chunking.md)에 담겨 있지 않은 전체 말뭉치 단위 질문에서 실패한다. GraphRAG는 구절을 직접 검색하는 대신, 말뭉치를 다양한 일반화 수준에서 질의할 수 있는 계층적 색인을 사전에 계산해 이 문제에 대응한다.

## 핵심 아이디어 / 동작 방식

색인 단계에서 LLM으로 [엔터티·관계 추출 (Entity & Relationship Extraction)](../techniques/entity-relationship-extraction.md)을 수행해 엔터티 그래프를 만든 뒤, Leiden 알고리즘 기반 [커뮤니티 탐지 (Community Detection)](../techniques/community-detection.md)로 엔터티들을 계층적 클러스터로 분할한다. 각 클러스터에 대해 LLM이 [커뮤니티 요약 (Community Summarization)](../techniques/community-summarization.md)으로 보고서를 미리 생성한다. 질의 시점(global search)에는 관련 커뮤니티 요약마다 부분 답변이 병렬로 생성되고, map-reduce 단계가 이를 결합해 최종 응답을 만든다. 반면 local search는 특정 엔터티에 답을 근거시킨다.

## 기여

[국소 대 전역 검색 (Local vs Global Search)](../techniques/local-and-global-search.md)의 구분을 도입하고, 백만 토큰 규모 말뭉치에서 커뮤니티 요약이 벡터-RAG 베이스라인 대비 답변의 포괄성과 다양성을 높임을 보였으며, 오픈소스 참조 구현을 함께 제공했다.

## 강점과 한계

강점은 전역적 sensemaking 성능이 우수하고 근거 기반 요약을 통해 [환각 (Hallucination)](../concepts/hallucination.md)을 줄인다는 점이다. 주요 한계는 LLM 기반 그래프 구축과 전수 요약에 드는 높은 토큰·연산 비용으로, 이는 이후 [LazyGraphRAG](lazygraphrag.md)와 [LightRAG](lightrag.md)가 완화하려 한 지점이다.

## 관련 항목
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — 이 논문이 해당 용어와 패러다임을 대중화했다.
- [LazyGraphRAG](lazygraphrag.md) — 요약을 지연시켜 색인 비용을 줄인 Microsoft 후속 연구.
- [LightRAG](lightrag.md) — 증분 갱신을 지원하는 경량 그래프 색인 대안.
- [microsoft/graphrag (library)](../tools/microsoft-graphrag-library.md) — 이 기법의 공식 오픈소스 구현체.
- [Community Summarization](../techniques/community-summarization.md) — 이 기법이 의존하는 핵심 색인 기술.
- [Query-Focused Summarization (QFS)](../concepts/query-focused-summarization.md) — 전역 질의에 대한 과제 정의.
- [HippoRAG](hipporag.md) — Personalized PageRank 검색을 쓰는 대조적 그래프-RAG 기법.
- [Graph RAG: A Survey (Peng et al.)](../surveys/graph-rag-survey.md) — GraphRAG를 더 넓은 지형 속에 위치시킨다.

## 참고문헌
- Edge, D., Trinh, H., Cheng, N., Bradley, J., Chao, A., Mody, A., Truitt, S., Metropolitansky, D., Ness, R. O., & Larson, J. (2024). *From Local to Global: A Graph RAG Approach to Query-Focused Summarization*. arXiv preprint (Microsoft Research). arXiv:2404.16130 — https://arxiv.org/abs/2404.16130
