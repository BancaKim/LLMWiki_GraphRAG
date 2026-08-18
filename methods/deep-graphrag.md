---
type: Method
title: Deep GraphRAG
description: 전역 검색의 포괄성과 지역 검색의 효율성 사이의 상충을 계층적 global-to-local 3단계 검색으로 절충하고, DW-GRPO 강화학습으로 소형 LLM이 지식 통합을 담당하도록 한 GraphRAG 기법이다.
tags: [graphrag, retrieval, community-detection, reinforcement-learning, hierarchical-retrieval]
authors: [Yuejie Li, Ke Yang, Tao Wang, Bolin Chen, Bowen Li, Chengjun Mao]
year: 2026
venue: arXiv preprint
arxiv: "2601.11144"
resource: https://arxiv.org/abs/2601.11144
timestamp: 2026-08-18
---

# Deep GraphRAG

Deep GraphRAG는 [GraphRAG (the paradigm)](../concepts/graph-rag.md)에서 오래 지적되어 온 **전역 검색과 지역 검색의 상충**을 정면으로 다루는 기법이다. 전역(global) 검색은 코퍼스를 폭넓게 포괄하지만 비용이 크고, 지역(local) 검색은 효율적이지만 흩어진 근거를 놓치기 쉽다. 이 논문은 둘을 양자택일하는 대신 **계층적 global-to-local 검색**으로 단계적으로 좁혀 가고, 지식 통합 단계를 소형 [LLM](../concepts/large-language-model.md)에 맡겨 강화학습으로 훈련한다.

## 개요

[Microsoft GraphRAG](microsoft-graphrag.md) 계열은 [커뮤니티 요약 (Community Summarization)](../techniques/community-summarization.md)을 전수 생성해 전역 질의에 답하지만 색인·질의 비용이 크고, 지역 검색은 특정 엔터티 주변에 갇힌다. Deep GraphRAG는 이 [Local vs Global Search](../techniques/local-and-global-search.md) 구분을 고정된 두 모드가 아니라 **거시적 커뮤니티 간(inter-community) 관계와 미시적 커뮤니티 내(intra-community) 관계를 잇는 하나의 연속된 축**으로 재구성한다.

## 핵심 아이디어

검색은 세 단계로 진행된다. 첫째 **커뮤니티 간 필터링**으로, 지역 맥락을 이용해 탐색 공간 자체를 먼저 쳐낸다. 둘째 **커뮤니티 수준 정제**로, 엔터티 상호작용 분석을 통해 관련성 높은 [부분 그래프 (Subgraph Extraction)](../techniques/subgraph-extraction.md)에 우선순위를 부여한다. 셋째 표적 커뮤니티 안에서 **엔터티 수준의 세밀한 검색**을 수행한다. 이 과정 전반을 **빔 서치(beam search) 기반 동적 재순위화 모듈**이 이끌며 후보를 계속 걸러 효율과 전역 포괄성의 균형을 맞춘다.

검색된 근거는 별도의 **지식 통합 모듈(Knowledge Integration Module)** 이 정리하는데, 여기에 소형 LLM을 쓰고 **DW-GRPO(Dynamic Weighting Reward GRPO)** 로 학습한다. 이는 관련성(relevance)·충실성(faithfulness)·간결성(conciseness) 세 목표의 보상 가중치를 동적으로 조정하는 강화학습 기법이다.

## 기여

- 전역·지역을 단계적으로 잇는 계층적 global-to-local 3단계 검색 파이프라인을 제안했다.
- 빔 서치로 최적화한 동적 재순위화로 후보 집합을 지속적으로 축소하는 구조를 설계했다.
- 보상 가중치를 동적으로 조정하는 DW-GRPO를 도입해, **1.5B 규모의 소형 모델이 72B 베이스라인과 견줄 만한 성능**을 내도록 했다.
- Natural Questions와 [HotpotQA](../benchmarks/hotpotqa.md)에서 검색 정확도와 효율 양쪽의 향상을 보고했다.

## 강점과 한계

강점은 전역 포괄성을 상당 부분 유지하면서 탐색 공간을 조기에 줄여 비용을 낮춘다는 점, 그리고 소형 모델로 통합 단계를 처리해 운영 부담을 줄인다는 점이다. 한계로는 커뮤니티 구조에 의존하므로 [커뮤니티 탐지 (Community Detection)](../techniques/community-detection.md) 품질이 성능을 좌우하고, 3단계 파이프라인과 재순위화가 도입하는 하이퍼파라미터가 늘어나며, DW-GRPO를 위한 강화학습 훈련이 별도로 필요해 곧바로 적용하기는 어렵다는 점을 들 수 있다.

## 관련 항목

- [Local vs Global Search](../techniques/local-and-global-search.md) — 이 기법이 절충하려는 바로 그 구분이다.
- [DRIFT Search](../techniques/drift-search.md) — 지역과 전역을 섞는다는 문제의식을 공유하는 Microsoft 측 접근이다.
- [Microsoft GraphRAG](microsoft-graphrag.md) — 커뮤니티 요약 기반 전역 검색의 대표 비교 대상이다.
- [Community Detection (Leiden)](../techniques/community-detection.md) — 계층적 검색이 전제로 삼는 커뮤니티 구조를 만드는 기법이다.
- [Hierarchical Clustering](../techniques/hierarchical-clustering.md) — 계층을 따라 좁혀 가는 검색의 배경 기법이다.
- [LazyGraphRAG](lazygraphrag.md) — 전역 요약 비용을 줄이려는 다른 노선의 대안이다.
- [MiniRAG](minirag.md) — 소형 모델로 그래프 RAG를 돌린다는 목표를 공유한다.
- [LinearRAG](linearrag.md) — 색인 쪽에서 비용을 낮추는 상보적 접근이다.

## 참고문헌

- Li, Y., Yang, K., Wang, T., Chen, B., Li, B., & Mao, C. (2026). *Deep GraphRAG: A Balanced Approach to Hierarchical Retrieval and Adaptive Integration*. arXiv preprint. arXiv:2601.11144 — https://arxiv.org/abs/2601.11144
