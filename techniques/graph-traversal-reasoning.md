---
type: Technique
title: Graph Traversal Reasoning
description: LLM을 에이전트로 삼아 지식 그래프의 관계 경로를 반복적으로 탐색하거나 미리 계획해 따라가면서, 그 경로에 모인 근거로 멀티홉 질문에 답하는 GraphRAG 추론 기법이다.
tags: [graphrag, knowledge-graph, multi-hop-reasoning, graph-traversal, retrieval, knowledge-graph-qa]
timestamp: 2026-06-29
---

# Graph Traversal Reasoning

Graph Traversal Reasoning(그래프 순회 추론)은 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)의 개체와 관계를 따라 경로를 이동하면서 답의 근거를 모으는 [GraphRAG](../concepts/graph-rag.md) 추론 기법이다. 질문과 관련된 시작 개체에서 출발해 관계 간선(edge)을 한 홉(hop)씩 따라가며, 여러 문서·사실에 흩어진 정보를 연결해야 풀리는 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md) 질문에 답한다. 임베딩 유사도로 구절을 독립적으로 가져오는 검색과 달리, 그래프의 명시적 연결 구조를 추론의 골격으로 삼는 점이 특징이다.

## 개념

핵심 단위는 개체-관계-개체로 이어지는 관계 경로(relation path)다. 질문에 답하려면 어떤 개체에서 출발해 어떤 관계들을 거쳐 어떤 개체에 도달해야 하는지를 찾아야 하며, 그 경로 자체가 답의 근거이자 추론 과정의 설명이 된다. 이렇게 경로를 따라 답을 도출하면 각 추론 단계를 추적할 수 있어, [LLM](../concepts/large-language-model.md)이 내부 지식만으로 추론할 때 발생하는 [환각 (Hallucination)](../concepts/hallucination.md)을 줄이는 데 도움이 된다.

## 동작 방식

크게 두 갈래의 전략이 있다. 첫째는 탐색형으로, LLM을 에이전트로 두어 매 단계 현재 경로의 끝에서 연결된 후보 관계와 이웃 개체를 살피고, 관련성이 높은 경로만 남기며 한 홉씩 확장한다. [Think-on-Graph (ToG)](../methods/think-on-graph.md)가 이 방식의 대표로, 빔 서치로 유망한 경로를 추려가며 답하기에 충분한지 LLM이 직접 판정한다. 둘째는 계획형으로, [Reasoning on Graphs (RoG)](../methods/reasoning-on-graphs.md)처럼 LLM이 먼저 그래프 스키마에 부합하는 관계 경로를 계획으로 생성한 뒤 그 계획을 따라 실제 추론 경로를 검색한다. 어느 쪽이든 경로에 모인 사실을 근거로 답과 설명을 함께 [생성 (RAG)](../concepts/retrieval-augmented-generation.md)한다.

## GraphRAG에서의 활용

그래프 순회 추론은 정형 KG를 다루는 [KGQA (Knowledge Graph QA)](../concepts/knowledge-graph-question-answering.md) 계열 GraphRAG 기법의 토대다. ToG와 RoG 외에도 [StructGPT](../methods/structgpt.md)는 LLM이 구조화 데이터를 반복 호출하며 경로를 따라 추론하고, [GraphReader](../methods/graphreader.md)는 텍스트로 만든 그래프 위를 에이전트가 순회한다. 이런 기법들은 흩어진 근거를 연결 구조로 모아 멀티홉 질문의 정확도와 해석 가능성을 높이지만, 대체로 잘 구축된 KG에 의존하고 매 단계 LLM 호출로 인한 비용·지연이 크다는 한계가 있다.

## 관련 항목
- [Think-on-Graph (ToG)](../methods/think-on-graph.md) — LLM 에이전트가 빔 서치로 경로를 반복 탐색하는 탐색형 대표 기법.
- [Reasoning on Graphs (RoG)](../methods/reasoning-on-graphs.md) — 관계 경로를 계획으로 먼저 생성하고 따라가는 계획형 대표 기법.
- [Think-on-Graph 2.0](../methods/think-on-graph-2.md) — 그래프 순회를 텍스트 코퍼스와 결합해 확장한 후속 기법.
- [StructGPT](../methods/structgpt.md) — 정형 데이터를 반복 호출하며 경로를 따라 추론하는 관련 접근.
- [GraphReader](../methods/graphreader.md) — 텍스트로 구성한 그래프 위를 에이전트가 순회하는 기법.
- [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md) — 그래프 순회 추론이 풀려는 다단계 추론 유형.
- [Knowledge Graph QA (KGQA)](../concepts/knowledge-graph-question-answering.md) — 순회 추론이 주로 적용되는 과제 설정.
- [Unifying LLMs and KGs: A Roadmap](../surveys/llm-kg-roadmap.md) — LLM과 KG를 결합한 추론 연구의 전반적 지형.
