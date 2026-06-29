---
type: Benchmark
title: HotpotQA
description: Wikipedia 문단에 기반해 여러 문서를 연결해야 답할 수 있는 약 113,000개의 멀티홉 질의응답 쌍과 문장 단위 근거 라벨을 제공하는 데이터셋이다.
tags: [benchmark, multi-hop-reasoning, question-answering, retrieval, graphrag]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/1809.09600
authors: [Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio, William W. Cohen, Ruslan Salakhutdinov, Christopher D. Manning]
year: 2018
venue: EMNLP 2018
arxiv: "1809.09600"
---

# HotpotQA

HotpotQA는 Yang et al.(2018)이 공개한 멀티홉 질의응답(multi-hop question answering) 데이터셋이다. 각 질문은 둘 이상의 Wikipedia 문서에서 정보를 찾아 연결해야만 답할 수 있도록 설계되었으며, 약 113,000개의 크라우드소싱 질의응답 쌍으로 구성된다. 정답 외에 추론에 필요한 문장 단위 근거(supporting facts)를 함께 라벨링하여, 시스템이 답을 설명 가능하게 도출하도록 유도한다.

## 개요

HotpotQA는 특정 지식 베이스나 스키마에 종속되지 않은 자유 형식 질문으로 구성되어 있어, 사전 정의된 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md) 위의 질의응답과 구별된다. 질문은 두 엔티티를 잇는 다리 역할을 하는 bridge 유형과, 두 엔티티의 속성을 견주는 comparison 유형으로 나뉜다. 이러한 구성은 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md) 능력을 직접적으로 평가하기 위한 것이다.

## 과제 및 형식

데이터셋은 두 가지 설정을 제공한다. distractor 설정에서는 정답에 필요한 2개의 근거 문단과 8개의 방해 문단을 합한 10개 문단을 읽고 답과 근거를 함께 산출한다. fullwiki 설정에서는 방해 문단이 주어지지 않고 전체 Wikipedia 범위에서 관련 문서를 직접 검색해야 하므로, [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md) 및 [Dense Retrieval / Vector Search](../concepts/dense-retrieval.md) 방식의 검색 성능이 함께 평가된다.

## 평가 지표

평가는 답(Answer), 근거(Supporting facts), 둘을 결합한 Joint의 세 범주에 대해 각각 Exact Match(EM)와 F1으로 측정한다. Joint 지표는 정답과 근거를 모두 맞혀야 점수를 얻으므로, 단순 정답 정확도뿐 아니라 추론 과정의 타당성까지 함께 검증한다.

## GraphRAG 연구에서의 활용

HotpotQA는 [GraphRAG (the paradigm)](../concepts/graph-rag.md) 계열 연구에서 멀티홉 검색·추론 성능을 가늠하는 표준 벤치마크로 널리 쓰인다. 특히 [HippoRAG](../methods/hipporag.md), [HippoRAG 2](../methods/hipporag-2.md) 등은 [MuSiQue](musique.md), [2WikiMultiHopQA](2wikimultihopqa.md)와 더불어 HotpotQA를 사용해 여러 문서에 흩어진 단서를 통합하는 능력을 보고한다.

## 관련 항목

- [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md) — HotpotQA가 측정하려는 핵심 능력
- [MuSiQue](musique.md) — 함께 비교되는 멀티홉 QA 벤치마크
- [2WikiMultiHopQA](2wikimultihopqa.md) — 함께 비교되는 Wikipedia 기반 멀티홉 QA 벤치마크
- [HippoRAG](../methods/hipporag.md) — HotpotQA로 멀티홉 검색 성능을 평가하는 대표 GraphRAG 기법
- [HippoRAG 2](../methods/hipporag-2.md) — HotpotQA를 평가에 사용하는 후속 기법
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — 이 벤치마크가 적용되는 연구 패러다임
- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md) — fullwiki 설정에서 평가되는 검색·생성 방식

## 참고문헌

- Yang, Z., Qi, P., Zhang, S., Bengio, Y., Cohen, W. W., Salakhutdinov, R., & Manning, C. D. (2018). *HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering*. EMNLP 2018. arXiv:1809.09600 — https://arxiv.org/abs/1809.09600
