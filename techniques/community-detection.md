---
type: Technique
title: Community Detection (Leiden)
description: 그래프를 밀접하게 연결된 노드 집합인 커뮤니티로 분할하는 기법으로, Microsoft GraphRAG는 Traag, Waltman, van Eck(2019)이 제안한 Leiden 알고리즘을 사용한다.
tags: [graphrag, community-detection, clustering, knowledge-graph, leiden]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/1810.08473
authors: [V. A. Traag, L. Waltman, N. J. van Eck]
year: 2019
venue: "Scientific Reports 9, 5233"
arxiv: "1810.08473"
---

# Community Detection (Leiden)

커뮤니티 탐지(Community Detection)는 그래프의 노드들을 내부적으로 촘촘히 연결되고 외부와는 성기게 연결된 묶음, 즉 커뮤니티로 분할하는 기법이다. [GraphRAG (the paradigm)](../concepts/graph-rag.md)에서는 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)를 의미적으로 응집된 하위 그룹으로 나누어, 전체 말뭉치를 한눈에 조망하기 어려운 전역 질의에 대비한 계층적 색인을 만드는 데 쓰인다. [Microsoft GraphRAG](../methods/microsoft-graphrag.md)는 이 단계에서 Leiden 알고리즘을 채택한다.

## 개념

커뮤니티 탐지는 보통 모듈러리티(modularity)와 같은 품질 지표를 최적화하여, 같은 커뮤니티 안의 엣지 밀도가 무작위 기대치보다 높아지도록 분할을 찾는다. 결과는 단일 분할에 그치지 않고 여러 해상도 수준에서 중첩된 계층을 이룰 수 있어, [계층적 클러스터링 (Hierarchical Clustering)](hierarchical-clustering.md)과 밀접하다. GraphRAG 맥락에서 각 커뮤니티는 하나의 주제나 사건 군을 표상하며, 이후 [커뮤니티 요약 (Community Summarization)](community-summarization.md)의 입력 단위가 된다.

## 동작 방식

Leiden 알고리즘은 널리 쓰이던 Louvain 방법을 개선한 것이다. Traag, Waltman, van Eck은 Louvain이 내부적으로 끊겨 있거나 제대로 연결되지 않은 커뮤니티를 만들어 낼 수 있음을 지적하고, Leiden이 모든 커뮤니티의 연결성을 보장하도록 설계했다. 알고리즘은 노드를 지역적으로 이동시키는 단계, 분할을 정련하는 단계, 그리고 커뮤니티를 하나의 노드로 묶어 그래프를 집계하는 단계를 반복하며, 이를 통해 다층 계층을 만들어 낸다. 이 과정은 [개체·관계 추출 (Entity & Relationship Extraction)](entity-relationship-extraction.md)으로 [지식 그래프 구축 (Knowledge Graph Construction)](knowledge-graph-construction.md)이 끝난 그래프 위에서 수행된다.

## GraphRAG에서의 활용

Microsoft GraphRAG는 인덱싱 시점에 Leiden으로 엔터티 그래프를 다층 커뮤니티로 분할하고, 각 커뮤니티에 대한 요약 보고서를 생성한다. 이렇게 만들어진 계층은 [전역·지역 검색 (Local vs Global Search)](local-and-global-search.md)에서 전역 검색의 토대가 되어, 말뭉치 전체를 아우르는 [Query-Focused Summarization (QFS)](../concepts/query-focused-summarization.md)형 질문에 답하도록 돕는다. 즉 커뮤니티 탐지는 개별 사실 검색과 전역적 조망 사이를 잇는 다리 역할을 한다.

## 관련 항목
- [Community Summarization](community-summarization.md) — 탐지된 각 커뮤니티를 요약 보고서로 변환하는 후속 단계.
- [Hierarchical Clustering](hierarchical-clustering.md) — 다층 커뮤니티 구조를 만드는 일반적 기법군.
- [Microsoft GraphRAG](../methods/microsoft-graphrag.md) — Leiden 커뮤니티 탐지를 인덱싱에 사용하는 대표 기법.
- [Local vs Global Search](local-and-global-search.md) — 커뮤니티 계층을 전역 검색에 활용하는 검색 전략.
- [Knowledge Graph Construction](knowledge-graph-construction.md) — 커뮤니티 탐지의 입력이 되는 그래프를 만드는 선행 단계.
- [Query-Focused Summarization (QFS)](../concepts/query-focused-summarization.md) — 전역 커뮤니티 요약이 겨냥하는 질의 유형.
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — 커뮤니티 탐지를 색인 단계에 포함하는 상위 패러다임.

## 참고문헌
- Traag, V. A., Waltman, L., & van Eck, N. J. (2019). *From Louvain to Leiden: guaranteeing well-connected communities*. Scientific Reports 9, 5233. arXiv:1810.08473 — https://arxiv.org/abs/1810.08473
