---
type: Method
title: HippoRAG 2
description: HippoRAG를 확장하여 패시지를 지식 그래프에 더 깊이 통합하고 밀집 검색으로 시드를 부여한 Personalized PageRank를 사용함으로써, 사실·의미파악·연상 기억 과제 전반에서 인간의 장기 기억에 더 가깝게 접근하려는 GraphRAG 기반 검색 증강 생성 방법이다.
tags: [graphrag, retrieval, knowledge-graph, personalized-pagerank, continual-learning, multi-hop-reasoning]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2502.14802
authors: [Bernal Jiménez Gutiérrez, Yiheng Shu, Weijian Qi, Sizhe Zhou, Yu Su]
year: 2025
venue: ICML 2025
arxiv: "2502.14802"
---

# HippoRAG 2

HippoRAG 2는 검색 증강 생성([RAG](../concepts/retrieval-augmented-generation.md))을 비모수적(non-parametric) 연속 학습의 한 형태로 보고, 인간의 장기 기억에 가까운 검색을 지향하는 [GraphRAG](../concepts/graph-rag.md) 방법이다. Gutiérrez et al. (2025)가 제안했으며, 선행 연구인 [HippoRAG](hipporag.md)를 확장하여 패시지를 오픈 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)에 더 긴밀하게 통합하고 검색 과정에서 [LLM](../concepts/large-language-model.md)을 더 적극적으로 활용한다. 저자들은 사실(factual), 의미파악(sense-making), 연상(associative) 세 범주의 기억 과제 전반에서 표준 RAG 대비 개선을 보고한다.

## 개요

벡터 기반 RAG는 평면적인 청크를 독립적으로 검색하기 때문에 기억의 상호 연결된 구조를 포착하기 어렵고, 이는 연상 및 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md)의 성능을 제한한다. HippoRAG 2는 LLM을 신피질(neocortex)로, 그래프와 [Personalized PageRank](../techniques/personalized-pagerank.md)를 해마 색인(hippocampal index)으로 보는 HippoRAG의 신경생물학적 설계를 유지하되, 색인과 검색 단계를 재설계하여 패시지와 추출된 사실이 검색 과정에서 함께 작동하도록 한다.

## 핵심 아이디어 / 동작 방식

오프라인 색인 단계에서 LLM이 [개체·관계 추출 (Entity & Relationship Extraction)](../techniques/entity-relationship-extraction.md)을 수행해 패시지로부터 오픈 지식 그래프의 트리플(triple)을 구성한다. 동의어 탐지로 구(phrase) 노드를 연결하고, 패시지 자체도 그래프에 노드로 추가하여 구 노드와 함께 다룬다. 질의 시점에는 임베딩 모델이 [밀집 검색 (Dense Retrieval)](../concepts/dense-retrieval.md)으로 트리플과 패시지를 함께 점수화해 두 유형의 시드 노드를 선택한다. 이어 Personalized PageRank가 이 결합 그래프 위에서 관련도를 전파하여 구조화된 사실과 패시지 맥락을 함께 반영하는 [하이브리드 검색 (Hybrid Retrieval)](../techniques/hybrid-retrieval.md) 형태를 이룬다. 또한 LLM이 검색된 트리플을 온라인으로 필터링하여 시드의 정밀도를 높인다.

## 기여

- 그래프를 사실 전용으로만 다루지 않고 패시지를 일급 노드로 추가하여, 패시지-그래프 통합을 한층 심화했다.
- 트리플과 패시지를 모두 대상으로 한 밀집 검색으로 혼합 유형의 시드를 Personalized PageRank에 부여한다.
- 트리플에 대한 온라인 LLM 필터링을 도입하여 기존 HippoRAG 대비 검색 정밀도를 개선했다.

## 강점과 한계

HippoRAG 2는 강력한 임베딩 기준선 대비 연상 기억 과제에서 약 7%의 향상을 보고하며, 사실 및 의미파악 과제도 함께 개선하여 인간 수준 기억과의 격차를 좁힌다고 주장한다. 한계로는 LLM 추출·필터링 품질에 대한 의존, 그래프와 임베딩을 동시에 유지하는 비용, 그리고 Personalized PageRank 튜닝에 대한 민감성이 있다.

## 관련 항목

- [HippoRAG](hipporag.md) — HippoRAG 2가 직접 확장한 선행 프레임워크
- [Personalized PageRank](../techniques/personalized-pagerank.md) — 검색의 핵심을 이루는 전파 알고리즘
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — 이 방법이 구현하는 더 넓은 패러다임
- [Microsoft GraphRAG](microsoft-graphrag.md) — 커뮤니티 요약 기반의 대조적인 GraphRAG 파이프라인
- [LightRAG](lightrag.md) — 효율성에 초점을 둔 동시대의 graph-RAG 방법
- [RAPTOR](raptor.md) — 계층적 요약 기반의 또 다른 비교 대상 검색 방법
- [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md) — HippoRAG 2가 겨냥하는 연상적 추론 능력
- [하이브리드 검색 (Hybrid Retrieval)](../techniques/hybrid-retrieval.md) — 밀집 검색과 그래프 검색을 결합한 검색 방식
- [MuSiQue](../benchmarks/musique.md) — 평가에 쓰인 멀티홉 QA 벤치마크

## 참고문헌

- Gutiérrez, B. J., Shu, Y., Qi, W., Zhou, S., & Su, Y. (2025). *From RAG to Memory: Non-Parametric Continual Learning for Large Language Models*. ICML 2025 (PMLR 267:21497–21515). arXiv:2502.14802 — https://arxiv.org/abs/2502.14802
