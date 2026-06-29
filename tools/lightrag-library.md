---
type: Tool
title: LightRAG (HKUDS library)
description: 홍콩대 데이터 인텔리전스 랩(HKUDS)이 공개한 그래프 기반 RAG 프레임워크의 공식 오픈소스 구현체로, 지식 그래프와 벡터 검색을 결합한 이중 수준 검색을 제공한다.
tags: [graphrag, retrieval, knowledge-graph, open-source, lightrag]
timestamp: 2026-06-29
resource: https://github.com/HKUDS/LightRAG
authors: [Zirui Guo, Lianghao Xia, Yanhua Yu, Tu Ao, Chao Huang]
year: 2024
venue: Findings of EMNLP 2025
arxiv: "2410.05779"
---

# LightRAG (HKUDS library)

LightRAG (HKUDS library)는 홍콩대 데이터 인텔리전스 랩(HKUDS)이 공개한 [LightRAG](../methods/lightrag.md) 방법론의 공식 레퍼런스 구현체(reference implementation)다. 문서 색인 과정에서 지식 그래프([Knowledge Graph](../concepts/knowledge-graph.md))를 구축하고, 이를 벡터 검색과 결합해 질의에 응답하는 경량 RAG([Retrieval-Augmented Generation](../concepts/retrieval-augmented-generation.md)) 라이브러리다. Microsoft GraphRAG보다 가벼운 대안을 표방하며 MIT 라이선스로 배포된다.

## 개요

라이브러리는 LLM([Large Language Model](../concepts/large-language-model.md))을 사용해 텍스트 청크에서 엔티티와 관계를 추출([Entity & Relationship Extraction](../techniques/entity-relationship-extraction.md))하여 그래프를 만들고, 그래프와 벡터 표현을 함께 저장한다. 검색은 세부 사실 중심의 저수준(low-level) 검색과 추상 개념 중심의 고수준(high-level) 검색을 결합한 이중 수준 방식을 사용한다.

## 주요 기능

- 그래프 기반 색인과 [하이브리드 검색](../techniques/hybrid-retrieval.md)을 결합한 다섯 가지 질의 모드(local, global, hybrid, naive, mix)
- 색인·질의 시 LLM 호출을 줄여 비용과 지연을 낮추는 경량 파이프라인
- 집합 병합 기반의 증분 업데이트로 기존 그래프를 헐지 않고 신규 문서를 통합
- KV·벡터·그래프·문서 상태 저장소를 분리한 구조로 PostgreSQL, [Neo4j](neo4j.md), Milvus, Qdrant 등 다양한 백엔드 지원

## GraphRAG에서의 일반적 사용

GraphRAG([GraphRAG (the paradigm)](../concepts/graph-rag.md)) 파이프라인을 직접 구축할 때, 문서 컬렉션에서 자동으로 지식 그래프를 만들고 멀티홉 추론([Multi-hop Reasoning](../concepts/multi-hop-reasoning.md))이 필요한 질의에 응답하는 백엔드로 흔히 쓰인다. [microsoft/graphrag](microsoft-graphrag-library.md)나 [nano-graphrag](nano-graphrag.md)와 함께 경량·실용 GraphRAG 구현을 비교·선택하는 대상이 된다.

## 관련 항목

- [LightRAG](../methods/lightrag.md) — 이 라이브러리가 구현하는 방법론 논문
- [microsoft/graphrag (library)](microsoft-graphrag-library.md) — LightRAG가 경량 대안으로 비교하는 구현체
- [nano-graphrag](nano-graphrag.md) — 또 다른 경량 GraphRAG 구현 라이브러리
- [Neo4j](neo4j.md) — 그래프 저장소 백엔드로 지원되는 그래프 데이터베이스
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — 이 도구가 구현하는 전체 패러다임
- [Entity & Relationship Extraction](../techniques/entity-relationship-extraction.md) — 그래프 구축에 사용하는 핵심 추출 기법
- [Hybrid Retrieval](../techniques/hybrid-retrieval.md) — 그래프와 벡터 검색을 결합하는 질의 방식

## 참고문헌

- Guo, Z., Xia, L., Yu, Y., Ao, T., & Huang, C. (2024). *LightRAG: Simple and Fast Retrieval-Augmented Generation*. Findings of EMNLP 2025. arXiv:2410.05779 — https://arxiv.org/abs/2410.05779
