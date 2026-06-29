---
type: Method
title: G-Retriever
description: 텍스트 속성을 가진 그래프에 대한 질의응답을 위해 GNN, LLM, RAG를 결합한 기법으로, Prize-Collecting Steiner Tree로 관련 부분그래프를 검색하고 소프트 프롬프팅으로 LLM에 주입한다.
tags: [graphrag, retrieval, graph-neural-network, knowledge-graph-qa, subgraph-extraction, soft-prompting]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2402.07630
authors: [Xiaoxin He, Yijun Tian, Yifei Sun, Nitesh V. Chawla, Thomas Laurent, Yann LeCun, Xavier Bresson, Bryan Hooi]
year: 2024
venue: NeurIPS 2024
arxiv: "2402.07630"
---

# G-Retriever

G-Retriever는 텍스트 속성을 가진 그래프(textual graph)에 대해 대화형으로 질문하고 답을 받는 것을 목표로 하는 [GraphRAG](../concepts/graph-rag.md) 기법이다. [GNN (Graph Neural Network)](../techniques/graph-neural-network.md), [LLM](../concepts/large-language-model.md), [RAG](../concepts/retrieval-augmented-generation.md)의 장점을 하나의 파이프라인으로 결합하여, 그래프의 일부분만을 선택적으로 검색해 답변 근거로 사용한다. He et al.(2024)이 제안했으며, 일반적인 텍스트 그래프를 다루는 최초의 RAG 접근으로 소개되었다.

## 개요

LLM을 그래프 질의응답에 그대로 쓰면 그래프 전체를 텍스트로 펼쳐 넣어야 하므로 LLM의 컨텍스트 창을 초과하기 쉽고, 그래프에 없는 사실을 지어내는 [환각 (Hallucination)](../concepts/hallucination.md)이 발생하기 쉽다. G-Retriever는 질문과 관련된 부분만 검색해 입력하는 RAG 설계로 이 문제를 완화하며, 논문은 기준선 대비 환각을 약 54% 줄였다고 보고한다. 평가는 ExplaGraphs, SceneGraphs, [WebQSP (WebQuestionsSP)](../benchmarks/webqsp.md)를 묶은 GraphQA 벤치마크에서 이뤄졌다.

## 핵심 아이디어 / 동작 방식

검색 단계에서는 [텍스트 임베딩 (Text Embedding)](../concepts/text-embedding.md)으로 질문과 노드·간선의 유사도를 구해 점수를 매긴 뒤, [Prize-Collecting Steiner Tree](../techniques/subgraph-extraction.md) 알고리즘으로 관련성 높은 노드의 점수(prize) 합은 키우고 간선 비용은 줄이는 연결된 부분그래프를 추출한다. 생성 단계에서는 Graph Attention Network가 이 부분그래프를 인코딩하고, 투영 계층이 그래프 토큰을 LLM의 벡터 공간에 정렬한다. LLM은 동결한 채 이 그래프 토큰을 소프트 프롬프트로 주입해 미세조정하므로, LLM의 사전학습 언어 능력을 보존하면서 그래프 이해를 강화한다.

## 기여

- GNN, LLM, RAG를 결합해 일반 텍스트 그래프에 적용 가능한 RAG 프레임워크를 제시.
- [부분그래프 추출 (Subgraph Extraction)](../techniques/subgraph-extraction.md)을 PCST 최적화 문제로 정식화하여, LLM 컨텍스트 창을 넘는 큰 그래프로도 확장 가능하게 함.
- ExplaGraphs, SceneGraphs, WebQSP를 아우르는 GraphQA 벤치마크를 구성하고, 환각 감소와 정확도 향상을 보고.

## 강점과 한계

G-Retriever는 PCST 검색으로 입력 크기를 제어하면서 그래프 구조를 GNN으로 직접 인코딩해 환각을 줄이고, 동결된 LLM에 소프트 프롬프팅만 적용해 효율적으로 학습한다. 한계로는 검색 품질이 노드·간선 임베딩과 PCST의 하이퍼파라미터에 민감하다는 점, 트리 형태의 부분그래프가 복잡한 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md) 경로를 항상 담지 못한다는 점, 그리고 그래프 인코더 학습을 위한 미세조정이 필요하다는 점이 있다.

## 관련 항목
- [GNN (Graph Neural Network)](../techniques/graph-neural-network.md) — 부분그래프를 인코딩하는 핵심 구성요소
- [부분그래프 추출 (Subgraph Extraction)](../techniques/subgraph-extraction.md) — G-Retriever가 PCST로 수행하는 검색 단계
- [GraphRAG (패러다임)](../concepts/graph-rag.md) — G-Retriever가 구현하는 상위 패러다임
- [GNN-RAG](gnn-rag.md) — GNN과 LLM을 결합하는 또 다른 graph-RAG 기법
- [GRAG](grag.md) — 부분그래프 검색을 활용하는 동시대 graph-RAG 기법
- [SubgraphRAG](subgraphrag.md) — 부분그래프 검색에 초점을 둔 관련 KGQA 기법
- [환각 (Hallucination)](../concepts/hallucination.md) — G-Retriever가 완화하려는 문제
- [WebQSP (WebQuestionsSP)](../benchmarks/webqsp.md) — GraphQA 벤치마크에 포함된 평가 데이터셋

## 참고문헌
- He, X., Tian, Y., Sun, Y., Chawla, N. V., Laurent, T., LeCun, Y., Bresson, X., & Hooi, B. (2024). *G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering*. NeurIPS 2024. arXiv:2402.07630 — https://arxiv.org/abs/2402.07630
