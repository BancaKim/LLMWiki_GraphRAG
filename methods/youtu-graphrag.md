---
type: Method
title: Youtu-GraphRAG
description: Youtu-GraphRAG는 그래프 스키마 설계·구축·검색·추론을 공통 스키마를 매개로 하나의 에이전트 체계로 수직 통합하여, 복잡한 다단계 질의에 대한 그래프 검색 증강 추론을 일관되게 수행하는 프레임워크다.
tags: [graphrag, retrieval, knowledge-graph, multi-hop-reasoning, agentic, complex-reasoning]
authors: [Junnan Dong, Siyu An, Yifei Yu, Qian-Wen Zhang, Linhao Luo, Xiao Huang, Yunsheng Wu, Di Yin, Xing Sun]
year: 2025
venue: arXiv preprint (Tencent)
arxiv: "2508.19855"
resource: https://arxiv.org/abs/2508.19855
timestamp: 2026-07-23
---

# Youtu-GraphRAG

Youtu-GraphRAG는 그래프 스키마 설계, 그래프 구축, 검색, 추론이라는 파이프라인 전 단계를 하나의 에이전트 체계로 '수직 통합(vertically unified)'한 [GraphRAG](../concepts/graph-rag.md) 프레임워크다. 기존 연구가 그래프 구축이나 검색을 개별적으로 최적화해 도메인이 바뀔 때 성능이 저하되던 문제를, 공통의 그래프 스키마를 매개로 각 단계를 긴밀히 연결해 해결하려 한다. Tencent Youtu Lab의 Dong 등(2025)이 제안했으며, 복잡한 다단계 질의에 대한 검색 증강 추론(complex reasoning)을 표적으로 한다.

## 개요

그래프 스키마·구축·검색·추론을 서로 다른 목표로 따로 튜닝하면 각 구성 요소의 국소 최적이 전체 성능으로 이어지지 않고, 특히 미지의 도메인으로 이동할 때 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)의 구조와 검색 전략이 어긋난다. Youtu-GraphRAG는 이 단계들을 하나의 수직 축으로 묶어, [Knowledge Graph QA (KGQA)](../concepts/knowledge-graph-question-answering.md) 같은 [멀티홉 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md) 질의를 일관된 스키마 위에서 처리하는 것을 목표로 한다.

## 핵심 아이디어

시드 그래프 스키마가 자동 추출 에이전트에 대상 엔터티·관계·속성 유형을 제한해 [그래프 구축 (Knowledge Graph Construction)](../techniques/knowledge-graph-construction.md)을 안내하고, 미지의 도메인에서는 스키마를 점진적으로 확장한다. 구축된 지식은 하향식 필터링과 상향식 추론을 함께 지원하는 계층적 지식 트리(커뮤니티 요약 포함)로 조직되며, 에이전트형 검색기가 동일한 스키마를 해석해 복잡한 질의를 병렬 처리 가능한 하위 질의로 분해한다. 이렇게 구축·검색·추론이 같은 스키마를 공유함으로써 단계 간 정합이 유지된다.

## 기여

- 그래프 스키마를 매개로 구축·검색·추론을 하나로 잇는 수직 통합 에이전트 프레임워크를 제시했다.
- 시드 스키마로 추출 에이전트를 제약하고 미지 도메인에서 확장하는 방식과, 상·하향 추론을 함께 지원하는 계층적 지식 트리를 설계했다.
- 복잡한 질의를 병렬 하위 질의로 분해하는 에이전트 검색기로, 기존 SOTA 대비 토큰 비용을 낮추면서 정확도를 높였다고 보고한다.

## 강점과 한계

강점은 도메인 이동에 상대적으로 강건하고, 스키마 공유로 파이프라인 전체의 정합이 유지되며, 병렬 하위 질의로 비용 효율과 정확도를 함께 개선한다는 점이다. 반면 시드 스키마 설계와 계층적 트리 구성에 사전 설계 부담이 있고, 여러 에이전트 단계를 거치므로 구현 복잡도가 높으며, 성능이 스키마 확장과 추출 에이전트의 품질에 좌우된다.

## 관련 항목

- [Microsoft GraphRAG](microsoft-graphrag.md) — 계층적 커뮤니티 요약으로 그래프를 색인하는 선행 방법
- [Think-on-Graph 2.0](think-on-graph-2.md) — 에이전트형 그래프 검색을 반복 수행하는 비교 대상
- [Reasoning on Graphs (RoG)](reasoning-on-graphs.md) — 공저자 Linhao Luo가 참여한 관련 KG 기반 추론 방법
- [Graph Traversal Reasoning](../techniques/graph-traversal-reasoning.md) — 그래프 위 다단계 탐색의 핵심 메커니즘
- [Community Detection (Leiden)](../techniques/community-detection.md) — 계층적 지식 트리와 커뮤니티 요약에 쓰이는 기법
- [Knowledge Graph QA (KGQA)](../concepts/knowledge-graph-question-answering.md) — 이 프레임워크가 겨냥하는 대표 과제
- [Graph RAG: A Survey (Peng et al.)](../surveys/graph-rag-survey.md) — Youtu-GraphRAG를 더 넓은 지형 속에 위치시킨다

## 참고문헌

- Dong, J., An, S., Yu, Y., Zhang, Q.-W., Luo, L., Huang, X., Wu, Y., Yin, D., & Sun, X. (2025). *Youtu-GraphRAG: Vertically Unified Agents for Graph Retrieval-Augmented Complex Reasoning*. arXiv preprint (Tencent Youtu Lab). arXiv:2508.19855 — https://arxiv.org/abs/2508.19855
