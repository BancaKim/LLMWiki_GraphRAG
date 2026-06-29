---
type: Method
title: LightRAG
description: 코퍼스에서 구축한 KG 인덱싱과 이중 수준(저수준·고수준) 검색을 결합하고 증분 그래프 갱신을 지원하는 그래프 기반 RAG 방법.
tags: [graphrag, retrieval, knowledge-graph, dual-level-retrieval, incremental-indexing]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2410.05779
authors: [Zirui Guo, Lianghao Xia, Yanhua Yu, Tu Ao, Chao Huang]
year: 2024
venue: EMNLP 2025
arxiv: "2410.05779"
---

# LightRAG

LightRAG은 코퍼스에서 구축한 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)로 [RAG (검색 증강 생성)](../concepts/retrieval-augmented-generation.md)를 보강하는 [GraphRAG](../concepts/graph-rag.md) 방법이다. 그래프 기반 텍스트 인덱싱과, 세밀한 사실과 넓은 주제 맥락을 함께 가져오는 이중 수준(dual-level) 검색 기법을 결합한다. Guo et al. (2024)이 제안했으며, [Microsoft GraphRAG](microsoft-graphrag.md) 같은 커뮤니티 요약 파이프라인보다 단순하고 빠른 대안으로 제시되었다.

## 개요

기존 RAG는 평평한 텍스트 청크를 검색하기 때문에 개체들 사이의 관계적 의존성을 놓칠 수 있다. LightRAG은 대신 [LLM](../concepts/large-language-model.md)으로 코퍼스에서 개체와 관계를 추출해 그래프 인덱스를 구성하고, 노드와 엣지의 벡터 임베딩도 함께 유지한다. 이후 검색과 생성은 고립된 청크가 아니라 이 결합된 구조에 기반한다.

## 핵심 아이디어 / 동작 방식

인덱싱 단계에서 LightRAG은 [개체·관계 추출 (Entity & Relationship Extraction)](../techniques/entity-relationship-extraction.md)로 그래프를 만들고 키-값 프로파일로 노드를 중복 제거한다. 질의 시점에는 두 종류의 키를 생성한다. 특정 개체와 그 인접 관계를 겨냥하는 저수준 키와, 더 넓은 주제를 겨냥하는 고수준 키다. 이 키들은 그래프의 개체와 엣지에 대한 [밀집 검색 (Dense Retrieval)](../concepts/dense-retrieval.md)을 구동하며, 매칭된 노드는 이웃을 따라 확장되어 벡터 검색과 그래프 구조를 결합하는 [하이브리드 검색 (Hybrid Retrieval)](../techniques/hybrid-retrieval.md) 형태를 이룬다. 새 문서는 증분 인덱싱으로 통합된다. 지역 그래프를 기존 그래프에 집합 병합으로 합쳐 전역 인덱스를 다시 만들지 않는다.

## 기여

- 저수준(구체적) 질의와 고수준(추상적) 질의를 통합하는 이중 수준 검색 패러다임을 제시한다.
- 그래프 구조와 벡터 임베딩을 통합해 개체·관계 수준의 검색을 가능하게 한다.
- 전체 인덱스를 재구성하지 않고 새 데이터를 추가하는 증분 갱신 알고리즘으로 유지 비용을 낮춘다.

## 강점과 한계

LightRAG은 무거운 그래프 파이프라인보다 낮은 인덱싱·질의 비용으로 강한 효과를 보고하며, 증분 갱신은 변화하는 코퍼스에 적합하다. 한계로는 그래프 품질이 LLM 추출 정확도에 의존한다는 점, 그리고 단순 RAG에 비해 그래프 저장소와 벡터 저장소를 함께 유지해야 하는 복잡성이 있다.

## 관련 항목
- [GraphRAG (패러다임)](../concepts/graph-rag.md) — LightRAG이 구체화하는 더 넓은 패러다임이다.
- [Microsoft GraphRAG](microsoft-graphrag.md) — LightRAG이 비교 대상으로 삼는 커뮤니티 요약 시스템이다.
- [LazyGraphRAG](lazygraphrag.md) — 효율성에 초점을 둔 또 다른 GraphRAG 변형이다.
- [HippoRAG](hipporag.md) — PageRank 계열 검색을 쓰는 동시기 그래프 RAG 방법이다.
- [LightRAG (HKUDS library)](../tools/lightrag-library.md) — 이 방법의 오픈소스 구현이다.
- [Local vs Global Search](../techniques/local-and-global-search.md) — 저수준·고수준 검색이 반영하는 지역/전역 구분이다.
- [Hybrid Retrieval](../techniques/hybrid-retrieval.md) — LightRAG이 의존하는 벡터·그래프 검색의 결합이다.
- [개체·관계 추출 (Entity & Relationship Extraction)](../techniques/entity-relationship-extraction.md) — LightRAG의 그래프 인덱스를 만드는 단계다.

## 참고문헌
- Guo, Z., Xia, L., Yu, Y., Ao, T., & Huang, C. (2024). *LightRAG: Simple and Fast Retrieval-Augmented Generation*. EMNLP 2025. arXiv:2410.05779 — https://arxiv.org/abs/2410.05779
