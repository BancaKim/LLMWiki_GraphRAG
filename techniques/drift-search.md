---
type: Technique
title: DRIFT Search
description: 전역 검색의 커뮤니티 요약과 국소 검색의 엔터티 중심 탐색을 결합해, 광범위한 개관에서 출발하여 후속 질문으로 세부를 파고드는 Microsoft GraphRAG의 반복적 질의 기법이다.
tags: [graphrag, retrieval, knowledge-graph, query-routing, microsoft]
timestamp: 2026-06-29
resource: https://www.microsoft.com/en-us/research/blog/introducing-drift-search-combining-global-and-local-search-methods-to-improve-quality-and-efficiency/
---

# DRIFT Search

DRIFT Search(Dynamic Reasoning and Inference with Flexible Traversal)는 [Microsoft GraphRAG](../methods/microsoft-graphrag.md)의 질의 기법으로, 전역(global) 검색과 국소(local) 검색의 특성을 하나의 흐름에 결합한 것이다. 넓은 시야의 커뮤니티 요약에서 출발해 점차 구체적인 엔터티 수준의 근거로 좁혀 들어가는 방식으로, 한 단계의 검색만으로는 답하기 어려운 복합 질의를 다룬다. 2024년 Microsoft Research 블로그를 통해 소개되었다.

## 개념

[국소 대 전역 검색 (Local vs Global Search)](local-and-global-search.md)은 서로 다른 질의 유형에 강점을 갖는다. 전역 검색은 말뭉치 전반의 주제를 다루는 sensemaking 질문에 좋지만 특정 사실을 놓치기 쉽고, 국소 검색은 특정 엔터티에 대한 정밀한 답에 강하지만 시작점이 좁다. DRIFT는 이 둘을 순차적으로 엮어, 전역적 맥락으로 검색의 폭을 넓힌 뒤 국소적 탐색으로 깊이를 더한다.

## 동작 방식

먼저 'Primer' 단계에서 사용자 질의를 의미적으로 가장 가까운 상위 K개의 [커뮤니티 요약 (Community Summarization)](community-summarization.md) 보고서와 비교하여, 대략적인 초기 답변과 함께 탐색을 이끌 후속 질문(follow-up question)들을 생성한다. 이어지는 단계에서는 각 후속 질문에 대해 엔터티와 인접 관계, 연결된 원문을 끌어오는 국소 검색을 수행하고, 그 결과가 다시 새로운 후속 질문을 낳는 반복(iterative) 구조를 이룬다. 마지막으로 누적된 중간 답변들을 계층적으로 종합해 최종 응답을 만든다. 이는 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md)을 그래프 위에서 동적으로 펼치는 과정에 해당한다.

## GraphRAG에서의 활용

DRIFT Search는 [microsoft/graphrag](../tools/microsoft-graphrag-library.md) 라이브러리에 국소·전역 검색과 나란히 제공되는 질의 모드다. 국소 검색의 출발점에 커뮤니티 정보를 주입함으로써 더 다양한 사실을 끌어와 답변의 폭과 정확성을 함께 높이려는 것이 핵심이며, 근거에 기반한 검색으로 [환각 (Hallucination)](../concepts/hallucination.md)을 억제하는 데도 기여한다. 다만 반복 검색에 따른 LLM 호출 비용은 단일 단계 검색보다 크다.

## 관련 항목
- [Local vs Global Search](local-and-global-search.md) — DRIFT가 결합하는 두 가지 기본 검색 전략.
- [Microsoft GraphRAG](../methods/microsoft-graphrag.md) — DRIFT Search를 도입하고 제공하는 기법.
- [Community Summarization](community-summarization.md) — Primer 단계가 비교 대상으로 삼는 전역 요약 자산.
- [microsoft/graphrag (library)](../tools/microsoft-graphrag-library.md) — DRIFT 질의 모드를 구현한 오픈소스 라이브러리.
- [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md) — 후속 질문으로 단계를 이어가는 반복 검색이 수행하는 추론.
- [Query-Focused Summarization (QFS)](../concepts/query-focused-summarization.md) — 전역 측면이 다루는 요약 기반 질의 과제.
- [Hybrid Retrieval](hybrid-retrieval.md) — 서로 다른 검색 방식을 결합한다는 점에서 맞닿은 기술.
- [LazyGraphRAG](../methods/lazygraphrag.md) — 검색 시점에 비용을 조정하는 GraphRAG 계열의 또 다른 변형.
