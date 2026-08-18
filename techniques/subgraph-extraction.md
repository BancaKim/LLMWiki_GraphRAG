---
type: Technique
title: Subgraph Extraction
description: 질의와 관련된 부분그래프(에고그래프)를 그래프에서 선택해 LLM에 제공하는 GraphRAG 검색 기법으로, G-Retriever의 PCST 최적화나 SubgraphRAG의 트리플 점수화처럼 큰 그래프를 컨텍스트에 맞는 크기로 추리는 데 쓰인다.
tags: [graphrag, retrieval, knowledge-graph, subgraph-extraction, kgqa]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2402.07630
---

# Subgraph Extraction

Subgraph Extraction(부분그래프 추출)은 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)나 텍스트 속성 그래프 전체에서 질의와 관련된 일부분만을 선택해 검색 단위로 삼는 [GraphRAG (the paradigm)](../concepts/graph-rag.md) 기법이다. 그래프가 [LLM (Large Language Model)](../concepts/large-language-model.md)의 컨텍스트 창을 쉽게 넘기는 규모이기 때문에, 질문에 답하는 데 필요한 노드·간선만 추려 입력하는 것이 목표다. 흔히 질의에 정박한 시드 노드 주변의 에고그래프(ego-graph)나 연결된 부분그래프 형태로 결과를 산출한다.

## 개념

핵심 과제는 "관련성"과 "크기" 사이의 균형이다. 너무 작으면 근거가 빠지고, 너무 크면 컨텍스트 창을 넘기거나 잡음이 늘어 [환각 (Hallucination)](../concepts/hallucination.md)을 유발한다. 일반적으로 [텍스트 임베딩 (Text Embedding)](../concepts/text-embedding.md)으로 질의와 노드·간선·트리플의 유사도를 매긴 뒤, 점수가 높은 요소를 시드로 삼아 그 주변을 연결된 부분그래프로 확장한다. 이렇게 추출된 부분그래프는 그 자체로 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md)에 필요한 관계 경로를 담을 수 있어, 구절을 독립적으로 가져오는 [밀집 검색 (Dense Retrieval)](../concepts/dense-retrieval.md)을 보완한다.

## 동작 방식

대표적으로 두 가지 정식화가 쓰인다. [G-Retriever](../methods/g-retriever.md)는 추출을 Prize-Collecting Steiner Tree(PCST) 최적화로 다루어, 관련 노드의 점수(prize) 합은 키우고 간선 비용은 줄이는 연결된 부분그래프를 찾는다. [SubgraphRAG](../methods/subgraphrag.md)는 경량 MLP로 각 트리플을 병렬 점수화하고 방향성 거리 인코딩으로 구조적 거리를 반영해, 질의 난이도와 모델 용량에 맞춰 크기를 유연하게 조절한다. 추출된 부분그래프는 텍스트로 직렬화해 프롬프트에 담거나, [GNN (Graph Neural Network)](graph-neural-network.md)으로 인코딩해 LLM 입력에 결합하는 방식으로 전달된다.

## GraphRAG에서의 활용

부분그래프 추출은 [KGQA (Knowledge Graph QA)](../concepts/knowledge-graph-question-answering.md) 계열 GraphRAG에서 검색의 중심 단계로 자리한다. G-Retriever와 SubgraphRAG가 WebQSP·CWQ 같은 벤치마크에서 이를 활용하며, 시드 기반 그래프 전파인 [Personalized PageRank](personalized-pagerank.md)나 경로 탐색 중심의 [Graph Traversal Reasoning](graph-traversal-reasoning.md)과는 "연결된 영역을 한 번에 추려 제공한다"는 점에서 대비된다. 이렇게 추출된 부분그래프는 LLM에 압축된 구조적 근거를 제공해 답변의 정확성과 추적 가능성을 높인다.

## 관련 항목
- [G-Retriever](../methods/g-retriever.md) — PCST 최적화로 연결된 부분그래프를 추출하는 대표 기법.
- [SubgraphRAG](../methods/subgraphrag.md) — 트리플 점수화로 크기 조절 가능한 부분그래프를 검색하는 기법.
- [Graph Neural Network (GNN)](graph-neural-network.md) — 추출된 부분그래프를 인코딩해 LLM에 결합하는 후속 단계.
- [Personalized PageRank](personalized-pagerank.md) — 시드에서 출발하는 그래프 전파로 관련 영역을 랭킹하는 관련 기법.
- [Graph Traversal Reasoning](graph-traversal-reasoning.md) — 부분그래프 대신 경로 탐색으로 근거를 모으는 대안적 검색 방식.
- [Knowledge Graph QA (KGQA)](../concepts/knowledge-graph-question-answering.md) — 부분그래프 추출이 주로 적용되는 과제 유형.
- [Knowledge Graph](../concepts/knowledge-graph.md) — 추출의 대상이 되는 기반 그래프 구조.
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — 부분그래프 추출을 검색 단계로 포함하는 상위 패러다임.
- [AGRAG](../methods/agrag.md) — 부분그래프 선택을 최소 비용 최대 영향(MCMI) 최적화 문제로 정식화한 기법.
