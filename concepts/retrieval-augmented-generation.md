---
type: Concept
title: Retrieval-Augmented Generation (RAG)
description: 외부 지식 소스에서 관련 정보를 검색해 LLM의 생성에 근거로 제공하는 패러다임으로, Lewis et al.(2020)이 NeurIPS에서 처음 정식화했으며 GraphRAG의 모태가 된다.
tags: [rag, retrieval, large-language-model, dense-retrieval, foundational]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2005.11401
authors: [Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, Douwe Kiela]
year: 2020
venue: NeurIPS 2020
arxiv: "2005.11401"
---

# Retrieval-Augmented Generation (RAG)

RAG(검색 증강 생성)는 질문에 답하거나 텍스트를 생성하기 전에 외부 지식 소스에서 관련 정보를 검색하여, 그 검색 결과를 [LLM (Large Language Model)](large-language-model.md)의 입력 근거로 제공하는 패러다임이다. 모델의 매개변수에만 의존하는 대신 검색된 외부 증거를 함께 사용하므로, 지식이 최신 상태로 유지되고 답변의 출처를 추적할 수 있다. Lewis et al.(2020)이 NeurIPS 2020에서 이 용어와 일반적 학습 방식을 처음 제시했다.

## 정의

RAG는 사전학습 seq2seq 모델이 보유한 매개변수 기억(parametric memory)과, 외부 문서 색인 같은 비매개변수 기억(non-parametric memory)을 결합한다. 원논문에서 비매개변수 기억은 Wikipedia의 [Dense Retrieval / Vector Search](dense-retrieval.md)로 구성된 벡터 색인이며, 검색기(DPR)가 질문에 관련된 문서를 찾고 생성기(BART)가 그 문서를 조건으로 답을 생성한다. 검색과 생성을 하나의 파이프라인으로 함께 학습한다는 점이 핵심이다.

## GraphRAG에서 중요한 이유

RAG는 [GraphRAG (the paradigm)](graph-rag.md)가 확장하는 출발점이다. 표준 RAG는 비정형 텍스트 조각을 [Text Embedding (텍스트 임베딩)](text-embedding.md)으로 색인하고 유사도로 검색하지만, 이런 방식은 여러 문서에 흩어진 사실을 잇는 [Multi-hop Reasoning (멀티홉 추론)](multi-hop-reasoning.md)이나 코퍼스 전체를 아우르는 질문에 약하다. GraphRAG 계열은 검색 대상을 평면 텍스트에서 [Knowledge Graph](knowledge-graph.md)와 그 구조로 바꿔 이 한계를 보완한다. 또한 RAG는 외부 근거를 제공함으로써 [Hallucination (환각)](hallucination.md)을 줄이는 공통 동기를 GraphRAG와 공유한다.

## 실제 활용

RAG는 개방형 질의응답, 사내 문서 검색 어시스턴트, 사실 검증 등 지식 집약적 과제에서 널리 쓰인다. 도메인 지식이 빠르게 바뀌거나 사적인 문서에 답이 있는 경우, 모델을 다시 학습하지 않고 검색 색인만 갱신하면 되므로 비용 효율적이다. 이러한 텍스트 기반 RAG의 발전사는 [RAG for LLMs: A Survey (Gao et al.)](../surveys/rag-survey.md)에 정리되어 있다.

## 관련 항목
- [GraphRAG (the paradigm)](graph-rag.md) — RAG의 검색 대상을 그래프 구조로 확장한 상위 패러다임
- [Large Language Model (LLM)](large-language-model.md) — RAG가 검색 근거로 보강하는 생성 모델
- [Dense Retrieval / Vector Search](dense-retrieval.md) — 원논문이 사용한 검색 방식이자 RAG의 기본 검색 메커니즘
- [Text Embedding (텍스트 임베딩)](text-embedding.md) — 문서와 질의를 벡터로 표현해 검색을 가능하게 하는 기반 기술
- [Hallucination (환각)](hallucination.md) — RAG가 외부 근거 제공으로 완화하려는 문제
- [Multi-hop Reasoning (멀티홉 추론)](multi-hop-reasoning.md) — 평면 RAG가 취약하고 GraphRAG가 보완하는 과제
- [Knowledge Graph](knowledge-graph.md) — GraphRAG가 검색 대상으로 삼는 구조화된 지식 표현
- [RAG for LLMs: A Survey (Gao et al.)](../surveys/rag-survey.md) — 텍스트 기반 RAG 연구 전반을 조망하는 서베이

## 참고문헌
- Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS 2020. arXiv:2005.11401 — https://arxiv.org/abs/2005.11401
