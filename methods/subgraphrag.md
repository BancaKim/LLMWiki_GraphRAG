---
type: Method
title: SubgraphRAG
description: 경량 MLP 검색기와 방향성 거리 인코딩(DDE)으로 지식 그래프에서 유연한 크기의 부분그래프를 검색하고, 이를 LLM에 제공해 추론·답변하게 하는 KG 기반 RAG 방법이다.
tags: [graphrag, knowledge-graph, retrieval, kgqa, subgraph-retrieval]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2410.20724
authors: [Mufei Li, Siqi Miao, Pan Li]
year: 2024
venue: ICLR 2025
arxiv: "2410.20724"
---

# SubgraphRAG

SubgraphRAG는 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)를 기반으로 한 [RAG (Retrieval-Augmented Generation)](../concepts/retrieval-augmented-generation.md) 방법으로, 질의와 관련된 부분그래프(subgraph)를 검색해 [LLM (Large Language Model)](../concepts/large-language-model.md)에 제공하고 추론과 답변 생성을 맡긴다. Li et al.(2024)이 제안했으며, 복잡한 검색기 대신 단순한 구조로도 효과적인 [KGQA (Knowledge Graph QA)](../concepts/knowledge-graph-question-answering.md) 성능을 달성할 수 있음을 보인다. 논문 제목 "Simple Is Effective"가 시사하듯, 그래프와 LLM 각각의 역할을 분리해 단순함과 성능의 균형을 추구한다.

## 개요

SubgraphRAG는 검색(retrieve)과 추론(reason)의 두 단계로 구성된다. 검색 단계에서는 지식 그래프의 트리플(triple)들에 점수를 매겨 질의와 관련된 [부분그래프를 추출](../techniques/subgraph-extraction.md)하고, 추론 단계에서는 추출된 부분그래프를 프롬프트에 담아 LLM이 답을 생성한다. WebQSP와 CWQ(ComplexWebQuestions) 등 [KGQA 벤치마크](../benchmarks/webqsp.md)에서 평가되었다.

## 핵심 아이디어 / 동작 방식

검색기는 무거운 [GNN (Graph Neural Network)](../techniques/graph-neural-network.md) 대신 경량 MLP(다층 퍼셉트론)를 사용해 각 트리플을 병렬로 점수화한다. 이때 방향성 거리 인코딩(Directional Distance Encoding, DDE)으로 토픽 엔티티와 트리플 사이의 구조적 거리를 인코딩해 질의 관련성을 포착한다. 검색되는 부분그래프의 크기는 질의의 난이도와 다운스트림 LLM의 용량에 맞춰 유연하게 조절할 수 있다. 검색된 부분그래프는 추가 미세조정 없이 LLM에 전달되어 답변과 근거 추론을 생성한다.

## 기여

병렬 트리플 점수화와 DDE를 결합한 단순한 검색기 설계를 제시하고, 부분그래프 크기를 조절 가능한 매개변수로 다룬다. Llama3.1-8B-Instruct 같은 작은 모델은 설명 가능한 추론과 함께 경쟁력 있는 결과를, GPT-4o 같은 큰 모델은 미세조정 없이 최신 수준의 정확도를 보였다.

## 강점과 한계

검색기가 가벼워 효율적이고 확장성이 좋으며, 근거를 함께 제시해 [환각 (Hallucination)](../concepts/hallucination.md)을 줄이는 데 기여한다. 반면 성능이 사전 구축된 지식 그래프의 품질과 토픽 엔티티 식별 정확도에 의존하며, 텍스트 코퍼스 자체를 다루는 [Microsoft GraphRAG](microsoft-graphrag.md)류와 달리 정형 KG가 전제되어야 한다.

## 관련 항목

- [G-Retriever](g-retriever.md) — 부분그래프 검색을 통해 KGQA를 수행하는 유사 계열 방법
- [GNN-RAG](gnn-rag.md) — GNN으로 부분그래프를 검색·추론하는 대조적 접근
- [Reasoning on Graphs (RoG)](reasoning-on-graphs.md) — KG 위에서 관계 경로를 활용하는 KGQA 방법
- [Think-on-Graph (ToG)](think-on-graph.md) — LLM이 그래프를 탐색하며 추론하는 방법
- [Subgraph Extraction](../techniques/subgraph-extraction.md) — SubgraphRAG의 핵심 검색 기법
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — SubgraphRAG가 속한 그래프 기반 RAG 패러다임
- [WebQuestionsSP (WebQSP)](../benchmarks/webqsp.md) — 주요 평가 벤치마크
- [ComplexWebQuestions (CWQ)](../benchmarks/complexwebquestions.md) — 멀티홉 평가 벤치마크

## 참고문헌

- Li, M., Miao, S., & Li, P. (2024). *Simple Is Effective: The Roles of Graphs and Large Language Models in Knowledge-Graph-Based Retrieval-Augmented Generation*. ICLR 2025. arXiv:2410.20724 — https://arxiv.org/abs/2410.20724
