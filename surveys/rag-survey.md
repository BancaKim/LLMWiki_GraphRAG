---
type: Survey
title: "RAG for LLMs: A Survey (Gao et al.)"
description: 대규모 언어 모델을 위한 RAG(검색 증강 생성) 연구를 Naive·Advanced·Modular RAG의 세 패러다임과 Retrieval·Generation·Augmentation의 3대 구성요소로 체계화한 종합 서베이 논문.
tags: [rag, retrieval, survey, taxonomy, large-language-model]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2312.10997
authors: [Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia, Jinliu Pan, Yuxi Bi, Yi Dai, Jiawei Sun, Qianyu Guo, Meng Wang, Haofen Wang]
year: 2023
venue: arXiv preprint
arxiv: "2312.10997"
---

# RAG for LLMs: A Survey (Gao et al.)

"Retrieval-Augmented Generation for Large Language Models: A Survey"는 Yunfan Gao 등이 2023년에 공개한 서베이로, 텍스트 기반 [RAG (Retrieval-Augmented Generation)](../concepts/retrieval-augmented-generation.md)의 발전 과정을 폭넓게 정리한 대표적 종합 정리에 해당한다. [Large Language Model (LLM)](../concepts/large-language-model.md)의 [환각 (Hallucination)](../concepts/hallucination.md)과 지식 노후화 문제를 외부 지식 검색으로 보완하는 흐름을 추적한다. 그래프 기반 검색이 등장하기 이전, 일반 RAG 지형 전체를 조망하는 상위 참조 자료로 자주 인용된다.

## 범위

검색 대상이 주로 비정형 텍스트 말뭉치인 RAG 연구 전반을 다룬다. [텍스트 임베딩 (Text Embedding)](../concepts/text-embedding.md)과 [Dense Retrieval / Vector Search](../concepts/dense-retrieval.md)를 기반으로 한 검색-생성 파이프라인을 중심으로, 연구의 발전 단계·구성요소·평가 방법을 포괄한다. 후속의 [GraphRAG (the paradigm)](../concepts/graph-rag.md)와 달리 그래프 구조 자체는 핵심 주제가 아니다.

## 다루는 내용(분류 체계)

저자들은 RAG의 발전을 세 패러다임으로 구분한다. (1) Naive RAG는 색인-검색-생성의 기본 흐름을 가리키며 [텍스트 청킹 (Text Chunking)](../concepts/text-chunking.md) 후 단순 벡터 검색에 의존한다. (2) Advanced RAG는 검색 전후 처리(쿼리 재작성, 재랭킹 등)로 품질을 높인다. (3) Modular RAG는 검색·생성 모듈을 유연하게 재구성하는 단계다. 또한 RAG 시스템을 Retrieval(무엇을 어떻게 검색하는가), Generation(검색 결과를 어떻게 활용하는가), Augmentation(반복·적응적 검색 등 보강 기법) 세 구성요소로 분해하고, 평가 지표와 [Hybrid Retrieval](../techniques/hybrid-retrieval.md)을 비롯한 기법을 함께 정리한다.

## 핵심 시사점

RAG는 파라미터에 갇힌 지식을 외부 검색으로 보완해 사실성과 최신성을 높이는 핵심 패러다임으로 자리 잡았다. 이 서베이는 검색 품질·맥락 활용·증강 전략을 분리해 보는 관점을 제시했으며, 평면 텍스트 검색이 약한 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md)이나 전역 질의의 한계가 이후 그래프 기반 접근으로 이어지는 배경을 보여준다.

## 관련 항목
- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md) — 이 서베이가 정형화한 핵심 개념.
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — 텍스트 RAG의 한계를 보완하는 후속 패러다임.
- [Graph RAG: A Survey (Peng et al.)](graph-rag-survey.md) — 그래프 기반 RAG로 범위를 확장한 후속 서베이.
- [RAG with Graphs (Han et al.)](graphrag-with-graphs-survey.md) — 그래프 RAG를 다루는 또 다른 대표 서베이.
- [Dense Retrieval / Vector Search](../concepts/dense-retrieval.md) — Naive RAG 검색의 기본 토대.
- [Hybrid Retrieval](../techniques/hybrid-retrieval.md) — Advanced RAG에서 다루는 검색 강화 기법.
- [Hallucination (환각)](../concepts/hallucination.md) — RAG가 완화하려는 핵심 문제.
- [Large Language Model (LLM)](../concepts/large-language-model.md) — RAG가 보강하는 대상 모델.

## 참고문헌
- Gao, Y., Xiong, Y., Gao, X., Jia, K., Pan, J., Bi, Y., Dai, Y., Sun, J., Guo, Q., Wang, M., & Wang, H. (2023). *Retrieval-Augmented Generation for Large Language Models: A Survey*. arXiv preprint. arXiv:2312.10997 — https://arxiv.org/abs/2312.10997
