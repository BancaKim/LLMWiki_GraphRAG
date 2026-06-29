---
type: Method
title: StructGPT
description: 전용 인터페이스로 구조화 데이터에서 근거를 모으고 LLM이 그 위에서 추론하도록 분리한, 반복적 읽기-추론(IRR) 기반의 범용 구조화 데이터 추론 프레임워크다.
tags: [graphrag, retrieval, knowledge-graph, knowledge-graph-qa, multi-hop-reasoning, llm]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2305.09645
authors: [Jinhao Jiang, Kun Zhou, Zican Dong, Keming Ye, Wayne Xin Zhao, Ji-Rong Wen]
year: 2023
venue: "EMNLP 2023"
arxiv: "2305.09645"
---

# StructGPT

StructGPT는 [LLM](../concepts/large-language-model.md)이 지식 그래프, 테이블, 데이터베이스 같은 구조화 데이터(structured data) 위에서 추론하도록 돕는 범용 프레임워크다. 핵심은 데이터에서 근거를 수집하는 "읽기(reading)"와 그 근거로 답을 도출하는 "추론(reasoning)"을 분리하고, 이를 반복하는 Iterative Reading-then-Reasoning(IRR) 절차다. Jiang et al.(2023)이 EMNLP 2023에서 제안했으며, 별도 학습 없이 여러 종류의 구조화 데이터를 하나의 패러다임으로 다루는 점이 특징이다.

## 개요

LLM은 방대한 비정형 텍스트로 학습되어, 스키마와 관계로 짜인 구조화 데이터를 직접 다루는 데 한계가 있다. 데이터 전체를 프롬프트에 넣으면 길이 제약과 [환각 (Hallucination)](../concepts/hallucination.md)이 문제가 된다. StructGPT는 데이터 접근을 LLM 외부의 전용 인터페이스에 맡기고, LLM은 인터페이스가 제공한 정제된 근거만 보고 추론에 집중하게 하여 이 간극을 좁힌다. 하나의 틀로 [KGQA](../concepts/knowledge-graph-question-answering.md), TableQA, Text-to-SQL을 함께 처리한다.

## 핵심 아이디어 / 동작 방식

각 데이터 유형마다 관련 정보를 추출하는 전용 인터페이스를 둔다. 동작은 invoking-linearization-generation 세 단계를 반복한다. 먼저 LLM이 인터페이스를 호출(invoking)해 현재 추론에 필요한 후보 정보(예: 개체의 이웃 관계, 테이블 열)를 가져오고, 그 결과를 LLM이 읽을 수 있는 텍스트로 선형화(linearization)한 뒤, LLM이 이를 근거로 다음 행동을 계획하거나 답을 생성(generation)한다. 한 번에 답하기 부족하면 다시 인터페이스를 호출해 근거를 보강하며, 이 읽기-추론 순환을 답이 확정될 때까지 반복한다. 이 점에서 그래프를 직접 순회하는 [Think-on-Graph (ToG)](think-on-graph.md)와 발상을 공유한다.

## 기여

- 테이블, 지식 그래프, 데이터베이스 등 여러 구조화 데이터를 단일 패러다임으로 추론하는 첫 통합 프레임워크 제시.
- 읽기와 추론을 분리한 IRR 절차와 invoking-linearization-generation 동작 방식 제안.
- 데이터 접근을 전용 인터페이스로 위임해, 학습 없이(zero-shot·few-shot) LLM의 구조화 데이터 추론 성능을 끌어올림.

## 강점과 한계

StructGPT는 추가 학습이나 미세조정 없이 여러 데이터 유형과 과제에 적용되며, 인터페이스가 검색 부담을 떠맡아 LLM은 추론에만 집중한다. 다만 각 데이터 유형마다 인터페이스를 설계해야 하고, 반복적 LLM 호출로 비용과 지연이 늘며, 성능은 인터페이스가 모아 주는 근거의 품질에 의존한다. 또한 잘 구조화된 데이터를 전제하므로, 비정형 텍스트 코퍼스에 곧바로 적용하기는 어렵다.

## 관련 항목
- [Think-on-Graph (ToG)](think-on-graph.md) — LLM이 그래프를 반복 탐색하며 추론하는 유사한 발상의 기법
- [Reasoning on Graphs (RoG)](reasoning-on-graphs.md) — 그래프 경로를 LLM 추론에 결합하는 비교 대상 기법
- [KGQA (Knowledge Graph QA)](../concepts/knowledge-graph-question-answering.md) — StructGPT가 다루는 과제 설정 중 하나
- [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md) — StructGPT가 추론 대상으로 삼는 구조화 데이터
- [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md) — 반복적 읽기-추론이 겨냥하는 복합 질의 유형
- [환각 (Hallucination)](../concepts/hallucination.md) — 외부 근거로 완화하려는 문제
- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md) — 외부 근거를 LLM에 결합한다는 점에서 맞닿는 패러다임
- [WebQSP](../benchmarks/webqsp.md) — StructGPT의 KGQA 평가에 쓰인 대표 벤치마크

## 참고문헌
- Jiang, J., Zhou, K., Dong, Z., Ye, K., Zhao, W. X., & Wen, J.-R. (2023). *StructGPT: A General Framework for Large Language Model to Reason over Structured Data*. EMNLP 2023. arXiv:2305.09645 — https://arxiv.org/abs/2305.09645
