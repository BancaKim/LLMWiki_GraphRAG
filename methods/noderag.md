---
type: Method
title: NodeRAG
description: 엔터티·의미 단위·고수준 요약·이벤트를 서로 다른 유형의 노드로 구분하는 이질적 그래프 구조로 그래프 기반 RAG를 재설계한 그래프 중심 프레임워크.
tags: [graphrag, retrieval, knowledge-graph, heterogeneous-graph, multi-hop-reasoning]
authors: [Tianyang Xu, Haojie Zheng, Chengze Li, Haoxiang Chen, Yixin Liu, Ruoxi Chen, Lichao Sun]
year: 2025
venue: arXiv preprint
arxiv: "2504.11544"
resource: https://arxiv.org/abs/2504.11544
timestamp: 2026-07-23
---

# NodeRAG

NodeRAG는 이질적(heterogeneous) 노드를 중심으로 [GraphRAG (the paradigm)](../concepts/graph-rag.md)를 재구성한 그래프 중심 프레임워크다. 엔터티, 의미 단위(semantic unit), 고수준 요약, 이벤트 등을 하나의 균일한 노드로 뭉뚱그리지 않고 서로 다른 유형의 노드로 구분한다. Xu et al.(2025)이 제안했으며, 기존 그래프 기반 RAG가 그래프 '구조 설계' 자체를 소홀히 했다는 문제의식에서 출발한다.

## 개요

많은 그래프 RAG 시스템은 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)를 검색을 위한 보조 색인 정도로만 다루어, 노드가 무엇을 표현해야 하는지에 대한 설계를 뒤로 미룬다. NodeRAG는 반대로 그래프 구조를 최우선 설계 대상으로 삼고, 이질적 노드 위에서 다양한 그래프 알고리즘이 매끄럽게 맞물리도록 인덱스를 구성한다.

## 핵심 아이디어

NodeRAG는 [Knowledge Graph Construction](../techniques/knowledge-graph-construction.md) 단계에서 원문 청크를 유형이 다른 노드들로 분해한다. 개념을 담는 엔터티 노드, 국소 사실을 담는 의미 단위 노드, 광범위한 맥락을 담는 고수준 요약 노드, 그리고 이벤트 노드가 하나의 이질적 그래프 안에 공존한다. 질의 시점에는 이 유형 구분을 활용해 [Personalized PageRank](../techniques/personalized-pagerank.md) 계열의 그래프 탐색과 벡터 검색을 결합하고, 필요한 노드만 선별해 [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md)에 필요한 근거를 최소한의 검색 토큰으로 모은다.

## 기여

- 엔터티·의미 단위·요약·이벤트를 구분하는 이질적 노드 설계를 도입해 그래프 알고리즘의 통합 지점을 명확히 했다.
- 그래프 '구조 설계'를 부차적 요소가 아니라 시스템의 일차적 설계 축으로 승격시켰다.
- [Microsoft GraphRAG](microsoft-graphrag.md), [LightRAG](lightrag.md) 대비 인덱싱·질의 시간과 저장 효율에서 우위를 보이고, 멀티홉 QA 정확도를 검색 토큰을 줄이며 향상시켰다.

## 강점과 한계

강점은 노드 유형을 세분화함으로써 불필요한 맥락을 걷어내고 검색 효율과 멀티홉 성능을 동시에 끌어올린다는 점이다. 한계로는 여러 유형의 노드를 만들고 유지하는 인덱싱 파이프라인의 복잡성, 그리고 노드 분해 품질이 여전히 LLM 추출 정확도에 의존한다는 점이 있다.

## 관련 항목
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — NodeRAG가 구조 설계 측면에서 구체화하는 상위 패러다임이다.
- [Microsoft GraphRAG](microsoft-graphrag.md) — 커뮤니티 요약을 쓰는 비교 대상 시스템이다.
- [LightRAG](lightrag.md) — 효율에 초점을 둔 또 다른 비교 대상 그래프 RAG 기법이다.
- [HippoRAG](hipporag.md) — PageRank 계열 검색을 공유하는 동시대 그래프 RAG 방법이다.
- [RAPTOR](raptor.md) — 계층적 요약 노드로 다중 수준 색인을 만드는 대조적 접근이다.
- [Knowledge Graph Construction](../techniques/knowledge-graph-construction.md) — 이질적 노드 그래프를 만드는 핵심 단계다.
- [Community Summarization](../techniques/community-summarization.md) — 고수준 요약 노드와 대비되는 요약 색인 기법이다.

## 참고문헌
- Xu, T., Zheng, H., Li, C., Chen, H., Liu, Y., Chen, R., & Sun, L. (2025). *NodeRAG: Structuring Graph-based RAG with Heterogeneous Nodes*. arXiv preprint. arXiv:2504.11544 — https://arxiv.org/abs/2504.11544
