---
type: Method
title: MedGraphRAG
description: 의료 도메인을 위한 GraphRAG 프레임워크로, 삼중 그래프 구성(Triple Graph Construction)과 U-retrieval을 통해 LLM이 근거 기반의 안전한 의료 응답을 생성하도록 돕는다.
tags: [graphrag, retrieval, knowledge-graph, medical, hallucination]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2408.04187
authors: [Junde Wu, Jiayuan Zhu, Yunli Qi, Jingkun Chen, Min Xu, Filippo Menolascina, Vicente Grau]
year: 2024
venue: ACL 2025
arxiv: "2408.04187"
---

# MedGraphRAG

MedGraphRAG는 의료 도메인에 특화된 [GraphRAG](../concepts/graph-rag.md) 프레임워크로, [LLM](../concepts/large-language-model.md)이 사적인 의료 문서를 다룰 때 근거에 기반한 안전하고 신뢰할 수 있는 응답을 생성하도록 설계되었다. 핵심은 삼중 그래프 구성(Triple Graph Construction)과 U-retrieval이라는 두 기법으로, 사용자 문서를 검증된 의료 출처 및 표준 용어 체계와 연결한다. Wu et al.(2024)이 제안했으며 ACL 2025에 게재되었다.

## 개요

일반 [RAG](../concepts/retrieval-augmented-generation.md)는 의료처럼 정확성과 출처 추적이 중요한 분야에서 [환각](../concepts/hallucination.md)과 근거 부족 문제를 겪는다. MedGraphRAG는 세 계층의 데이터를 다룬다. 최하위는 UMLS 같은 사전 수준의 표준 용어 체계, 중간은 의학 논문·교과서 같은 권위 있는 문헌, 최상위는 MIMIC-IV 같은 사용자별 임상 문서다. 이 계층들을 [지식 그래프](../concepts/knowledge-graph.md)로 구성하고 서로 연결해 응답의 근거를 추적할 수 있게 한다.

## 핵심 아이디어 / 동작 방식

문서는 의미 기반으로 [청킹](../concepts/text-chunking.md)된 뒤 [개체·관계 추출](../techniques/entity-relationship-extraction.md)을 거쳐 그래프로 변환된다. 삼중 그래프 구성은 사용자 문서의 개체를 상위 계층의 의료 문헌, 그리고 표준 용어 사전과 삼중으로 연결하는 구조를 만든다. 검색 단계의 U-retrieval은 상위 요약에서 시작해 정밀한 노드로 좁혀가는 하향식(top-down) 검색과, 검색된 근거를 다시 위로 종합하는 상향식(bottom-up) 응답 정제를 결합한다. 이를 통해 전역 맥락과 정밀한 인덱싱을 함께 활용한다.

## 기여

- 의료 데이터의 신뢰도에 따라 계층을 나눈 삼중 그래프 구성 방식을 제시했다.
- 전역 맥락과 정밀 검색을 절충하는 U-retrieval 검색 메커니즘을 도입했다.
- 표준 용어 체계와의 연결로 생성된 응답의 출처 추적과 근거 제시를 가능하게 했다.

## 강점과 한계

강점은 응답이 검증된 출처에 연결되어 [환각](../concepts/hallucination.md)을 줄이고 안전성과 설명 가능성을 높인다는 점이다. 또한 [멀티홉 추론](../concepts/multi-hop-reasoning.md)이 필요한 의료 질의에서 계층 간 연결을 활용할 수 있다. 한계로는 그래프 구성과 다계층 연결에 따른 구축 비용, 그리고 UMLS·의학 문헌 같은 도메인 자원에 대한 의존성이 있어 의료 외 영역으로의 일반화가 제한된다는 점이 있다.

## 관련 항목

- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — MedGraphRAG가 속하는 상위 패러다임
- [Microsoft GraphRAG](microsoft-graphrag.md) — 계층적 그래프와 요약 기반 검색을 공유하는 대표 시스템
- [LightRAG](lightrag.md) — 그래프 기반 인덱싱과 이중 검색을 결합한 유사 방법
- [HippoRAG](hipporag.md) — 지식 그래프 위 검색으로 멀티홉 추론을 지원하는 방법
- [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md) — 삼중 그래프 구성의 기반 표현
- [Hallucination (환각)](../concepts/hallucination.md) — MedGraphRAG가 완화하려는 핵심 문제
- [Neo4j](../tools/neo4j.md) — 구현에서 그래프 저장에 사용하는 도구
- [Entity & Relationship Extraction](../techniques/entity-relationship-extraction.md) — 문서를 그래프로 변환하는 단계

## 참고문헌

- Wu, J., Zhu, J., Qi, Y., Chen, J., Xu, M., Menolascina, F., & Grau, V. (2024). *Medical Graph RAG: Towards Safe Medical Large Language Model via Graph Retrieval-Augmented Generation*. ACL 2025. arXiv:2408.04187 — https://arxiv.org/abs/2408.04187
