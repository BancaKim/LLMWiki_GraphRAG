---
type: Method
title: CLAUSE
description: 지식 그래프 위의 컨텍스트 구성을 순차적 의사결정 문제로 보고, 부분그래프 구축·경로 탐색·근거 선별을 담당하는 세 에이전트를 질의별 예산 제약 아래 강화학습으로 함께 최적화한 뉴로심볼릭 프레임워크다.
tags: [graphrag, neurosymbolic, agentic, reinforcement-learning, subgraph-extraction]
year: 2025
venue: ICLR 2026
arxiv: "2509.21035"
resource: https://arxiv.org/abs/2509.21035
timestamp: 2026-08-31
---

# CLAUSE

CLAUSE는 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md) 위에서 LLM에 넘길 컨텍스트를 만드는 일을 **순차적 의사결정 과정**으로 정식화한 [뉴로심볼릭](../concepts/neurosymbolic-graphrag.md) 프레임워크다. 무엇을 확장하고, 어떤 경로를 따라가거나 되돌아갈지, 어떤 근거를 남기고 언제 멈출지를 학습된 정책이 결정한다. ICLR 2026에 게재되었으며, "신경망이 그래프를 읽는다"에서 나아가 **심볼릭 구조 위의 탐색 자체를 학습 대상**으로 삼은 점이 특징이다.

## 개요

지식 그래프는 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md)에 좋은 구조적 컨텍스트를 주지만, 실제 서비스는 정확도뿐 아니라 지연과 비용을 함께 맞춰야 하고 근거의 출처(provenance)도 보존해야 한다. 고정된 k-홉 확장이나 "더 길게 생각하기" 식 프롬프팅은 과다 검색으로 컨텍스트를 부풀리고 실행 시간을 예측 불가능하게 만든다.

## 핵심 아이디어

세 에이전트가 역할을 나눈다. **Subgraph Architect** 는 질문에 정박한 [부분그래프 (Subgraph Extraction)](../techniques/subgraph-extraction.md)를 구성하되 답을 뒷받침하는 경로는 보존하면서 과확장을 피한다. **Path Navigator** 는 단계 예산을 지키며 추론 경로를 탐색하고 필요하면 수정한다([그래프 순회 추론 (Graph Traversal Reasoning)](../techniques/graph-traversal-reasoning.md)). **Context Curator** 는 토큰 예산 안에서 정확한 응답에 충분한 최소한의 텍스트 조각 묶음을 조립한다.

세 에이전트는 **LC-MAPPO(Lagrangian-Constrained Multi-Agent PPO)** 로 함께 학습된다. 간선 편집 수, 상호작용 단계 수, 선택 토큰 수에 대한 **질의별 자원 예산**을 라그랑주 제약으로 걸어, 부분그래프 구축·경로 발견·근거 선택이 개별 최적이 아니라 공동 최적이 되도록 한다. 지연과 프롬프트 비용이 사용자가 지정하는 예산(또는 가격)으로 노출되므로, **재학습 없이 질의 단위로** 정확도·지연·비용의 균형점을 옮길 수 있다.

## 기여

- 그래프 컨텍스트 구성을 예산 제약이 있는 순차적 의사결정 문제로 정식화했다.
- 역할이 분리된 3개 에이전트와 이를 공동 최적화하는 LC-MAPPO 알고리즘을 제안했다.
- [HotpotQA](../benchmarks/hotpotqa.md), MetaQA, FactKG에서 EM@1을 높이면서 부분그래프 증가량과 종단 지연을 함께 줄였다. MetaQA 2-hop에서는 최강 RAG 베이스라인(GraphRAG) 대비 **EM@1 +39.3, 지연 18.6% 감소, 간선 증가 40.9% 감소**를 보고했다.

## 강점과 한계

강점은 정확도와 비용을 **명시적 제약으로 동시에 다루고**, 예산을 바꿔도 재학습이 필요 없다는 점, 그리고 탐색 궤적이 남아 근거 추적이 가능하다는 점이다. 한계로는 다중 에이전트 강화학습 훈련 자체가 부담이고, 보상·제약 설계와 예산 설정에 민감할 수 있으며, 학습이 이루어진 그래프·질의 분포를 벗어나면 정책의 일반화가 보장되지 않는다는 점을 들 수 있다.

## 관련 항목

- [온톨로지 기반·뉴로심볼릭 GraphRAG](../concepts/neurosymbolic-graphrag.md) — CLAUSE가 속한 연구 흐름.
- [Subgraph Extraction](../techniques/subgraph-extraction.md) — Subgraph Architect가 수행하는 핵심 작업.
- [Graph Traversal Reasoning](../techniques/graph-traversal-reasoning.md) — Path Navigator의 탐색 방식.
- [Think-on-Graph (ToG)](think-on-graph.md) — LLM이 그래프를 단계적으로 탐색하되 학습된 정책 없이 프롬프팅에 의존하는 선행 접근.
- [GraphSearch](graphsearch.md) — 에이전트가 반복 검색을 수행하는 동시대 설계.
- [EA-GraphRAG](ea-graphrag.md) — 비용·지연을 질의 단위로 조절한다는 목표를 공유한다.
- [Knowledge Graph QA (KGQA)](../concepts/knowledge-graph-question-answering.md) — 평가가 이루어지는 과제 설정.
- [OG-RAG](og-rag.md) — 같은 흐름에서 온톨로지로 심볼릭 구조를 도입한 EMNLP 2025 연구.

## 참고문헌

- *CLAUSE: Agentic Neuro-Symbolic Knowledge Graph Reasoning via Dynamic Learnable Context Engineering* (2025). ICLR 2026. arXiv:2509.21035 — https://arxiv.org/abs/2509.21035
