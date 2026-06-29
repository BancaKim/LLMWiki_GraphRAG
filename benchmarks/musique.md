---
type: Benchmark
title: MuSiQue
description: 단일 홉 질문을 조합해 구성한 2~4홉 멀티홉 질의응답 벤치마크로, 약 25K개의 문항과 답 가능/불가능 변형(MuSiQue-Ans, MuSiQue-Full)을 제공한다.
tags: [benchmark, multi-hop-reasoning, question-answering, retrieval]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2108.00573
authors: [Harsh Trivedi, Niranjan Balasubramanian, Tushar Khot, Ashish Sabharwal]
year: 2022
venue: Transactions of the Association for Computational Linguistics (TACL)
arxiv: "2108.00573"
---

# MuSiQue

MuSiQue는 여러 단계의 추론을 거쳐야 답할 수 있는 질의응답(QA) 능력을 평가하기 위한 멀티홉 질의응답 벤치마크다. Trivedi et al.(2022)이 제안했으며, 연결된 여러 개의 단일 홉(single-hop) 질문을 상향식으로 조합해 2~4홉 질문을 만드는 방식으로 약 25K개의 문항을 구성한다. 이를 통해 추론 단계가 서로 끊기지 않고 한 단계가 다른 단계의 정보에 의존하도록 설계되어, 우회적 추론으로 정답을 맞히기 어렵게 만든다.

## 개요

MuSiQue는 기존 멀티홉 데이터셋이 종종 단계 간 연결 없이도 풀린다는 한계를 보완하고자, 구성 가능한 단일 홉 질문 쌍을 체계적으로 선택하고 엄격한 필터를 적용해 만들어졌다. 그 결과 사람과 기계의 성능 격차가 기존 대비 약 3배 더 크고, 단계를 건너뛰는 방식의 풀이가 더 어렵다. 데이터셋은 두 가지 변형으로 제공된다. MuSiQue-Ans는 모두 답할 수 있는 문항으로 구성되며, MuSiQue-Full은 답할 수 없는 대조 문항을 추가해 답 가능 여부 판단까지 요구한다. 이 벤치마크는 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md) 능력을 측정하는 대표적 자원이다.

## 과제 및 형식

각 문항은 질문과 함께 여러 개의 후보 문단(passage)을 제공하며, 그중 일부만이 정답을 도출하는 데 필요한 근거 문단이다. 시스템은 관련 문단을 검색하고 여러 홉에 걸쳐 근거를 추적하면서 최종 답을 추출해야 한다. 각 멀티홉 질문은 이를 구성한 단일 홉 질문들로 분해될 수 있어, 추론 경로를 명시적으로 분석할 수 있다는 점이 특징이다. 이러한 형식은 분산된 문단에서 정보를 연결하는 검색·추론 능력을 함께 평가한다.

## 평가 지표

핵심 지표는 정답 토큰 수준의 Answer F1과 근거 문단 식별을 평가하는 Support F1이다. MuSiQue-Full에서는 답 가능 여부 판단을 반영하기 위해 그룹 단위의 충분성 지표(Group Answer Sufficiency F1, Group Support Sufficiency F1)가 추가로 사용된다. 이를 통해 답의 정확성과 근거 검색 품질을 함께 측정한다.

## GraphRAG 연구에서의 활용

MuSiQue는 분산된 문서에서 정보를 연결해야 하는 특성 때문에, 그래프 구조로 검색을 강화하는 [GraphRAG (the paradigm)](../concepts/graph-rag.md) 연구에서 자주 쓰이는 평가 자원이다. [HippoRAG](../methods/hipporag.md), [HippoRAG 2](../methods/hipporag-2.md) 등 다중 문서 멀티홉 검색을 표방하는 방법들이 [HotpotQA](hotpotqa.md), [2WikiMultiHopQA](2wikimultihopqa.md)와 함께 MuSiQue를 표준 비교 대상으로 채택한다. 단계 간 연결이 강제되는 설계 덕분에, 단순한 [Dense Retrieval / Vector Search](../concepts/dense-retrieval.md) 대비 그래프 기반 검색의 이점을 드러내기에 적합한 난이도 높은 벤치마크로 평가된다.

## 관련 항목

- [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md) — MuSiQue가 직접 측정하는 핵심 능력
- [HotpotQA](hotpotqa.md) — 함께 자주 보고되는 멀티홉 QA 벤치마크
- [2WikiMultiHopQA](2wikimultihopqa.md) — 유사한 멀티홉 QA 데이터셋으로 비교 대상
- [HippoRAG](../methods/hipporag.md) — MuSiQue를 주요 평가 대상으로 삼는 GraphRAG 방법
- [HippoRAG 2](../methods/hipporag-2.md) — MuSiQue에서 성능을 보고하는 후속 방법
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — 이 벤치마크가 활용되는 연구 패러다임
- [Dense Retrieval / Vector Search](../concepts/dense-retrieval.md) — 비교 기준이 되는 기본 검색 방식

## 참고문헌

- Trivedi, H., Balasubramanian, N., Khot, T., & Sabharwal, A. (2022). *MuSiQue: Multihop Questions via Single-hop Question Composition*. Transactions of the Association for Computational Linguistics (TACL), 10, 539–554. arXiv:2108.00573 — https://arxiv.org/abs/2108.00573
