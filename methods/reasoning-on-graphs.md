---
type: Method
title: Reasoning on Graphs (RoG)
description: RoG는 LLM과 지식 그래프를 결합해 관계 경로를 계획으로 생성하고 이를 따라 추론 경로를 검색·추론함으로써 충실하고 해석 가능한 추론을 수행하는 KGQA 방법이다.
tags: [graphrag, knowledge-graph, kgqa, multi-hop-reasoning, retrieval]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2310.01061
authors: [Linhao Luo, Yuan-Fang Li, Gholamreza Haffari, Shirui Pan]
year: 2024
venue: ICLR 2024
arxiv: "2310.01061"
---

# Reasoning on Graphs (RoG)

Reasoning on Graphs(RoG)는 [LLM](../concepts/large-language-model.md)과 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)를 결합하여 충실하고(faithful) 해석 가능한(interpretable) 추론을 수행하는 [KGQA](../concepts/knowledge-graph-question-answering.md) 방법이다. Luo 등(2024)이 ICLR 2024에서 제안했으며, KG의 구조를 단순한 사실 저장소가 아닌 추론을 위한 계획의 근거로 활용한다. 핵심은 LLM이 KG에 기반한 관계 경로(relation path)를 먼저 "계획"으로 생성하고, 그 계획을 따라 실제 추론 경로를 검색해 답을 도출하는 데 있다.

## 개요

LLM은 강력한 추론 능력을 보이지만 최신 지식이 부족하고 추론 과정에서 [환각 (Hallucination)](../concepts/hallucination.md)을 일으킨다. 기존 KG 기반 방법은 KG를 사실 지식 베이스로만 쓰고 구조 정보를 충분히 활용하지 못했다. RoG는 이를 보완하여 계획-검색-추론(planning-retrieval-reasoning)의 세 단계로 KG의 구조를 추론에 통합한다.

## 핵심 아이디어 / 동작 방식

RoG는 세 단계로 작동한다. 첫째, 계획 단계에서 LLM이 질문에 대해 KG에 근거한 관계 경로들을 생성한다. 이 경로는 그래프 스키마에 부합하도록 학습되어 충실한 계획 역할을 한다. 둘째, 검색 단계에서 생성된 관계 경로를 따라 KG에서 유효한 [추론 경로](../techniques/graph-traversal-reasoning.md)를 [추출](../techniques/subgraph-extraction.md)한다. 셋째, 추론 단계에서 LLM이 검색된 경로를 근거로 답과 추론 과정을 함께 생성한다. 계획과 추론은 단일 LLM을 공동 학습하는 최적화 목표로 통합된다.

## 기여

- KG의 구조 정보를 관계 경로 형태의 명시적 계획으로 활용하는 계획-검색-추론 프레임워크를 제안했다.
- 관계 경로를 근거로 삼아 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md)의 각 단계를 추적 가능하게 만들어 해석 가능성을 높였다.
- WebQSP와 CWQ 두 KGQA 벤치마크에서 당시 최첨단 성능을 보고했다.

## 강점과 한계

강점은 관계 경로가 검색된 사실로 뒷받침되어 환각을 줄이고 추론 과정을 사람이 검증할 수 있다는 점이다. 한계로는 정답을 담은 잘 정비된 KG의 존재에 의존하며, 관계 경로 생성을 위해 LLM을 미세조정해야 한다는 점, 그리고 평가가 주로 [WebQSP](../benchmarks/webqsp.md)·[CWQ](../benchmarks/complexwebquestions.md) 같은 정형 KGQA 환경에 집중되어 있다는 점이 있다.

## 관련 항목

- [Think-on-Graph (ToG)](think-on-graph.md) — LLM이 KG를 탐색하며 추론하는 또 다른 KGQA 접근
- [GNN-RAG](gnn-rag.md) — GNN으로 추론 경로를 검색해 LLM 추론을 보강하는 KGQA 방법
- [StructGPT](structgpt.md) — 정형 데이터를 LLM 추론에 통합하는 관련 프레임워크
- [Graph Traversal Reasoning](../techniques/graph-traversal-reasoning.md) — RoG의 경로 검색이 의존하는 그래프 순회 추론 기법
- [Knowledge Graph QA (KGQA)](../concepts/knowledge-graph-question-answering.md) — RoG가 다루는 과제 영역
- [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md) — 관계 경로가 지원하는 다단계 추론
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — 그래프 구조를 검색·생성에 활용하는 상위 패러다임
- [Unifying LLMs and KGs: A Roadmap](../surveys/llm-kg-roadmap.md) — LLM과 KG 통합 연구의 전반적 지형

## 참고문헌

- Luo, L., Li, Y.-F., Haffari, G., & Pan, S. (2024). *Reasoning on Graphs: Faithful and Interpretable Large Language Model Reasoning*. ICLR 2024. arXiv:2310.01061 — https://arxiv.org/abs/2310.01061
