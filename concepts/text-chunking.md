---
type: Concept
title: Text Chunking (청킹)
description: 긴 문서를 검색·색인의 기본 단위가 되도록 작은 텍스트 조각으로 분할하는 전처리로, 청크 크기와 중첩의 트레이드오프가 검색 품질을 좌우하며 GraphRAG에서는 청크가 그래프의 노드로 쓰이기도 한다.
tags: [text-chunking, retrieval, graphrag, indexing, preprocessing]
timestamp: 2026-06-29
---

# Text Chunking (청킹)

Text Chunking(청킹)은 긴 문서를 검색과 색인의 기본 단위가 되는 작은 텍스트 조각(청크)으로 분할하는 전처리 단계다. [LLM (Large Language Model)](large-language-model.md)의 문맥 창과 임베딩 입력 길이에는 한계가 있으므로, 문서를 통째로 다루는 대신 다루기 좋은 크기로 나눈다. 각 청크는 [텍스트 임베딩](text-embedding.md)으로 벡터화되어 색인되며, [RAG (검색 증강 생성)](retrieval-augmented-generation.md)와 [GraphRAG](graph-rag.md) 파이프라인의 출발점이 된다.

## 정의

청킹은 문서를 일정 토큰·문자 수 단위로 자르거나, 문장·단락·제목 같은 구조 경계를 따라 분할한다. 핵심 설계 변수는 청크 크기와 청크 간 중첩(overlap)이다. 청크가 너무 크면 한 조각에 여러 주제가 섞여 검색 정밀도가 떨어지고, 너무 작으면 맥락이 끊겨 의미가 불완전해진다. 인접 청크끼리 일부 내용을 겹치게 두는 중첩은 경계에서 잘린 정보의 손실을 줄이지만, 저장·연산 비용을 늘린다. 이처럼 청킹은 정밀도와 맥락 보존 사이의 트레이드오프를 조율하는 작업이다.

## GraphRAG에서 중요한 이유

[GraphRAG](graph-rag.md)에서 청크는 인덱스의 일차 입력 단위다. 각 청크에서 [개체·관계 추출](../techniques/entity-relationship-extraction.md)을 수행해 [지식 그래프](knowledge-graph.md)를 구축하므로, 청크 경계가 어디에 놓이느냐가 추출되는 개체와 관계의 품질에 직접 영향을 준다. 또한 [Microsoft GraphRAG](../methods/microsoft-graphrag.md)를 비롯한 여러 시스템에서 청크 자체가 그래프의 노드가 되어, 추출된 개체와 출처(provenance)로 연결된다. 이렇게 청크 노드와 개체 노드가 함께 놓이면 [밀집 검색](dense-retrieval.md)으로 찾은 진입점에서 그래프 탐색으로 근거를 확장할 수 있어, 여러 청크에 흩어진 단서를 잇는 [멀티홉 추론](multi-hop-reasoning.md)에 유리하다.

## 실제 활용

실무에서는 고정 크기 분할, 문장·단락 단위 분할, 문서의 헤딩 구조를 따르는 분할, 의미 경계를 추정하는 시맨틱 청킹 등 여러 전략을 데이터 특성에 맞게 선택한다. [microsoft/graphrag](../tools/microsoft-graphrag-library.md), [nano-graphrag](../tools/nano-graphrag.md), [LightRAG](../methods/lightrag.md) 같은 도구는 청크 크기와 중첩을 설정값으로 노출해 색인 단위를 조정하게 한다. 청크 크기는 임베딩 비용, 검색 대상 수, 추출 정확도에 두루 영향을 주므로 대표적인 튜닝 대상이 된다.

## 관련 항목
- [Text Embedding (텍스트 임베딩)](text-embedding.md) — 각 청크를 벡터로 변환해 색인하는 표현 기술
- [Dense Retrieval / Vector Search](dense-retrieval.md) — 청크 벡터를 유사도로 검색하는 기본 검색기
- [Retrieval-Augmented Generation (RAG)](retrieval-augmented-generation.md) — 청크를 검색 단위로 삼는 상위 프레임워크
- [GraphRAG (the paradigm)](graph-rag.md) — 청크를 그래프 노드와 추출 입력으로 활용하는 패러다임
- [Entity & Relationship Extraction](../techniques/entity-relationship-extraction.md) — 청크에서 개체·관계를 뽑아 그래프를 만드는 단계
- [Knowledge Graph](knowledge-graph.md) — 청크에서 추출된 개체·관계로 구성되는 구조
- [Microsoft GraphRAG](../methods/microsoft-graphrag.md) — 청크를 노드로 두고 색인을 구축하는 대표 시스템
- [Multi-hop Reasoning (멀티홉 추론)](multi-hop-reasoning.md) — 여러 청크에 흩어진 근거를 잇는 추론 과제
