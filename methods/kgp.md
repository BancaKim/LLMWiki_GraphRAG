---
type: Method
title: Knowledge Graph Prompting (KGP)
description: 여러 문서 위에 지식 그래프를 구성하고 LM 기반 그래프 탐색기로 근거 문단을 모아 LLM의 다중 문서 질의응답(MD-QA)을 돕는 그래프 기반 프롬프팅 기법(Wang et al., 2024).
tags: [graphrag, retrieval, knowledge-graph, multi-hop, prompting]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2308.11730
authors: [Yu Wang, Nedim Lipka, Ryan A. Rossi, Alexa Siu, Ruiyi Zhang, Tyler Derr]
year: 2024
venue: "AAAI 2024"
arxiv: "2308.11730"
---

# Knowledge Graph Prompting (KGP)

KGP(Knowledge Graph Prompting)는 여러 문서에 걸친 다중 문서 질의응답(MD-QA, Multi-Document Question Answering)을 위해, 문서 모음 위에 [지식 그래프](../concepts/knowledge-graph.md)를 구성하고 그 위를 탐색하며 모은 근거 문단을 [LLM](../concepts/large-language-model.md)의 프롬프트로 제공하는 [GraphRAG](../concepts/graph-rag.md) 계열 기법이다. Wang et al.(2024)이 제안했으며 AAAI 2024에 게재되었다. 그래프 구성 모듈과 그래프 탐색 모듈의 두 부분으로 이루어진다.

## 개요

기존 [RAG](../concepts/retrieval-augmented-generation.md)는 문단을 독립적으로 검색하기 때문에, 답이 여러 문서·구조에 흩어져 있는 [멀티홉 추론](../concepts/multi-hop-reasoning.md) 질문에서 적절한 문맥을 모으기 어렵다. KGP는 문서 간·문서 내 관계를 그래프로 명시화하고, 질의에 따라 그래프를 단계적으로 탐색해 LLM에 넘길 올바른 문맥(context)을 구성하는 것을 목표로 한다.

## 핵심 아이디어 / 동작 방식

그래프 구성 모듈은 문단이나 문서 구조(페이지, 표 등)를 노드로 삼고, 문단 간 의미적·어휘적 유사도나 문서 내 구조적 관계를 간선으로 연결해 [지식 그래프를 구성](../techniques/knowledge-graph-construction.md)한다. 그래프 탐색 모듈에서는 HotpotQA·2WikiMultiHopQA 등의 추론 데이터로 미세조정(fine-tuning)한 LM(T5)을 탐색기로 사용하여, 현재 노드에서 다음에 방문할 이웃 노드를 선택하며 그래프를 [순회 추론](../techniques/graph-traversal-reasoning.md)한다. 이렇게 점진적으로 모은 근거 문단을 LLM 프롬프트에 넣어 답을 생성한다.

## 기여

- MD-QA를 위한 그래프 구성과 LM 기반 그래프 탐색을 결합한 KGP 프레임워크를 제안했다.
- 문단뿐 아니라 페이지·표 같은 문서 구조를 노드로 포함해 비정형·반정형 문서를 함께 다룰 수 있게 했다.
- HotpotQA, 2WikiMultiHopQA, MuSiQue, IIRC 등 멀티홉 MD-QA 벤치마크에서 검색 품질과 정확도 향상을 보였다.

## 강점과 한계

강점은 문서 간 연결을 명시적으로 활용해 흩어진 근거를 모으고, 학습된 탐색기가 검색 경로를 안내하여 [환각](../concepts/hallucination.md)을 줄인다는 점이다. 한계로는 문서마다 그래프를 구성하는 전처리 비용이 들고, 탐색기 LM을 추론 데이터로 미세조정해야 하므로 도메인 이전 시 추가 비용이 발생할 수 있다.

## 관련 항목

- [GraphRAG (패러다임)](../concepts/graph-rag.md) — KGP가 속한 상위 패러다임
- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md) — KGP가 그래프로 확장·보완하는 기반 방법
- [Knowledge Graph Construction](../techniques/knowledge-graph-construction.md) — 그래프 구성 모듈이 수행하는 핵심 기술
- [Graph Traversal Reasoning](../techniques/graph-traversal-reasoning.md) — LM 탐색기가 그래프를 순회하는 방식
- [GraphReader](graphreader.md) — 에이전트가 그래프를 탐색해 문맥을 모으는 유사 접근
- [Think-on-Graph (ToG)](think-on-graph.md) — LLM이 그래프 위를 탐색하며 추론하는 관련 기법
- [HotpotQA](../benchmarks/hotpotqa.md) — KGP 평가에 사용된 멀티홉 QA 벤치마크
- [MuSiQue](../benchmarks/musique.md) — KGP 평가에 사용된 멀티홉 QA 벤치마크

## 참고문헌

- Wang, Y., Lipka, N., Rossi, R. A., Siu, A., Zhang, R., & Derr, T. (2024). *Knowledge Graph Prompting for Multi-Document Question Answering*. AAAI 2024. arXiv:2308.11730 — https://arxiv.org/abs/2308.11730
