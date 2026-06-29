---
type: Method
title: GRAG
description: 개별 문서 대신 텍스트 부분그래프(subgraph)를 검색하고 그 위상 정보를 LLM 생성에 통합하는 그래프 기반 RAG 기법(Hu et al., 2024).
tags: [graphrag, retrieval, subgraph, gnn, multi-hop]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2405.16506
authors: [Yuntong Hu, Zhihan Lei, Zheng Zhang, Bo Pan, Chen Ling, Liang Zhao]
year: 2024
venue: "Findings of NAACL 2025"
arxiv: "2405.16506"
---

# GRAG

GRAG(Graph Retrieval-Augmented Generation)는 개별 문서 단위로 검색하는 기존 [RAG](../concepts/retrieval-augmented-generation.md)의 한계를 보완하기 위해, 질의와 관련된 텍스트 부분그래프(subgraph)를 검색하고 그 위상(topology) 정보를 [LLM](../concepts/large-language-model.md) 생성 과정에 함께 주입하는 [GraphRAG](../concepts/graph-rag.md) 계열 기법이다. Hu et al.(2024)이 제안했으며 Findings of NAACL 2025에 게재되었다. 인용 그래프나 [지식 그래프](../concepts/knowledge-graph.md)처럼 문서들이 서로 연결된 환경에서, 개별 노드만이 아니라 구조 자체를 활용하는 데 초점을 둔다.

## 개요

기존 RAG는 검색 단계에서 문서를 독립적으로 다루기 때문에 인용 그래프, 소셜 미디어, 지식 그래프와 같이 연결된 문서(networked documents)를 제대로 처리하지 못한다. GRAG는 이 문제를 텍스트 부분그래프 검색 문제로 재정의하고, 검색된 부분그래프의 텍스트와 위상 정보를 함께 활용해 문맥적·사실적으로 일관된 응답을 생성하는 것을 목표로 한다.

## 핵심 아이디어 / 동작 방식

GRAG는 두 단계로 동작한다. 첫째, [부분그래프 추출](../techniques/subgraph-extraction.md)을 분할 정복(divide-and-conquer) 전략으로 수행해 선형 시간에 가까운 비용으로 질의와 가장 관련성 높은 부분그래프 구조를 찾는다. 둘째, 검색된 텍스트 그래프를 텍스트 뷰(text view)와 그래프 뷰(graph view)라는 두 가지 상보적 관점으로 LLM에 제공한다. 그래프 뷰는 [GNN](../techniques/graph-neural-network.md)으로 위상 정보를 인코딩하고, 텍스트 뷰는 부분그래프를 언어화하여 함께 입력함으로써 모델이 그래프 문맥을 더 효과적으로 이해하도록 돕는다.

## 기여

- 검색 대상을 개별 엔티티가 아닌 부분그래프 구조로 확장하고, 이를 선형 시간에 가깝게 찾는 추출 절차를 제시했다.
- 텍스트 뷰와 그래프 뷰를 결합한 그래프 문맥 인식 생성(graph context-aware generation) 방식을 통해 위상 정보를 LLM 생성에 통합했다.
- 멀티홉([멀티홉 추론](../concepts/multi-hop-reasoning.md)) 그래프 추론 과제에서 위상 인식이 응답 일관성에 기여함을 보였다.

## 강점과 한계

강점은 개별 노드 중심 검색이 놓치는 연결 구조를 보존하여 [환각](../concepts/hallucination.md)을 줄이고 멀티홉 질의에 강하다는 점이다. 한계로는 텍스트 속성을 가진 그래프가 사전에 존재해야 하며, 그래프 뷰를 위한 GNN 인코더 학습이 필요해 그래프가 없는 일반 코퍼스에는 곧바로 적용하기 어렵다.

## 관련 항목

- [GraphRAG (패러다임)](../concepts/graph-rag.md) — GRAG가 속한 상위 패러다임
- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md) — GRAG가 확장·보완하는 기반 방법
- [G-Retriever](g-retriever.md) — 텍스트 속성 그래프에서 부분그래프를 검색해 LLM에 결합하는 유사 접근
- [SubgraphRAG](subgraphrag.md) — 부분그래프 검색을 핵심으로 삼는 또 다른 KG 기반 RAG
- [GNN-RAG](gnn-rag.md) — GNN으로 그래프 정보를 검색·추론에 결합하는 관련 기법
- [Subgraph Extraction](../techniques/subgraph-extraction.md) — GRAG 검색 단계의 핵심 기술
- [Graph Neural Network (GNN)](../techniques/graph-neural-network.md) — 그래프 뷰 인코딩에 사용되는 구성 요소
- [Graph RAG: A Survey (Peng et al.)](../surveys/graph-rag-survey.md) — GRAG를 포함한 GraphRAG 기법들을 정리한 서베이

## 참고문헌

- Hu, Y., Lei, Z., Zhang, Z., Pan, B., Ling, C., & Zhao, L. (2024). *GRAG: Graph Retrieval-Augmented Generation*. Findings of NAACL 2025. arXiv:2405.16506 — https://arxiv.org/abs/2405.16506
