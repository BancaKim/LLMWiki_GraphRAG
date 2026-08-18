---
type: Concept
title: GraphRAG (the paradigm)
description: 평면 벡터 색인 대신 그래프 또는 지식 그래프를 검색 인덱스로 사용하는 RAG 패러다임으로, 인덱싱 단계에서 그래프를 구축하고 질의 단계에서 지역 질문과 전역 질문을 그래프 구조로 답한다.
tags: [graphrag, retrieval, knowledge-graph, rag, multi-hop-reasoning]
timestamp: 2026-06-29
---

# GraphRAG (the paradigm)

GraphRAG(그래프 기반 검색 증강 생성)는 검색 인덱스로 평면적인 벡터 저장소가 아니라 그래프, 특히 [Knowledge Graph](knowledge-graph.md)를 사용하는 [RAG (Retrieval-Augmented Generation)](retrieval-augmented-generation.md)의 한 갈래이자 포괄 개념이다. 텍스트를 독립된 조각으로만 다루는 대신 개체(entity)와 그 사이의 관계를 명시적 구조로 표현하여, 여러 문서에 흩어진 정보를 잇거나 코퍼스 전체를 조망하는 질문에 답하는 것을 목표로 한다. 이는 단일 시스템이 아니라 Microsoft GraphRAG, LightRAG, HippoRAG 등 다양한 구현이 공유하는 설계 방향을 가리킨다.

## 정의

GraphRAG 파이프라인은 보통 두 단계로 나뉜다. 인덱싱 단계에서는 원본 문서를 처리해 [Knowledge Graph Construction](../techniques/knowledge-graph-construction.md)을 수행한다. 즉 [Entity & Relationship Extraction](../techniques/entity-relationship-extraction.md)으로 노드와 엣지를 뽑고, 필요하면 [Community Detection (Leiden)](../techniques/community-detection.md)과 [Community Summarization](../techniques/community-summarization.md)으로 그래프를 계층화한다. 질의 단계에서는 질문을 그래프에 정합시켜 관련 부분 그래프나 요약을 검색하고, 이를 [LLM (Large Language Model)](large-language-model.md)의 생성 근거로 제공한다.

## GraphRAG에서 중요한 이유

핵심 동기는 검색 단위를 평면 텍스트에서 구조로 바꾸는 데 있다. 그래프 구조는 경로를 따라 사실을 연결하므로 [Multi-hop Reasoning (멀티홉 추론)](multi-hop-reasoning.md)에 유리하고, 명시적 근거 제공으로 [Hallucination (환각)](hallucination.md)을 줄이는 데 기여한다. 또한 질문 유형을 [Local vs Global Search](../techniques/local-and-global-search.md)로 구분한다. 지역(local) 질문은 특정 개체 주변의 이웃을 탐색해 답하고, 전역(global) 질문은 [Query-Focused Summarization (QFS)](query-focused-summarization.md)처럼 코퍼스 전반을 종합해 답하므로 표준 벡터 검색이 약한 영역을 보완한다.

## 실제 활용

GraphRAG는 기업 문서·기술 매뉴얼·과학 문헌처럼 개체 간 관계가 풍부한 도메인에서 질의응답과 요약에 쓰인다. 대표적으로 Microsoft GraphRAG는 커뮤니티 요약 기반 전역 검색을, HippoRAG는 그래프 위 [Personalized PageRank](../techniques/personalized-pagerank.md) 검색을 사용한다. 설계 방향과 분류는 [Graph RAG: A Survey (Peng et al.)](../surveys/graph-rag-survey.md)에 정리되어 있다.

## 관련 항목
- [Retrieval-Augmented Generation (RAG)](retrieval-augmented-generation.md) — GraphRAG가 검색 대상을 그래프로 확장하기 전의 상위 개념
- [Knowledge Graph](knowledge-graph.md) — GraphRAG가 검색 인덱스로 삼는 핵심 데이터 구조
- [Local vs Global Search](../techniques/local-and-global-search.md) — 지역·전역 질문을 나누는 GraphRAG의 질의 전략
- [Knowledge Graph Construction](../techniques/knowledge-graph-construction.md) — 인덱싱 단계에서 그래프를 만드는 과정
- [Multi-hop Reasoning (멀티홉 추론)](multi-hop-reasoning.md) — 그래프 구조가 특히 강점을 보이는 과제
- [Microsoft GraphRAG](../methods/microsoft-graphrag.md) — 커뮤니티 요약 기반 전역 검색을 제시한 대표 구현
- [HippoRAG](../methods/hipporag.md) — 개인화 PageRank로 그래프를 검색하는 대표 구현
- [Graph RAG: A Survey (Peng et al.)](../surveys/graph-rag-survey.md) — GraphRAG 방법론을 체계적으로 정리한 서베이
- [When to use Graphs in RAG](../surveys/when-to-use-graphs-in-rag.md) — 그래프 구조가 실제로 이득이 되는 조건을 따진 분석
- [GraphRAG 보안과 지식 포이즈닝](graphrag-security.md) — 그래프 색인이 새로 만들어 내는 공격면과 방어 과제
