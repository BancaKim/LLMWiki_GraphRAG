---
type: Concept
title: "지식 그래프 (Knowledge Graph)"
description: 개체(entity)를 노드로, 개체 사이의 관계(relation)를 엣지로 표현하고 사실을 (주어, 술어, 목적어) 트리플로 저장하는 그래프 형태의 구조화된 지식 표현 방식이다.
tags: [knowledge-graph, graphrag, retrieval, ontology, multi-hop-reasoning]
timestamp: 2026-06-29
---

# Knowledge Graph

지식 그래프(KG, Knowledge Graph)는 현실 세계의 사실을 그래프 구조로 표현한 지식 베이스이다. 개체(entity)를 노드로, 개체 사이의 관계(relation)를 엣지로 나타내며, 각 사실은 (주어, 술어, 목적어) 형태의 트리플(triple)로 저장된다. 이렇게 명시적이고 구조화된 표현 덕분에 사실을 검색·연결·검증하기 쉽고, [GraphRAG (the paradigm)](graph-rag.md)에서 [Large Language Model (LLM)](large-language-model.md)의 출력을 외부 사실에 근거시키는 토대가 된다.

## 정의

KG는 노드(개체)와 그 사이의 라벨이 붙은 엣지(관계)로 이루어진 방향 그래프다. 가장 기본 단위는 "Marie Curie — 수상 — 노벨물리학상"처럼 주어-술어-목적어로 구성된 트리플이며, 여러 트리플이 노드를 공유하며 연결돼 하나의 그래프를 이룬다. 어떤 유형의 개체와 관계가 허용되는지는 스키마 또는 온톨로지(ontology)가 규정하여 일관성과 추론 가능성을 보장한다. KG는 텍스트로부터 [개체·관계 추출 (Entity & Relationship Extraction)](../techniques/entity-relationship-extraction.md)과 [지식 그래프 구축 (Knowledge Graph Construction)](../techniques/knowledge-graph-construction.md)을 거쳐 만들어진다.

## GraphRAG에서 중요한 이유

KG는 사실을 분리된 [청크 (Text Chunking)](text-chunking.md)가 아니라 명시적으로 연결된 구조로 저장하므로, 답변을 검증 가능한 근거에 그라운딩(grounding)하여 [환각 (Hallucination)](hallucination.md)을 줄인다. 또한 관계 엣지를 따라 노드를 잇는 [그래프 순회 추론 (Graph Traversal Reasoning)](../techniques/graph-traversal-reasoning.md)이 가능해, 단일 구절에 답이 담겨 있지 않은 [멀티홉 추론 (Multi-hop Reasoning)](multi-hop-reasoning.md)에 특히 유리하다. 이는 표면적 유사도에만 의존하는 [밀집 검색 (Dense Retrieval)](dense-retrieval.md)이 약한 지점을 보완한다.

## 실제 활용

KG는 [지식 그래프 질의응답 (KGQA)](knowledge-graph-question-answering.md)의 핵심 자원이며, Neo4j 같은 그래프 데이터베이스에 저장돼 질의된다. GraphRAG 계열에서는 [Microsoft GraphRAG](../methods/microsoft-graphrag.md), [LightRAG](../methods/lightrag.md), [HippoRAG](../methods/hipporag.md) 등이 KG를 색인·검색 단위로 활용한다.

## 관련 항목
- [GraphRAG (the paradigm)](graph-rag.md) — KG를 검색 증강에 결합한 패러다임으로, 본 개념의 핵심 응용처.
- [Knowledge Graph Construction](../techniques/knowledge-graph-construction.md) — 텍스트에서 KG를 만들어 내는 과정.
- [Entity & Relationship Extraction](../techniques/entity-relationship-extraction.md) — 트리플의 개체와 관계를 추출하는 기반 기술.
- [Multi-hop Reasoning (멀티홉 추론)](multi-hop-reasoning.md) — KG의 연결 구조가 직접 지원하는 추론 유형.
- [Knowledge Graph QA (KGQA)](knowledge-graph-question-answering.md) — KG를 지식원으로 삼는 대표 과제.
- [Unifying LLMs and KGs: A Roadmap](../surveys/llm-kg-roadmap.md) — KG와 LLM의 통합을 정리한 서베이.
- [Neo4j](../tools/neo4j.md) — KG를 저장·질의하는 대표 그래프 데이터베이스.
- [Hallucination (환각)](hallucination.md) — KG 그라운딩이 완화하려는 LLM의 문제.
