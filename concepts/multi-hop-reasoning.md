---
type: Concept
title: Multi-hop Reasoning (멀티홉 추론)
description: 하나의 구절에 답이 담겨 있지 않아 여러 사실과 관계를 단계적으로 연결해야 답할 수 있는 질의 유형으로, 평면 벡터 RAG가 약하고 그래프 구조가 보완하는 대표적 과제이다.
tags: [multi-hop-reasoning, graphrag, retrieval, knowledge-graph, reasoning]
timestamp: 2026-06-29
---

# Multi-hop Reasoning (멀티홉 추론)

멀티홉 추론(multi-hop reasoning)은 하나의 문서나 구절에서 곧바로 답을 찾을 수 없고, 서로 다른 곳에 흩어진 둘 이상의 사실을 연쇄적으로 이어 붙여야 비로소 답에 도달하는 질의 유형을 가리킨다. "X의 감독이 태어난 도시의 시장은 누구인가?"처럼 각 단계(홉, hop)가 다음 단계의 단서를 제공하며, 중간 개체를 매개로 추론이 진행된다. 이는 단일 사실을 그대로 조회하는 단일홉(single-hop) 질의와 대비된다.

## 정의

멀티홉 질의는 답을 얻기까지 둘 이상의 추론 단계가 필요하며, 각 홉은 하나의 사실 또는 관계를 해소한다. 일반적으로 첫 홉에서 찾은 중간 개체가 다음 홉의 검색 키가 되어, "A → B → C"와 같은 추론 경로(reasoning path)를 형성한다. [Knowledge Graph](knowledge-graph.md)에서는 이러한 경로가 노드를 잇는 엣지의 연속으로 명시적으로 표현되며, 이를 따라가는 과정이 [그래프 순회 추론 (Graph Traversal Reasoning)](../techniques/graph-traversal-reasoning.md)이다. HotpotQA·MuSiQue 같은 벤치마크가 이 능력을 측정한다.

## GraphRAG에서 중요한 이유

표준 [RAG (Retrieval-Augmented Generation)](retrieval-augmented-generation.md)는 질의와 표면적으로 유사한 [청크 (Text Chunking)](text-chunking.md)를 [밀집 검색 (Dense Retrieval)](dense-retrieval.md)으로 가져온다. 그러나 멀티홉 질의에서는 최종 답을 담은 구절이 질의 문장과 어휘적·의미적으로 멀리 떨어져 있을 수 있어, 중간 단계를 잇는 다리 구절을 놓치기 쉽다. [GraphRAG (the paradigm)](graph-rag.md)는 사실을 명시적으로 연결된 그래프로 저장하므로, 관계 엣지를 따라 중간 개체를 거쳐 답까지 도달하는 추론 경로를 검색할 수 있다. 이로써 근거가 분산된 질문에서도 답을 검증 가능한 사실에 그라운딩하여 [환각 (Hallucination)](hallucination.md)을 줄인다.

## 실제 활용

멀티홉 추론은 [지식 그래프 질의응답 (KGQA)](knowledge-graph-question-answering.md), 복잡한 개방형 질의응답, 여러 문서에 걸친 사실 검증 등에서 핵심 능력으로 평가된다. [HippoRAG](../methods/hipporag.md)는 [Personalized PageRank](../techniques/personalized-pagerank.md)로, [Think-on-Graph (ToG)](../methods/think-on-graph.md)는 그래프 위에서의 단계적 탐색으로 이 과제에 접근하며, [HotpotQA](../benchmarks/hotpotqa.md)·[MuSiQue](../benchmarks/musique.md)·[2WikiMultiHopQA](../benchmarks/2wikimultihopqa.md) 등이 표준 평가 데이터셋으로 쓰인다.

## 관련 항목
- [Knowledge Graph](knowledge-graph.md) — 추론 경로를 노드와 엣지로 명시적으로 표현하는 구조
- [GraphRAG (the paradigm)](graph-rag.md) — 그래프 구조로 멀티홉 검색을 가능하게 하는 패러다임
- [Dense Retrieval / Vector Search](dense-retrieval.md) — 멀티홉 질의에서 다리 구절을 놓치기 쉬운 기본 검색 방식
- [Graph Traversal Reasoning](../techniques/graph-traversal-reasoning.md) — 엣지를 따라 홉을 잇는 추론 과정
- [HippoRAG](../methods/hipporag.md) — PPR로 멀티홉 검색을 수행하는 대표 방법
- [Think-on-Graph (ToG)](../methods/think-on-graph.md) — 그래프 위 단계적 탐색으로 멀티홉을 푸는 방법
- [HotpotQA](../benchmarks/hotpotqa.md) — 멀티홉 추론을 측정하는 대표 벤치마크
- [MuSiQue](../benchmarks/musique.md) — 다단계 조합 질의로 멀티홉 능력을 평가하는 벤치마크
