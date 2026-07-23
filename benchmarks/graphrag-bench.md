---
type: Benchmark
title: GraphRAG-Bench
description: GraphRAG 모델을 계층적 지식 검색과 심층 맥락 추론 양면에서 평가하는 도메인 특화 벤치마크로, 20개 핵심 교재·16개 학문 분야에 걸친 다양한 형식의 추론 문제를 제공한다.
tags: [benchmark, graphrag, knowledge-retrieval, reasoning, evaluation]
authors: [Yilin Xiao, Junnan Dong, Chuang Zhou, Su Dong, Qian-wen Zhang, Di Yin, Xing Sun, Xiao Ma]
year: 2025
venue: arXiv preprint (ICLR 2026)
arxiv: "2506.02404"
resource: https://arxiv.org/abs/2506.02404
timestamp: 2026-07-23
---

# GraphRAG-Bench

GraphRAG-Bench는 Xiao et al.(2025)이 제안한 도메인 특화 벤치마크로, GraphRAG 모델을 계층적 지식 검색(hierarchical knowledge retrieval)과 심층 맥락 추론(deep contextual reasoning) 두 축에서 평가한다. 20개 핵심 교재와 16개 학문 분야에 걸친 대학 수준의 문제로 구성되며, 그래프 구축에서 지식 검색과 답변 생성으로 이어지는 파이프라인 전 과정을 종합적으로 진단한다. "When to use Graphs in RAG" 계열 분석과 함께, GraphRAG가 표준 RAG보다 언제·왜 유리한지를 규명하려는 흐름을 대표하는 벤치마크다.

## 개요

기존 질의응답 벤치마크가 단편적 사실 검색에 치우쳐 [GraphRAG (the paradigm)](../concepts/graph-rag.md)의 구조적 이점을 충분히 드러내지 못한다는 문제의식에서 출발했다. GraphRAG-Bench는 교재의 장·절 구조를 반영한 계층적 지식을 바탕으로, 여러 개념을 연결해야 풀리는 문제를 구성해 [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)의 그래프 기반 확장이 실제로 어디에서 이득을 내는지를 측정하도록 설계되었다.

## 과제 및 형식

문항은 객관식(multiple-choice), 참·거짓(true/false), 다중 선택(multi-select), 개방형(open-ended), 빈칸 채우기(fill-in-the-blank) 등 다양한 형식을 포함한다. 각 문제는 흩어진 근거를 잇는 [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md)을 요구하도록 만들어져, 단순 회수만으로는 정답에 이르기 어렵게 구성된다.

## 평가 지표

답변 정확도에 그치지 않고 GraphRAG 파이프라인을 단계별로 평가한다. 즉 그래프 구축의 품질, 지식 검색의 적합성, 답변 생성의 정확성을 함께 측정하며, 추론 과정의 논리적 일관성(logical coherence)까지 점검한다. 이를 통해 최종 정답뿐 아니라 검색과 추론이 실제로 유효하게 작동했는지를 분리해 진단할 수 있다.

## GraphRAG 연구에서의 활용

GraphRAG-Bench는 [Microsoft GraphRAG](../methods/microsoft-graphrag.md), [LightRAG](../methods/lightrag.md), DIGIMON 등 다양한 GraphRAG 구현을 동일한 조건에서 비교할 수 있는 표준 평가대를 제공한다. 그래프 구조가 검색·추론에 언제 기여하는지를 실증적으로 규명하려는 연구에서 핵심 자원으로 쓰이며, 방법 간 성능 격차의 원인을 파이프라인 단계별로 분석하는 데 활용된다.

## 관련 항목

- [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md) — GraphRAG-Bench 문항이 요구하는 핵심 능력
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — 이 벤치마크가 평가 대상으로 삼는 연구 패러다임
- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md) — 그래프 기반 확장의 이점을 견주는 기준
- [Microsoft GraphRAG](../methods/microsoft-graphrag.md) — 벤치마크에서 비교되는 대표 GraphRAG 구현
- [LightRAG](../methods/lightrag.md) — 함께 평가되는 경량 GraphRAG 방법
- [Graph RAG: A Survey (Peng et al.)](../surveys/graph-rag-survey.md) — GraphRAG 평가 흐름을 정리한 서베이
- [HotpotQA](hotpotqa.md) — 전통적 멀티홉 QA 평가와 대비되는 기존 벤치마크

## 참고문헌

- Xiao, Y., Dong, J., Zhou, C., Dong, S., Zhang, Q., Yin, D., Sun, X., & Ma, X. (2025). *GraphRAG-Bench: Challenging Domain-Specific Reasoning for Evaluating Graph Retrieval-Augmented Generation*. arXiv preprint (ICLR 2026). arXiv:2506.02404 — https://arxiv.org/abs/2506.02404
