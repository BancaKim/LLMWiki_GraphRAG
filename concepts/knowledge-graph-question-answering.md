---
type: Concept
title: Knowledge Graph QA (KGQA)
description: 지식 그래프(KG)에 담긴 구조화된 사실을 근거로 자연어 질문에 답하는 과제로, ToG·RoG·GNN-RAG 등 다수 그래프 추론 기법이 표준 평가 대상으로 삼는다.
tags: [knowledge-graph, kgqa, question-answering, graphrag, multi-hop-reasoning]
timestamp: 2026-06-29
---

# Knowledge Graph QA (KGQA)

지식 그래프 질의응답(KGQA, Knowledge Graph Question Answering)은 [Knowledge Graph](knowledge-graph.md)에 저장된 구조화된 사실을 지식원으로 삼아 자연어 질문에 답하는 과제다. 답은 일반적으로 그래프 안의 한 개체(entity)나 값이며, 그것에 도달하기 위해 질문에 담긴 개체·관계를 그래프의 노드·엣지에 대응시키는 과정이 핵심이다. 단일 트리플로 답할 수 있는 단순 질의부터 여러 관계를 연쇄적으로 따라가야 하는 복잡한 질의까지 폭넓은 난이도를 포괄한다.

## 정의

KGQA는 자연어 질문 q와 지식 그래프 G가 주어졌을 때, G에서 답을 찾아 반환하는 문제로 정의된다. 전통적으로는 질문을 SPARQL 같은 구조화 질의로 번역하는 의미 분석(semantic parsing) 방식과, 답이 있을 법한 부분그래프를 검색해 그 위에서 직접 추론하는 정보 검색(information retrieval) 방식으로 나뉜다. 답을 얻기까지 둘 이상의 관계를 거쳐야 하는 [멀티홉 추론 (Multi-hop Reasoning)](multi-hop-reasoning.md)이 특히 어려운 부분이며, 이때 그래프 위의 추론 경로를 따라가는 [그래프 순회 추론 (Graph Traversal Reasoning)](../techniques/graph-traversal-reasoning.md)이 사용된다.

## GraphRAG에서 중요한 이유

KGQA는 [GraphRAG (the paradigm)](graph-rag.md) 계열 기법이 검색·추론 성능을 평가받는 대표적인 다운스트림 과제다. 표준 [Retrieval-Augmented Generation (RAG)](retrieval-augmented-generation.md)가 텍스트 청크를 검색해 답하는 것과 달리, KGQA는 명시적으로 연결된 사실 위에서 답을 도출하므로 출력을 검증 가능한 근거에 그라운딩하여 [Hallucination](hallucination.md)을 줄인다. 또한 [Large Language Model (LLM)](large-language-model.md)이 그래프 구조와 결합해 어떻게 다단계 추론을 수행하는지를 직접 드러내, 단순 표면 유사도 검색의 한계를 비교·검증하는 시험대가 된다.

## 실제 활용

[Think-on-Graph (ToG)](../methods/think-on-graph.md)는 LLM이 그래프를 단계적으로 탐색하며 답을 찾고, [Reasoning on Graphs (RoG)](../methods/reasoning-on-graphs.md)는 관계 경로 계획을 먼저 생성해 추론하며, [GNN-RAG](../methods/gnn-rag.md)는 [Graph Neural Network (GNN)](../techniques/graph-neural-network.md)로 후보 부분그래프를 추려 LLM에 넘긴다. 이들 기법은 [WebQuestionsSP (WebQSP)](../benchmarks/webqsp.md)와 [ComplexWebQuestions (CWQ)](../benchmarks/complexwebquestions.md) 같은 표준 벤치마크로 평가된다.

## 관련 항목
- [Knowledge Graph](knowledge-graph.md) — KGQA가 답을 길어 올리는 구조화된 지식원.
- [GraphRAG (the paradigm)](graph-rag.md) — KGQA를 핵심 평가 과제로 삼는 검색 증강 패러다임.
- [Multi-hop Reasoning (멀티홉 추론)](multi-hop-reasoning.md) — KGQA에서 가장 까다로운 다단계 질의 유형.
- [Think-on-Graph (ToG)](../methods/think-on-graph.md) — 그래프 탐색으로 KGQA를 푸는 대표 기법.
- [Reasoning on Graphs (RoG)](../methods/reasoning-on-graphs.md) — 관계 경로 계획 기반 KGQA 기법.
- [GNN-RAG](../methods/gnn-rag.md) — GNN으로 부분그래프를 추려 KGQA를 수행하는 기법.
- [WebQuestionsSP (WebQSP)](../benchmarks/webqsp.md) — KGQA 성능 측정의 표준 벤치마크.
- [ComplexWebQuestions (CWQ)](../benchmarks/complexwebquestions.md) — 복잡한 KGQA 능력을 평가하는 벤치마크.
