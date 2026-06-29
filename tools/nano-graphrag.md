---
type: Tool
title: nano-graphrag
description: Microsoft GraphRAG의 핵심 기능을 약 1100줄 규모로 재구현한 가볍고 수정하기 쉬운 오픈소스 GraphRAG 파이썬 라이브러리.
tags: [graphrag, retrieval, knowledge-graph, open-source, python]
timestamp: 2026-06-29
resource: https://github.com/gusye1234/nano-graphrag
---

# nano-graphrag

nano-graphrag는 gusye1234가 공개한 오픈소스 파이썬 라이브러리로, [GraphRAG](../concepts/graph-rag.md) 파이프라인을 작고 읽기 쉬운 코드로 재구현한 것이다. 테스트와 프롬프트를 제외하면 약 1100줄에 불과하며, 비동기(asynchronous) 처리와 타입 힌트를 지원한다. [Microsoft GraphRAG](../methods/microsoft-graphrag.md)의 원본 구현이 읽거나 수정하기 어렵다는 점을 동기로 삼아, 동일한 핵심 동작을 더 단순하게 제공하는 것을 목표로 한다.

## 개요

nano-graphrag는 문서를 [청킹](../concepts/text-chunking.md)한 뒤 [LLM](../concepts/large-language-model.md)으로 [엔티티·관계 추출](../techniques/entity-relationship-extraction.md)을 수행해 [지식 그래프](../concepts/knowledge-graph.md)를 구성하고, [커뮤니티 탐지](../techniques/community-detection.md)와 [커뮤니티 요약](../techniques/community-summarization.md)을 거쳐 질의에 답한다. 검색 단계는 local, global 두 가지 GraphRAG 검색과 일반 벡터 기반의 naive RAG를 지원한다. 다만 원본 Microsoft GraphRAG의 covariates 기능은 구현하지 않았고, global 검색의 세부 동작도 원본과 차이가 있다.

## 주요 기능

- 약 1100줄의 소형 코드베이스로, 비동기 및 전체 타입 지정(fully typed)을 지원한다.
- MD5 해시 기반 콘텐츠 키를 사용해 중복 계산을 피하는 증분 삽입(incremental insert)을 제공한다.
- LLM(OpenAI, Amazon Bedrock, DeepSeek, Ollama), 임베딩(OpenAI, Bedrock, Sentence-transformers), 벡터 저장소(nano-vectordb, hnswlib, milvus-lite, faiss), 그래프 저장소(NetworkX 기본, Neo4j) 등 구성요소를 교체할 수 있다.
- 계획·응답에는 고성능 LLM, 요약에는 저렴한 LLM을 나누어 쓰는 방식을 권장한다(기본값 gpt-4o, gpt-4o-mini).

## GraphRAG에서의 일반적 사용

연구 및 실험 환경에서 Microsoft GraphRAG의 무거운 의존성과 복잡한 코드 없이 GraphRAG 파이프라인을 빠르게 시험하거나, 검색 로직·저장소·프롬프트를 직접 수정·확장하려는 경우에 활용된다. 기본 [그래프 저장소](../tools/neo4j.md)로 NetworkX를 사용하지만 Neo4j로 교체할 수 있어, 소규모 프로토타이핑부터 커스텀 GraphRAG 변형 구현까지 폭넓게 쓰인다.

## 링크

- GitHub: https://github.com/gusye1234/nano-graphrag

## 관련 항목

- [microsoft/graphrag (library)](microsoft-graphrag-library.md) — nano-graphrag가 단순화 대상으로 삼은 공식 참조 구현 라이브러리
- [Microsoft GraphRAG](../methods/microsoft-graphrag.md) — nano-graphrag가 재구현한 원본 방법론
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — 본 도구가 구현하는 검색·생성 패러다임
- [LightRAG (HKUDS library)](lightrag-library.md) — 유사하게 경량화를 지향하는 그래프 기반 RAG 라이브러리
- [Neo4j](neo4j.md) — 교체 가능한 그래프 저장소 백엔드
- [Community Detection (Leiden)](../techniques/community-detection.md) — 그래프에서 커뮤니티를 식별하는 핵심 단계
- [Entity & Relationship Extraction](../techniques/entity-relationship-extraction.md) — 그래프 구성을 위한 LLM 기반 추출 단계
- [Local vs Global Search](../techniques/local-and-global-search.md) — nano-graphrag가 지원하는 두 가지 검색 모드

## 참고문헌

- gusye1234 et al. *nano-graphrag: A simple, easy-to-hack GraphRAG implementation*. GitHub. — https://github.com/gusye1234/nano-graphrag
