---
type: Method
title: HyperGraphRAG
description: 지식을 하이퍼그래프로 표현해 이진 관계를 넘어 n-항(n-ary) 관계 사실을 하이퍼엣지로 담고, 하이퍼그래프 구축·검색·생성 파이프라인으로 다중 도메인에서 표준 RAG와 그래프 RAG를 능가하는 그래프 기반 RAG 방법.
tags: [graphrag, retrieval, knowledge-graph, hypergraph, n-ary-relation]
authors: [Haoran Luo, Haihong E, Guanting Chen, Yandan Zheng, Xiaobao Wu, Yikai Guo, Qika Lin, Yu Feng, Zemin Kuang, Meina Song, Yifan Zhu, Luu Anh Tuan]
year: 2025
venue: NeurIPS 2025
arxiv: "2503.21322"
resource: https://arxiv.org/abs/2503.21322
timestamp: 2026-07-23
---

# HyperGraphRAG

HyperGraphRAG는 지식을 하이퍼그래프 구조로 표현하는 [GraphRAG](../concepts/graph-rag.md) 방법으로, 각 엣지가 두 개체만 잇는 이진(pairwise) 관계의 한계를 넘어 여러 개체가 얽힌 n-항(n-ary) 관계 사실을 하이퍼엣지로 나타낸다. 파이프라인은 하이퍼그래프 구축 → 하이퍼그래프 검색 → 하이퍼그래프 기반 생성의 세 단계로 구성된다. Luo et al.(2025)이 제안했으며 NeurIPS 2025에 게재되었다.

## 개요

기존 그래프 기반 [RAG](../concepts/retrieval-augmented-generation.md)는 [지식 그래프](../concepts/knowledge-graph.md)의 엣지가 두 노드만 연결하기 때문에, 실제 지식에 흔한 다항 관계(예: 특정 조건·용량·환자군에 걸친 의학적 사실)를 하나의 단위로 담기 어렵다. 이렇게 다항 사실을 여러 이진 엣지로 쪼개면 맥락이 파편화되고 검색 정확도가 떨어진다. HyperGraphRAG는 하나의 하이퍼엣지가 임의 개수의 개체를 동시에 묶도록 하여 사실의 온전한 구조를 보존한다.

## 핵심 아이디어

구축 단계에서 [LLM](../concepts/large-language-model.md)이 문서로부터 n-항 관계 사실을 추출해, 개체 집합과 이를 잇는 하이퍼엣지로 이뤄진 하이퍼그래프를 만든다. 이는 이진 관계에 한정된 통상적 개체·관계 추출을 확장한 형태다. 검색 단계에서는 질의와 관련된 개체와 하이퍼엣지를 함께 선택해, 하나의 사실에 연결된 모든 개체를 통째로 회수한다. 생성 단계에서는 회수된 하이퍼그래프 구조를 근거로 응답을 만들어, 파편화된 청크가 아니라 완결된 다항 사실에 답을 정박시킨다.

## 기여

- 이진 관계를 넘어 n-항 관계 사실을 하이퍼엣지로 표현하는 하이퍼그래프 기반 지식 표현을 제안했다.
- 하이퍼그래프 구축·검색·생성으로 이어지는 완결된 파이프라인을 설계했다.
- 의학·농업·컴퓨터과학·법률 도메인 실험에서 표준 RAG 및 [Microsoft GraphRAG](microsoft-graphrag.md) 등 그래프 기반 RAG 대비 정확도와 생성 품질 향상을 보였다.

## 강점과 한계

강점은 다항 사실의 구조를 보존해 멀티홉 추론이 필요한 질의에서 맥락 손실과 환각을 줄인다는 점이다. 여러 도메인에서 일관된 향상을 보고한 점도 강점으로 꼽힌다. 한계로는 하이퍼그래프 추출과 색인이 이진 그래프보다 복잡해 구축 비용이 크고, 하이퍼엣지 추출 품질이 LLM의 성능에 의존한다는 점이 있다.

## 관련 항목

- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — HyperGraphRAG가 속하는 상위 패러다임
- [Microsoft GraphRAG](microsoft-graphrag.md) — 이진 관계 그래프를 쓰는 대표 그래프 RAG로 비교 대상이 된다
- [LightRAG](lightrag.md) — 그래프 인덱싱과 이중 검색을 결합한 경량 그래프 RAG
- [MedGraphRAG](medgraphrag.md) — HyperGraphRAG의 의학 실험과 맞닿는 의료 도메인 그래프 RAG
- [Entity & Relationship Extraction](../techniques/entity-relationship-extraction.md) — 하이퍼그래프 구축이 다항 관계로 확장하는 추출 단계
- [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md) — 하이퍼엣지가 지원하려는 추론 유형
- [Graph RAG: A Survey (Peng et al.)](../surveys/graph-rag-survey.md) — 그래프 RAG 지형 속 위치를 잡아 준다

## 참고문헌

- Luo, H., E, H., Chen, G., Zheng, Y., Wu, X., Guo, Y., Lin, Q., Feng, Y., Kuang, Z., Song, M., Zhu, Y., & Tuan, L. A. (2025). *HyperGraphRAG: Retrieval-Augmented Generation via Hypergraph-Structured Knowledge Representation*. NeurIPS 2025. arXiv:2503.21322 — https://arxiv.org/abs/2503.21322
