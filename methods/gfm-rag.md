---
type: Method
title: GFM-RAG
description: GFM-RAG는 대규모로 사전학습한 그래프 파운데이션 모델(GFM)을 검색기로 삼아 그래프 인덱스 위에서 질의-지식 관계를 추론하고, 파인튜닝 없이 미지의 데이터셋에 zero-shot으로 적용되는 최초의 GFM 기반 RAG 방법이다.
tags: [graphrag, retrieval, graph-neural-network, multi-hop-reasoning, foundation-model, knowledge-graph]
authors: [Linhao Luo, Zicheng Zhao, Gholamreza Haffari, Dinh Phung, Chen Gong, Shirui Pan]
year: 2025
venue: NeurIPS 2025
arxiv: "2502.01113"
resource: https://arxiv.org/abs/2502.01113
timestamp: 2026-07-23
---

# GFM-RAG

GFM-RAG는 그래프 파운데이션 모델(Graph Foundation Model, GFM)을 검색기로 삼는 최초의 [GraphRAG](../concepts/graph-rag.md) 방법이다. [GNN (Graph Neural Network)](../techniques/graph-neural-network.md) 기반 리트리버가 그래프 인덱스 위에서 질의와 지식 사이의 관계를 추론하여 관련 문서를 찾아내고, 그 결과를 근거로 답을 [생성 (RAG)](../concepts/retrieval-augmented-generation.md)한다. Luo 등(2025)이 NeurIPS 2025에서 제안했으며, 파인튜닝 없이 미지의 데이터셋에 zero-shot으로 적용할 수 있는 최초의 GFM이라는 점이 특징이다.

## 개요

기존 GraphRAG 방법은 데이터셋마다 검색기를 새로 학습하거나 여러 번의 반복 검색에 의존해 일반화와 효율에서 제약이 있었다. GFM-RAG는 대규모 사전학습으로 얻은 단일 GFM을 재사용해, 다양한 도메인의 그래프 위에서 단일 단계 검색만으로 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md)을 수행하는 것을 목표로 한다.

## 핵심 아이디어

먼저 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)·문서 그래프·계층 그래프 등 다양한 구조 지식을 담을 수 있는 범용 그래프 인덱스를 구성한다. 그 위에서 GNN 기반 리트리버가 질의-지식 관계를 추론해 한 번의 순전파로 관련 문서를 검색한다. 저자들은 8M 파라미터 규모의 GFM을 60개 지식 그래프(1,400만 개 이상의 트리플)와 70만 문서를 사용해 2단계로 사전학습했다. 이렇게 학습된 GFM은 새로운 코퍼스에 대해 재학습 없이 곧바로 적용된다.

## 기여

- 그래프 파운데이션 모델을 검색기로 활용하는 최초의 GFM 기반 RAG 프레임워크를 제안했다.
- 다양한 구조 지식을 포괄하는 범용 그래프 인덱스와, 그 위에서 질의-지식 관계를 추론하는 GNN 리트리버를 설계했다.
- 대규모 2단계 사전학습으로 파인튜닝 없이 미지의 데이터셋에 zero-shot 적용이 가능하고, 단일 단계 검색으로 멀티홉 추론을 수행하는 일반화 능력을 보였다.

## 강점과 한계

강점은 데이터셋마다 검색기를 다시 학습할 필요가 없어 범용성이 높고, 반복 검색 없이 단일 단계로 멀티홉 질의를 처리해 효율적이라는 점이다. 한계로는 성능이 그래프 인덱스의 구축 품질에 의존하며, 인덱싱 단계의 비용이 여전히 요구된다는 점, 그리고 8M 규모의 GFM이 담을 수 있는 표현력과 도메인 커버리지에 상한이 있다는 점이 있다.

## 관련 항목

- [Reasoning on Graphs (RoG)](reasoning-on-graphs.md) — 1저자 Linhao Luo가 공유하는 선행 KGQA 연구
- [GNN-RAG](gnn-rag.md) — GNN을 검색기로 쓰는 유사 접근, 데이터셋별 학습에 의존하는 대조군
- [HippoRAG 2](hipporag-2.md) — 그래프 인덱스 위 단일 단계 검색을 지향하는 비교 대상
- [GNN (Graph Neural Network)](../techniques/graph-neural-network.md) — GFM 리트리버의 핵심 구성 기법
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — GFM-RAG가 속하는 상위 패러다임
- [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md) — 단일 단계 검색으로 겨냥하는 역량
- [MuSiQue](../benchmarks/musique.md) — 멀티홉 검색 성능 평가에 쓰이는 벤치마크

## 참고문헌

- Luo, L., Zhao, Z., Haffari, G., Phung, D., Gong, C., & Pan, S. (2025). *GFM-RAG: Graph Foundation Model for Retrieval Augmented Generation*. NeurIPS 2025. arXiv:2502.01113 — https://arxiv.org/abs/2502.01113
