---
type: Technique
title: Local vs Global Search
description: Microsoft GraphRAG의 두 가지 질의 모드로, 지역(local) 검색은 특정 엔터티 주변의 이웃과 근거를 모아 답하고, 전역(global) 검색은 커뮤니티 보고서를 맵리듀스로 결합해 말뭉치 전반을 아우르는 질문에 답한다.
tags: [graphrag, retrieval, query-focused-summarization, map-reduce, knowledge-graph]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2404.16130
---

# Local vs Global Search

지역 검색과 전역 검색(Local vs Global Search)은 [Microsoft GraphRAG](../methods/microsoft-graphrag.md)가 제공하는 두 가지 질의 모드다. 지역 검색은 질문에 관련된 특정 엔터티를 출발점으로 그 주변 정보를 모아 답하고, 전역 검색은 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)에서 미리 생성된 커뮤니티 보고서들을 맵리듀스로 결합해 답한다. 어떤 모드를 쓰느냐는 질문이 좁은 사실을 묻는지, 아니면 데이터셋 전반의 주제를 묻는지에 달려 있다.

## 개념

지역 검색은 답이 그래프의 한정된 영역에 모여 있는 구체적 질문("X는 누구이며 무엇과 관련되는가")에 적합하다. 반면 전역 검색은 답이 말뭉치 전체에 흩어져 있어 단순 [Dense Retrieval / Vector Search](../concepts/dense-retrieval.md)로는 포착하기 어려운, 본질적으로 [Query-Focused Summarization (QFS)](../concepts/query-focused-summarization.md)형 질문("이 자료 전체의 핵심 주제는 무엇인가")을 겨냥한다. 두 모드는 같은 그래프 색인 위에서 서로 다른 검색 전략을 취한다.

## 동작 방식

지역 검색은 질의를 임베딩해 관련 엔터티를 찾은 뒤, 그 엔터티의 이웃 노드·관계, 연결된 [Community Summarization](community-summarization.md) 보고서, 원문 [Text Chunking (청킹)](../concepts/text-chunking.md) 조각을 함께 모아 컨텍스트 창을 채운다. 전역 검색은 [Community Detection (Leiden)](community-detection.md)으로 얻은 계층의 한 층위 보고서들을 잘게 나눠 병렬로 부분 답변과 점수를 생성하는 map 단계와, 점수가 높은 부분 답변을 모아 최종 응답을 합성하는 reduce 단계로 이루어진다.

## GraphRAG에서의 활용

두 모드는 [GraphRAG (the paradigm)](../concepts/graph-rag.md)가 개별 사실 검색과 전역적 조망을 모두 다루게 하는 핵심 인터페이스다. 지역 검색은 [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md)이 필요한 구체적 질문에, 전역 검색은 [환각 (Hallucination)](../concepts/hallucination.md)을 줄이며 포괄적 요약을 제공하는 데 쓰인다. 이후 GraphRAG는 두 방식을 동적으로 결합한 [DRIFT Search](drift-search.md)를 추가해, 질문 유형에 따라 검색 폭과 깊이를 조절한다.

## 관련 항목
- [Microsoft GraphRAG](../methods/microsoft-graphrag.md) — 두 검색 모드를 정의하고 구현한 대표 기법.
- [Community Summarization](community-summarization.md) — 전역 검색이 맵리듀스로 결합하는 보고서를 만드는 색인 단계.
- [Community Detection (Leiden)](community-detection.md) — 전역 검색의 보고서 계층을 만들어 내는 선행 단계.
- [DRIFT Search](drift-search.md) — 지역과 전역 검색을 결합한 후속 질의 전략.
- [Query-Focused Summarization (QFS)](../concepts/query-focused-summarization.md) — 전역 검색이 본질적으로 수행하는 과제.
- [Hybrid Retrieval](hybrid-retrieval.md) — 그래프와 벡터 신호를 섞는 검색으로, 지역 검색의 컨텍스트 구성과 통한다.
- [LazyGraphRAG](../methods/lazygraphrag.md) — 사전 요약 비용을 낮춰 전역 질의를 지연 처리하는 대안.
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — 지역·전역 검색을 포괄하는 상위 패러다임.
