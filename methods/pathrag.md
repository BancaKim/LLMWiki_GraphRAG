---
type: Method
title: PathRAG
description: 질의 관련 노드들 사이의 핵심 관계 경로에 집중하고 흐름 기반 가지치기로 잡음과 토큰 소비를 줄이는 그래프 기반 RAG 방법.
tags: [graphrag, retrieval, relational-path, flow-based-pruning, knowledge-graph]
authors: [Boyu Chen, Zirui Guo, Zidan Yang, Yuluo Chen, Junze Chen, Zhenghao Liu, Chuan Shi, Cheng Yang]
year: 2025
venue: arXiv preprint
arxiv: "2502.14902"
resource: https://arxiv.org/abs/2502.14902
timestamp: 2026-07-23
---

# PathRAG

PathRAG는 질의와 관련된 노드들 사이의 핵심 관계 경로(relational path)에 집중하여 그래프 기반 RAG의 노이즈와 토큰 소비를 줄이는 [GraphRAG](../concepts/graph-rag.md) 방법이다. Chen 등(2025)이 제안했으며, [Microsoft GraphRAG](microsoft-graphrag.md)나 [LightRAG](lightrag.md)이 검색한 정보에 잡음과 중복이 많다는 문제의식에서 출발한다. 흐름 기반 가지치기(flow-based pruning)로 핵심 경로를 선별한 뒤 이를 텍스트 프롬프트로 변환하여, LLM이 더 일관되고 맥락 인지적인 응답을 생성하도록 유도한다.

## 개요

기존 그래프 기반 [RAG (Retrieval-Augmented Generation)](../concepts/retrieval-augmented-generation.md)는 질의와 관련된 노드나 이웃 서브그래프를 폭넓게 가져오지만, 그 과정에서 관련성이 낮은 개체와 중복된 관계가 함께 딸려 와 프롬프트를 부풀리고 응답 품질을 떨어뜨린다. PathRAG는 개별 노드나 서브그래프가 아니라 노드들을 잇는 관계 경로 자체를 검색 단위로 삼아, 질의에 실제로 기여하는 연결만 남기는 데 초점을 둔다.

## 핵심 아이디어

PathRAG는 먼저 질의에서 추출한 개체들을 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)의 시작 노드로 삼고, 이들 사이를 잇는 경로들을 후보로 모은다. 이어 흐름 기반 가지치기를 적용해, 거리가 멀수록 흐름이 감쇠하는 방식으로 각 경로에 신뢰도 점수를 매기고 낮은 점수의 경로를 제거한다. 살아남은 핵심 경로들은 신뢰도 순으로 정렬되어 텍스트 프롬프트로 직렬화되는데, 이 경로 기반 프롬프팅은 여러 노드에 걸친 멀티홉 연결 구조를 LLM에 명시적으로 전달해 답변의 논리적 흐름을 뒷받침한다.

## 기여

- 노드·서브그래프 대신 관계 경로를 검색 단위로 삼는 경로 중심 그래프 RAG를 제안했다.
- 거리 기반 감쇠를 이용한 흐름 기반 가지치기로 잡음 경로를 제거하고 토큰 소비를 줄였다.
- 경로를 신뢰도 순으로 배치하는 경로 기반 프롬프팅으로 응답의 논리적 일관성을 높였다.

## 강점과 한계

강점은 지역·전역을 아우르는 질의에서 잡음과 중복을 줄여 더 적은 토큰으로 일관된 답을 낸다는 점이다. 한계로는 경로 탐색과 점수화가 그래프 구축 품질에 의존하고, 후보 경로 수가 많아지면 가지치기 비용이 커질 수 있다는 점이 있다.

## 관련 항목

- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — PathRAG가 구체화하는 상위 패러다임이다.
- [Microsoft GraphRAG](microsoft-graphrag.md) — PathRAG가 잡음·중복 문제로 지목한 커뮤니티 요약 시스템이다.
- [LightRAG](lightrag.md) — PathRAG가 비교 대상으로 삼는 경량 그래프 RAG 방법이다.
- [Reasoning on Graphs (RoG)](reasoning-on-graphs.md) — 관계 경로를 계획으로 활용하는 관련 방법이다.
- [Graph Traversal Reasoning](../techniques/graph-traversal-reasoning.md) — 경로 후보를 모으는 그래프 순회 기법이다.
- [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md) — 관계 경로가 지원하는 다단계 추론이다.
- [Graph RAG: A Survey (Peng et al.)](../surveys/graph-rag-survey.md) — PathRAG를 더 넓은 지형 속에 위치시킨다.

## 참고문헌

- Chen, B., Guo, Z., Yang, Z., Chen, Y., Chen, J., Liu, Z., Shi, C., & Yang, C. (2025). *PathRAG: Pruning Graph-based Retrieval Augmented Generation with Relational Paths*. arXiv preprint. arXiv:2502.14902 — https://arxiv.org/abs/2502.14902
