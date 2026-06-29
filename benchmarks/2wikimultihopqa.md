---
type: Benchmark
title: 2WikiMultiHopQA
description: Wikipedia 본문과 Wikidata를 결합해 만든 약 19만 개 규모의 멀티홉 질의응답 데이터셋으로, 정답과 함께 문장 단위 근거 및 추론 경로를 나타내는 근거 트리플(evidence triples)을 제공한다.
tags: [benchmark, multi-hop-reasoning, question-answering, knowledge-graph, retrieval]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2011.01060
authors: [Xanh Ho, Anh-Khoa Duong Nguyen, Saku Sugawara, Akiko Aizawa]
year: 2020
venue: COLING 2020
arxiv: "2011.01060"
---

# 2WikiMultiHopQA

2WikiMultiHopQA는 Ho et al.(2020)이 공개한 멀티홉 질의응답(multi-hop question answering) 데이터셋이다. Wikipedia의 비정형 본문과 Wikidata의 정형 지식을 함께 활용해 구성되었으며, 정답뿐 아니라 추론 과정을 검증할 수 있는 근거 정보를 함께 제공하는 것이 특징이다. 데이터셋은 약 192,606개의 예시로 이루어져 있고, 학습·개발·테스트로 분할된다.

## 개요

2WikiMultiHopQA는 기존 멀티홉 데이터셋에서 단일 문단만으로 답이 추론되는 지름길 문제를 줄이기 위해 설계되었다. 질문은 Wikidata 트리플과 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)에 정의된 논리 규칙, 그리고 템플릿을 결합해 생성되며, comparison(비교), inference(추론), compositional(합성), bridge-comparison(브리지 비교)의 네 가지 유형으로 나뉜다. 이러한 구성은 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md) 능력을 직접 평가하기 위한 것이다.

## 과제 및 형식

각 예시는 질문, 정답, 여러 Wikipedia 문단으로 구성된 context, 그리고 두 가지 근거를 함께 제공한다. 하나는 문장 단위 근거인 supporting facts이며, 다른 하나는 (주어, 관계, 목적어) 형태의 근거 트리플(evidence triples)로 표현된 reasoning path이다. 트리플 기반 근거는 질문에서 정답으로 이어지는 완전한 추론 경로를 명시하므로, 이 데이터셋은 [Knowledge Graph QA (KGQA)](../concepts/knowledge-graph-question-answering.md)와 [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md) 양쪽 평가에 모두 쓰인다.

## 평가 지표

평가는 Answer(정답), Supporting facts(문장 근거), Evidence(근거 트리플), 그리고 이들을 결합한 Joint의 네 범주에 대해 각각 Exact Match(EM)와 F1으로 측정한다. Evidence 지표는 모델이 정답을 맞히는 것을 넘어 올바른 추론 경로를 제시했는지를 검증하므로, 추론 단계의 타당성까지 종합적으로 평가한다.

## GraphRAG 연구에서의 활용

2WikiMultiHopQA는 [GraphRAG (the paradigm)](../concepts/graph-rag.md) 계열 연구에서 여러 문서에 흩어진 단서를 통합하는 능력을 가늠하는 표준 벤치마크로 쓰인다. [HippoRAG](../methods/hipporag.md)와 [HippoRAG 2](../methods/hipporag-2.md) 등은 [HotpotQA](hotpotqa.md), [MuSiQue](musique.md)와 더불어 이 데이터셋을 사용해 멀티홉 검색·추론 성능을 보고한다. 근거 트리플을 제공한다는 점에서 그래프 기반 검색 방법의 추론 경로 평가에 특히 적합하다.

## 관련 항목

- [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md) — 이 벤치마크가 측정하려는 핵심 능력
- [HotpotQA](hotpotqa.md) — 함께 비교되는 Wikipedia 기반 멀티홉 QA 벤치마크
- [MuSiQue](musique.md) — 함께 비교되는 멀티홉 QA 벤치마크
- [Knowledge Graph QA (KGQA)](../concepts/knowledge-graph-question-answering.md) — 근거 트리플 기반 평가와 맞닿는 과제 유형
- [Knowledge Graph](../concepts/knowledge-graph.md) — 질문 생성과 근거 트리플의 기반이 되는 Wikidata 구조
- [HippoRAG](../methods/hipporag.md) — 이 데이터셋으로 멀티홉 검색 성능을 평가하는 대표 GraphRAG 기법
- [HippoRAG 2](../methods/hipporag-2.md) — 이 데이터셋을 평가에 사용하는 후속 기법
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — 이 벤치마크가 적용되는 연구 패러다임

## 참고문헌

- Ho, X., Nguyen, A.-K. D., Sugawara, S., & Aizawa, A. (2020). *Constructing A Multi-hop QA Dataset for Comprehensive Evaluation of Reasoning Steps*. COLING 2020. arXiv:2011.01060 — https://arxiv.org/abs/2011.01060
