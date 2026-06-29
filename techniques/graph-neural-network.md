---
type: Technique
title: Graph Neural Network (GNN)
description: 그래프 구조 위에서 이웃 노드의 정보를 반복적으로 집계해 노드·엣지·부분그래프의 표현을 학습하는 신경망 계열로, GraphRAG에서는 부분그래프 인코딩과 노드 랭킹/검색에 활용된다.
tags: [graph-neural-network, retrieval, knowledge-graph, gnn-rag, graphrag]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/1812.08434
---

# Graph Neural Network (GNN)

Graph Neural Network(그래프 신경망, GNN)는 그래프의 노드와 엣지 위에서 동작하는 신경망 계열로, 각 노드가 자신의 이웃으로부터 메시지를 받아 표현(임베딩)을 갱신하는 메시지 전달(message passing) 방식으로 학습한다. 여러 층을 거치면 노드의 표현에 점점 더 넓은 이웃의 정보가 담기므로, 그래프의 위상과 노드 속성을 함께 반영한 벡터를 얻을 수 있다. [GraphRAG (the paradigm)](../concepts/graph-rag.md)에서는 이 표현을 이용해 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)의 부분그래프를 인코딩하거나, 질문과 관련된 노드를 점수화·랭킹하는 데 쓴다.

## 개념

GNN은 그래프를 입력으로 받아 노드·엣지·그래프 단위의 표현을 산출하며, 노드 분류, 링크 예측, 부분그래프 점수화 등 다양한 과제에 적용된다. 대표적인 변형으로 이웃 표현을 정규화해 평균하는 GCN(Graph Convolutional Network), 이웃마다 학습된 어텐션 가중치를 부여하는 GAT(Graph Attention Network), 이웃을 표본추출해 집계함으로써 대규모 그래프로 확장하는 GraphSAGE 등이 있다. 이렇게 얻은 표현은 [Dense Retrieval / Vector Search](../concepts/dense-retrieval.md)와 결합되어 검색 단위로 활용된다.

## 동작 방식

핵심 연산은 메시지 전달이다. 각 층에서 노드는 이웃 노드(및 엣지)의 표현을 모아 집계 함수로 결합하고, 이를 자신의 이전 표현과 합쳐 새 표현을 만든다. 층 수가 곧 정보가 전파되는 홉(hop) 거리에 해당하므로, 여러 층을 쌓으면 멀리 떨어진 노드의 신호까지 반영되어 [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md)에 필요한 구조적 단서를 포착할 수 있다. 학습된 표현은 노드와 질의 사이의 관련성 점수로 변환되어 랭킹에 쓰이거나, [Subgraph Extraction](subgraph-extraction.md)으로 추린 부분그래프 전체를 하나의 벡터로 인코딩하는 데 사용된다.

## GraphRAG에서의 활용

[GNN-RAG](../methods/gnn-rag.md)는 GNN을 질문에 대한 후보 답변 엔터티를 추론·랭킹하는 [Knowledge Graph QA (KGQA)](../concepts/knowledge-graph-question-answering.md) 검색기로 사용하고, 그 결과를 [Large Language Model (LLM)](../concepts/large-language-model.md)에 전달해 답을 생성한다. [G-Retriever](../methods/g-retriever.md)는 GNN으로 인코딩한 부분그래프 표현을 LLM의 입력과 결합(soft prompt)해 그래프 질의응답을 수행한다. 이처럼 GNN은 그래프의 구조 정보를 검색 단계에 직접 반영함으로써, 텍스트 임베딩만으로는 놓치기 쉬운 관계적 신호를 보완하는 역할을 한다.

## 관련 항목
- [GNN-RAG](../methods/gnn-rag.md) — GNN을 KGQA 검색기로 사용해 후보 엔터티를 랭킹하는 기법.
- [G-Retriever](../methods/g-retriever.md) — GNN으로 인코딩한 부분그래프를 LLM에 결합하는 그래프 QA 기법.
- [Subgraph Extraction](subgraph-extraction.md) — GNN 인코딩의 입력이 되는 부분그래프를 추리는 선행 단계.
- [Knowledge Graph QA (KGQA)](../concepts/knowledge-graph-question-answering.md) — GNN 검색기가 주로 적용되는 과제 유형.
- [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md) — 여러 층의 메시지 전달이 포착하는 다중 홉 구조적 추론.
- [Dense Retrieval / Vector Search](../concepts/dense-retrieval.md) — GNN 표현이 결합되는 임베딩 기반 검색 방식.
- [Knowledge Graph](../concepts/knowledge-graph.md) — GNN이 표현을 학습하는 기반 그래프 구조.
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — GNN 기반 부분그래프 인코딩·랭킹을 검색에 포함하는 상위 패러다임.
