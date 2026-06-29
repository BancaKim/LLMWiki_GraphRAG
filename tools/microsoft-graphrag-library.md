---
type: Tool
title: microsoft/graphrag (library)
description: Microsoft Research가 공개한 GraphRAG의 공식 오픈소스 Python 라이브러리로, 비정형 텍스트에서 엔터티 지식 그래프를 색인하고 local/global/DRIFT 검색으로 질의하는 모듈식 RAG 파이프라인을 제공한다.
tags: [graphrag, retrieval, knowledge-graph, python, open-source]
timestamp: 2026-06-29
resource: https://github.com/microsoft/graphrag
---

# microsoft/graphrag (library)

microsoft/graphrag는 [Microsoft GraphRAG](../methods/microsoft-graphrag.md) 기법의 공식 오픈소스 참조 구현체로, github.com/microsoft/graphrag에서 배포되는 Python 라이브러리다. LLM(대규모 언어 모델)을 이용해 비정형 텍스트에서 구조화된 데이터를 추출하는 데이터 파이프라인이자 변환 도구 모음이며, MIT 라이선스로 제공되고 PyPI에서 `graphrag` 패키지로 설치할 수 있다. 다만 공식 문서는 이것이 정식 지원되는 Microsoft 제품이 아니라 연구 시연용 코드임을 명시한다.

## 개요

이 라이브러리는 [그래프 기반 RAG](../concepts/graph-rag.md) 워크플로를 색인(indexing)과 질의(query)의 두 단계로 나눠 모듈식으로 구현한다. 색인 파이프라인은 입력 말뭉치를 처리해 엔터티 그래프와 계층적 커뮤니티 요약을 산출하고, 질의 단계는 이렇게 사전 계산된 산출물을 활용해 응답을 생성한다. CLI와 Python API를 모두 제공하며, 동작은 설정 파일과 프롬프트 튜닝으로 조정한다.

## 주요 기능

- LLM 기반 [엔터티·관계 추출 (Entity & Relationship Extraction)](../techniques/entity-relationship-extraction.md)을 통한 [지식 그래프 구축 (Knowledge Graph Construction)](../techniques/knowledge-graph-construction.md).
- Leiden 알고리즘을 사용하는 [커뮤니티 탐지 (Community Detection)](../techniques/community-detection.md)와 [커뮤니티 요약 (Community Summarization)](../techniques/community-summarization.md).
- 세 가지 검색 모드: 특정 엔터티에 답을 근거시키는 local search, 커뮤니티 보고서를 map-reduce로 종합하는 global search, 그리고 둘을 결합한 [DRIFT Search](../techniques/drift-search.md).
- 프롬프트 자동 튜닝과 설정 가능한 색인 파이프라인.

## GraphRAG에서의 일반적 사용

연구자와 실무자는 이 라이브러리를 GraphRAG 패러다임의 기준 구현으로 삼아 비교 baseline이나 프로덕션 색인 도구로 활용한다. [LazyGraphRAG](../methods/lazygraphrag.md)나 [nano-graphrag](nano-graphrag.md) 같은 변형·경량 구현이 이 코드베이스를 참조하거나 단순화한 형태로 등장했고, 산출된 그래프는 [Neo4j](neo4j.md) 등 외부 그래프 저장소와 연계되기도 한다.

## 링크

- 저장소: https://github.com/microsoft/graphrag
- 문서: https://microsoft.github.io/graphrag/

## 관련 항목
- [Microsoft GraphRAG](../methods/microsoft-graphrag.md) — 이 라이브러리가 구현하는 원본 기법.
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — 이 도구가 대표하는 더 넓은 패러다임.
- [DRIFT Search](../techniques/drift-search.md) — 이 라이브러리가 추가한 local/global 결합 검색 모드.
- [Community Summarization](../techniques/community-summarization.md) — 색인 파이프라인의 핵심 단계.
- [nano-graphrag](nano-graphrag.md) — 동일 패러다임을 단순화한 경량 구현.
- [LazyGraphRAG](../methods/lazygraphrag.md) — 색인 비용을 줄인 Microsoft 후속 변형.
- [LightRAG (HKUDS library)](lightrag-library.md) — 증분 갱신을 지향하는 대안 그래프-RAG 라이브러리.
- [Neo4j](neo4j.md) — 산출 그래프를 저장·질의할 수 있는 외부 그래프 데이터베이스.

## 참고문헌
- Edge, D., Trinh, H., Cheng, N., Bradley, J., Chao, A., Mody, A., Truitt, S., Metropolitansky, D., Ness, R. O., & Larson, J. (2024). *From Local to Global: A Graph RAG Approach to Query-Focused Summarization*. arXiv preprint (Microsoft Research). arXiv:2404.16130 — https://arxiv.org/abs/2404.16130
