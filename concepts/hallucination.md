---
type: Concept
title: Hallucination (환각)
description: LLM이 유창하지만 근거가 없거나 사실과 다른 내용을 그럴듯하게 생성하는 현상으로, 검색과 그래프 그라운딩으로 외부 근거를 제공해 완화한다.
tags: [hallucination, large-language-model, rag, graphrag, knowledge-graph]
timestamp: 2026-06-29
---

# Hallucination (환각)

환각(hallucination)은 [LLM (Large Language Model)](large-language-model.md)이 문법적으로 유창하고 자신감 있게 들리지만 실제로는 근거가 없거나 사실과 다른 내용을 생성하는 현상이다. 모델이 학습 데이터의 통계적 패턴에 따라 다음 토큰을 예측할 뿐 진위를 검증하지 않기 때문에, 존재하지 않는 인용·수치·관계가 그럴듯한 형태로 섞여 나올 수 있다. 사용자가 그 오류를 알아채기 어렵다는 점에서 신뢰성 문제의 핵심으로 다뤄진다.

## 정의

환각은 흔히 두 종류로 구분된다. 입력으로 주어진 맥락과 어긋나는 출력을 내는 사실 충돌형(faithfulness)과, 외부 세계의 사실과 어긋나는 사실 오류형(factuality)이다. 두 경우 모두 모델이 보유한 매개변수 기억의 한계, 학습 데이터의 공백, 또는 모호한 질의에서 비롯된다. 외부 근거 없이 모델 내부 지식에만 의존할수록 발생 가능성이 커진다.

## GraphRAG에서 중요한 이유

환각 완화는 [RAG (Retrieval-Augmented Generation)](retrieval-augmented-generation.md)와 [GraphRAG (the paradigm)](graph-rag.md)를 추동한 핵심 동기다. 검색으로 가져온 문서를 생성 근거로 제시하면 모델이 추측 대신 검색된 증거에 답을 정합(grounding)시킬 수 있다. 특히 GraphRAG는 근거를 [Knowledge Graph](knowledge-graph.md)의 명시적 개체와 관계로 표현하므로, 출처를 추적하고 사실을 검증하기 쉽다. 여러 문서에 흩어진 사실을 잇는 [Multi-hop Reasoning (멀티홉 추론)](multi-hop-reasoning.md)에서도 그래프 경로가 추론의 근거를 드러내어, 잘못 연결된 사실이 만드는 환각을 줄이는 데 기여한다.

## 실제 활용

환각 위험은 의료·법률·금융처럼 오류 비용이 큰 도메인에서 특히 문제가 되며, 이런 분야에서 그래프 기반 그라운딩이 활발히 시도된다. 다만 검색과 그래프가 환각을 완전히 없애지는 못하며, 검색 결과가 부정확하거나 그래프 구축 단계에서 오류가 유입되면 환각이 재현될 수 있다. 따라서 출처 표기, 답변과 근거의 일치 검증 등 평가 절차가 함께 쓰인다.

## 관련 항목
- [Large Language Model (LLM)](large-language-model.md) — 환각이 발생하는 생성 모델
- [Retrieval-Augmented Generation (RAG)](retrieval-augmented-generation.md) — 외부 근거 검색으로 환각을 완화하는 패러다임
- [GraphRAG (the paradigm)](graph-rag.md) — 그래프 구조로 근거를 제공해 환각을 줄이는 갈래
- [Knowledge Graph](knowledge-graph.md) — 출처 추적과 사실 검증을 돕는 구조화된 근거
- [Multi-hop Reasoning (멀티홉 추론)](multi-hop-reasoning.md) — 사실을 잘못 연결한 환각을 그래프 경로로 줄이는 과제
- [HippoRAG](../methods/hipporag.md) — 그래프 검색으로 근거 기반 답변을 추구하는 대표 구현
- [RAG for LLMs: A Survey (Gao et al.)](../surveys/rag-survey.md) — 환각 완화를 포함한 RAG 연구 전반을 정리한 서베이
