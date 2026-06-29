---
type: Technique
title: Personalized PageRank
description: 시드 노드 집합에서 출발하는 랜덤 워크의 정상 분포로 그래프 노드를 랭킹하는 PageRank 변형으로, HippoRAG 등 GraphRAG 기법에서 질의에 정박한 시드로부터 구절·노드를 점수화하는 데 쓰인다.
tags: [graphrag, retrieval, knowledge-graph, personalized-pagerank, graph-algorithm]
timestamp: 2026-06-29
resource: https://www.cs.princeton.edu/~chazelle/courses/BIB/pagerank.htm
---

# Personalized PageRank

Personalized PageRank(PPR, 개인화 페이지랭크)는 고전적인 PageRank 알고리즘을 일반화한 그래프 랭킹 기법이다. 표준 PageRank가 그래프 전체에 균일하게 분포된 "순간이동(teleport)" 분포를 가정하는 반면, PPR은 이 순간이동 분포를 특정 시드 노드 집합에 집중시킨다. 그 결과 산출되는 점수는 시드 노드와의 그래프상 근접성과 연결 구조를 함께 반영하므로, 질의에 관련된 노드를 시드로 삼으면 그래프 전파를 통해 관련 노드·구절을 랭킹할 수 있다.

## 개념

PageRank는 그래프 위 랜덤 워크의 정상 분포(stationary distribution)로 노드 중요도를 정의한다. 매 단계에서 워커는 확률 (1−α)로 인접 노드로 이동하고, 확률 α로 순간이동 분포에 따라 임의의 노드로 점프한다. PPR은 이 순간이동 분포를 균일 분포 대신 시드 노드에 질량을 둔 분포로 바꾼 것이다. 따라서 점수는 시드에서 가깝고 잘 연결된 노드일수록 높아져, 시드를 중심으로 한 "국소적 중요도"를 측정하는 셈이 된다. 이는 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md) 위에서 특정 질의 맥락에 정박한 랭킹을 만들 때 유용하다.

## 동작 방식

PPR은 보통 점수 벡터를 반복적으로 갱신하는 멱법(power iteration)으로 계산한다. 시드 분포에서 출발해, 각 반복마다 현재 점수를 인접 노드로 전파하고 감쇠 계수(α)만큼을 시드 쪽으로 되돌리는 과정을 수렴할 때까지 반복한다. 시드를 어디에 두느냐에 따라 결과가 완전히 달라지므로, 동일한 그래프라도 질의마다 다른 랭킹을 얻을 수 있다. 노드 점수가 정해지면, 각 노드를 포함하는 구절이나 문서로 점수를 합산·전이해 검색 결과를 정렬하는 데 활용한다.

## GraphRAG에서의 활용

[GraphRAG (the paradigm)](../concepts/graph-rag.md)에서 PPR은 그래프 기반 검색의 핵심 랭킹 장치로 쓰인다. 대표적으로 [HippoRAG](../methods/hipporag.md)는 코퍼스로부터 만든 지식 그래프 위에서, [LLM](../concepts/large-language-model.md)이 질의에서 식별한 개체를 시드로 삼아 PPR을 실행하고, 그래프 전파로 여러 문서에 흩어진 근거를 한 번의 검색 단계로 모은다. 이 방식은 반복적인 [밀집 검색 (Dense Retrieval)](../concepts/dense-retrieval.md) 없이도 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md)에 필요한 연결된 근거를 가져온다는 점에서, 구절을 독립적으로 가져오는 표준 검색과 구별된다. 후속작인 [HippoRAG 2](../methods/hipporag-2.md)도 동일한 PPR 전파를 검색의 토대로 삼는다.

## 관련 항목
- [HippoRAG](../methods/hipporag.md) — 질의 개체를 시드로 PPR을 실행해 단일 단계 멀티홉 검색을 수행하는 대표 기법.
- [HippoRAG 2](../methods/hipporag-2.md) — PPR 전파를 더 깊은 구절 통합과 함께 확장한 후속 기법.
- [Knowledge Graph](../concepts/knowledge-graph.md) — PPR 전파가 이루어지는 그래프 구조.
- [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md) — PPR 기반 검색이 한 단계로 다루려는 추론 유형.
- [Dense Retrieval / Vector Search](../concepts/dense-retrieval.md) — PPR 검색과 대비되는, 구절을 독립적으로 가져오는 표준 검색.
- [Graph Traversal Reasoning](graph-traversal-reasoning.md) — 그래프 위 전파·탐색으로 근거를 모으는 관련 기법군.
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — PPR을 검색 랭킹에 활용하는 상위 패러다임.

## 참고문헌
- Haveliwala, T. H. (2002). *Topic-Sensitive PageRank*. Proceedings of WWW 2002.
- Page, L., Brin, S., Motwani, R., & Winograd, T. (1999). *The PageRank Citation Ranking: Bringing Order to the Web*. Stanford InfoLab.
