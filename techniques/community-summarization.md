---
type: Technique
title: Community Summarization
description: 그래프에서 탐지된 계층적 커뮤니티마다 LLM으로 '보고서'를 사전 생성하고, 이 요약들을 맵리듀스로 결합해 전역적 질의에 답하는 GraphRAG의 색인·검색 기술이다.
tags: [graphrag, community-detection, query-focused-summarization, map-reduce, retrieval]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2404.16130
---

# Community Summarization

커뮤니티 요약(Community Summarization)은 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)에서 탐지된 각 커뮤니티(밀집 연결된 엔터티 군집)에 대해 [LLM (Large Language Model)](../concepts/large-language-model.md)으로 자연어 '보고서(community report)'를 생성하는 기술이다. [Microsoft GraphRAG](../methods/microsoft-graphrag.md)가 도입한 핵심 색인 단계로, 개별 [청크 (Text Chunking)](../concepts/text-chunking.md)에는 답이 흩어져 있어 잘 풀리지 않는 전역적(global) sensemaking 질문을 '요약의 요약'으로 답하기 위한 토대를 만든다.

## 개념

목표는 말뭉치를 여러 일반화 수준에서 질의할 수 있는 계층적 색인을 사전에 구축하는 것이다. [커뮤니티 탐지 (Community Detection)](community-detection.md)로 얻은 군집은 보통 여러 층위의 [계층적 클러스터링 (Hierarchical Clustering)](hierarchical-clustering.md) 구조를 이루며, 하위 층은 좁은 주제를, 상위 층은 넓은 주제를 담는다. 각 층의 커뮤니티마다 그 안의 엔터티·관계·근거를 요약한 보고서가 미리 만들어지므로, 질의 시점에 원문 전체를 다시 읽지 않고도 적절한 추상화 수준의 요약을 검색할 수 있다.

## 동작 방식

색인 단계에서 LLM은 각 커뮤니티의 노드·엣지 설명을 입력받아 보고서를 작성한다. 한 커뮤니티가 너무 커서 컨텍스트 창을 넘을 때는 하위 커뮤니티 요약을 먼저 만들고 이를 다시 묶어 상위 요약을 생성하는, 일종의 [맵리듀스(map-reduce)] 방식으로 처리한다. 질의 시점(global search)에는 선택된 커뮤니티 요약마다 부분 답변을 병렬로 생성하는 map 단계와, 이 부분 답변들을 점수에 따라 결합해 최종 응답을 만드는 reduce 단계가 이어진다. 이는 본질적으로 [Query-Focused Summarization (QFS)](../concepts/query-focused-summarization.md) 과제를 그래프 구조 위에서 수행하는 것이다.

## GraphRAG에서의 활용

커뮤니티 요약은 [Microsoft GraphRAG](../methods/microsoft-graphrag.md)의 [국소 대 전역 검색 (Local vs Global Search)](local-and-global-search.md)에서 전역 검색을 떠받치는 자산으로, 단순 벡터-RAG가 놓치는 데이터셋 전반의 주제를 포괄적으로 답하게 한다. 사전 요약이 근거에 기반하므로 [환각 (Hallucination)](../concepts/hallucination.md)을 줄이는 효과도 있다. 다만 모든 커뮤니티를 미리 요약하는 비용이 크기 때문에, [LazyGraphRAG](../methods/lazygraphrag.md)는 이 요약을 질의 시점으로 지연시켜 색인 비용을 낮추는 대안을 제시했다.

## 관련 항목
- [Community Detection (Leiden)](community-detection.md) — 요약 대상이 되는 커뮤니티를 만들어 내는 선행 단계.
- [Hierarchical Clustering](hierarchical-clustering.md) — 여러 추상화 수준의 보고서를 가능하게 하는 군집 구조.
- [Microsoft GraphRAG](../methods/microsoft-graphrag.md) — 이 기술을 도입하고 의존하는 대표 기법.
- [Local vs Global Search](local-and-global-search.md) — 커뮤니티 요약을 전역 질의에 활용하는 검색 전략.
- [Query-Focused Summarization (QFS)](../concepts/query-focused-summarization.md) — 전역 질의가 본질적으로 해당하는 과제 정의.
- [LazyGraphRAG](../methods/lazygraphrag.md) — 전수 요약 비용을 줄이려 요약을 지연시킨 후속 연구.
- [Knowledge Graph Construction](knowledge-graph-construction.md) — 커뮤니티 요약이 얹히는 그래프 색인을 만드는 과정.
- [RAPTOR](../methods/raptor.md) — 재귀적 요약 트리로 다단 추상화를 구성하는 유사 접근.
