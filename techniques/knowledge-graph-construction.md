---
type: Technique
title: Knowledge Graph Construction
description: LLM으로 비정형 텍스트에서 개체와 관계를 추출해 노드·엣지로 연결된 KG 색인을 만드는 과정으로, GraphRAG의 인덱싱 단계에 해당한다.
tags: [graphrag, knowledge-graph, indexing, entity-extraction, retrieval]
timestamp: 2026-06-29
---

# Knowledge Graph Construction

지식 그래프 구축(Knowledge Graph Construction)은 비정형 텍스트 말뭉치를 입력으로 받아, 그 안의 개체(entity)와 개체 사이의 관계(relation)를 뽑아내 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)로 조직하는 과정이다. [GraphRAG (the paradigm)](../concepts/graph-rag.md)에서는 이 과정이 검색에 앞서 한 번 수행되는 인덱싱(색인) 단계에 해당하며, 이후 질의 시점에 검색·추론의 대상이 되는 그래프 색인을 만들어 낸다. 전통적으로는 규칙·통계 기반 파이프라인으로 수행됐으나, GraphRAG 계열에서는 주로 [Large Language Model (LLM)](../concepts/large-language-model.md)을 추출기로 사용한다.

## 개념

목표는 분리된 텍스트를 명시적으로 연결된 그래프 구조로 바꾸는 것이다. 결과물은 개체를 노드로, 관계를 라벨이 붙은 엣지로 가지며, 각 사실은 (주어, 술어, 목적어) 트리플로 표현된다. 핵심 하위 작업은 [개체·관계 추출 (Entity & Relationship Extraction)](entity-relationship-extraction.md), 같은 대상을 가리키는 노드를 합치는 개체 정규화(엔터티 해소), 그리고 그래프를 색인·저장하는 단계다. 이렇게 구축된 그래프는 [텍스트 청킹 (Text Chunking)](../concepts/text-chunking.md)만으로 얻기 어려운 사실 간 연결을 보존한다.

## 동작 방식

먼저 말뭉치를 청크 단위로 나눈 뒤, 각 청크에 대해 LLM에 프롬프트를 주어 개체와 관계 트리플을 추출한다. 추출된 노드는 표기 변이를 정규화해 병합하고, 동일 관계는 통합하여 중복을 줄인다. 일부 파이프라인은 노드·엣지에 텍스트 임베딩을 부여해 후속 [하이브리드 검색 (Hybrid Retrieval)](hybrid-retrieval.md)을 지원하고, [Microsoft GraphRAG](../methods/microsoft-graphrag.md)처럼 [커뮤니티 탐지 (Community Detection)](community-detection.md)와 [커뮤니티 요약 (Community Summarization)](community-summarization.md)을 덧붙여 계층적 색인을 형성하기도 한다. 완성된 그래프는 [Neo4j](../tools/neo4j.md) 같은 저장소에 적재된다.

## GraphRAG에서의 활용

구축된 그래프 색인은 GraphRAG의 검색 토대가 되며, 색인 품질이 이후 검색·생성 성능을 좌우한다. [HippoRAG](../methods/hipporag.md)는 이 그래프 위에서 검색을 수행하고, [LightRAG](../methods/lightrag.md)는 증분 갱신이 가능한 경량 구축을 지향한다. 명시적 연결 구조 덕분에 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md)을 지원하고 답변을 근거에 그라운딩하여 [환각 (Hallucination)](../concepts/hallucination.md)을 줄인다. 다만 LLM 기반 구축은 토큰·연산 비용이 높다는 한계가 있다.

## 관련 항목
- [Knowledge Graph](../concepts/knowledge-graph.md) — 본 과정의 산출물인 구조화된 지식 표현.
- [Entity & Relationship Extraction](entity-relationship-extraction.md) — 그래프의 노드와 엣지를 만들어 내는 핵심 하위 작업.
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — 그래프 구축을 인덱싱 단계로 삼는 상위 패러다임.
- [Microsoft GraphRAG](../methods/microsoft-graphrag.md) — LLM으로 엔터티 그래프를 구축하는 대표 기법.
- [LightRAG](../methods/lightrag.md) — 증분 갱신이 가능한 경량 그래프 구축 대안.
- [Community Detection (Leiden)](community-detection.md) — 구축된 그래프를 클러스터로 조직하는 후속 단계.
- [Neo4j](../tools/neo4j.md) — 구축된 그래프를 저장·질의하는 그래프 데이터베이스.
- [Text Chunking (청킹)](../concepts/text-chunking.md) — 추출에 앞서 입력을 분할하는 전처리 단계.
- [온톨로지 기반·뉴로심볼릭 GraphRAG](../concepts/neurosymbolic-graphrag.md) — 온톨로지를 스키마로 삼아 구축을 제약하는 접근.
- [OG-RAG](../methods/og-rag.md) — 도메인 온톨로지에 근거해 사실 묶음을 조직한 EMNLP 2025 사례.
