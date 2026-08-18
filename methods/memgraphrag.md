---
type: Method
title: MemGraphRAG
description: 공유 메모리로 전역 컨텍스트를 유지하는 협업 에이전트 사회로 고품질 그래프를 구축하고, 이에 맞춘 메모리 인지 계층적 검색을 수행하는 그래프 기반 RAG 프레임워크.
tags: [graphrag, multi-agent, shared-memory, knowledge-graph, retrieval]
authors: [Chuanjie Wu, Zhishang Xiang, Yunbo Tang, Zerui Chen, Qinggang Zhang, Jinsong Su]
year: 2026
venue: KDD 2026
arxiv: "2606.00610"
resource: https://arxiv.org/abs/2606.00610
timestamp: 2026-08-18
---

# MemGraphRAG

MemGraphRAG는 공유 메모리(shared memory)에 뒷받침된 협업 에이전트 사회(society of agents)로 지식 그래프를 구축하는 [GraphRAG (the paradigm)](../concepts/graph-rag.md) 프레임워크다. 그래프 구축 단계에서 전역적 관점이 없다는 기존 방법의 구조적 약점을 정면으로 겨냥한다. Wu et al.(2026)이 제안했으며 KDD 2026에 게재되었고, 코드는 샤먼대 XMU DeepLIT 저장소로 공개되어 있다.

## 개요

표준 [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)는 정보가 잘게 파편화된 대규모 비정형 코퍼스에서 어려움을 겪는다. 그래프를 도입한 기존 방법들도 [Knowledge Graph Construction](../techniques/knowledge-graph-construction.md) 과정에서 조각(fragment) 단위의 고립된 추출에 의존하기 때문에, 각 조각이 코퍼스 전체를 보지 못한 채 개별적으로 처리된다. 그 결과 주제적으로 일관되지 않고 논리적으로 상충하며 구조적으로 파편화된 그래프가 만들어지고, 이 품질 저하가 그대로 검색 성능 하락으로 이어진다.

## 핵심 아이디어

MemGraphRAG는 추출을 단일 모델의 국소 작업이 아니라 여러 에이전트가 협업하는 사회적 과정으로 재정의한다. 공유 메모리가 [Entity & Relationship Extraction](../techniques/entity-relationship-extraction.md) 전반에 통일된 전역 컨텍스트를 제공하므로, 에이전트들은 서로 다른 조각에서 나온 진술이 충돌할 때 이를 동적으로 해소하고 코퍼스 전반의 구조적 연결성을 유지할 수 있다. 검색 단계에서는 이렇게 만들어진 그래프의 성질에 맞춘 메모리 인지 계층적 검색(memory-aware hierarchical retrieval) 알고리즘을 사용해, 메모리에 축적된 전역 정보를 단서로 삼아 계층을 오르내리며 근거를 모은다.

## 기여

- 공유 메모리로 전역 컨텍스트를 공급하는 다중 에이전트 그래프 구축 절차를 제안해, 조각 단위 고립 추출의 한계를 구조적으로 해소했다.
- 구축된 그래프에 정합적인 메모리 인지 계층적 검색 알고리즘을 함께 설계했다.
- 여러 벤치마크에서 비슷한 효율을 유지하면서 최신 베이스라인을 능가하는 성능을 보였다.

## 강점과 한계

강점은 그래프 품질을 검색 이전 단계의 일차적 문제로 규정하고, 전역 컨텍스트 공유로 논리적 충돌과 파편화를 줄인다는 점이다. [Microsoft GraphRAG](microsoft-graphrag.md) 계열이 사후 요약으로 완화하던 문제를 구축 시점에 다룬다. 한계로는 에이전트 협업과 메모리 유지가 더해지는 만큼 파이프라인이 복잡해지고, 최종 그래프의 품질이 공유 메모리의 갱신·충돌 해소 정책과 에이전트 조율 설계에 민감하게 좌우된다는 점이 있다.

## 관련 항목

- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — MemGraphRAG가 구축 품질 측면에서 개선하려는 상위 패러다임이다.
- [Knowledge Graph Construction](../techniques/knowledge-graph-construction.md) — 다중 에이전트와 공유 메모리가 개입하는 핵심 단계다.
- [Entity & Relationship Extraction](../techniques/entity-relationship-extraction.md) — 조각 단위 고립 추출의 문제가 발생하는 지점이다.
- [Microsoft GraphRAG](microsoft-graphrag.md) — 조각별 추출과 커뮤니티 요약에 의존하는 대표적 비교 대상이다.
- [Youtu-GraphRAG](youtu-graphrag.md) — 에이전트 기반 구성으로 그래프 RAG를 재설계한 동시대 방법이다.
- [GraphSearch](graphsearch.md) — 검색 단계의 다단계 전략을 강조하는 비교 관점을 제공한다.
- [GraphRAG-Bench](../benchmarks/graphrag-bench.md) — 그래프 구축 품질과 검색 성능을 함께 평가하는 벤치마크다.

## 참고문헌

- Wu, C., Xiang, Z., Tang, Y., Chen, Z., Zhang, Q., & Su, J. (2026). *MemGraphRAG: Memory-based Multi-Agent System for Graph Retrieval-Augmented Generation*. KDD 2026. arXiv:2606.00610 — https://arxiv.org/abs/2606.00610
- 코드: https://github.com/XMUDeepLIT/MemGraphRAG
