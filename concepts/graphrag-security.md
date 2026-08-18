---
type: Concept
title: GraphRAG 보안과 지식 포이즈닝
description: GraphRAG의 그래프 색인 자체를 표적으로 삼는 지식 포이즈닝 공격과 그 방어 과제를 다루는 2025~2026년 연구 흐름을 정리한 개념 노트다.
tags: [graphrag, security, poisoning, knowledge-graph, adversarial-attack]
timestamp: 2026-08-18
---

# GraphRAG 보안과 지식 포이즈닝

GraphRAG 보안은 그래프를 검색 근거로 삼는 시스템이 악의적으로 조작된 지식에 얼마나 취약한지를 다루는 연구 흐름이다. 2025년 "GraphRAG under Fire"를 출발점으로, 2026년 LogicPoison·KEPo·ShadowMerge에 이르기까지 [GraphRAG (the paradigm)](graph-rag.md)를 직접 표적으로 삼는 포이즈닝 공격이 잇따라 제안되었다. 이 노트는 특정 시스템이 아니라 이들이 공유하는 문제의식과 공격·방어 지형을 정리한다.

## 정의

지식 포이즈닝(knowledge poisoning)은 공격자가 코퍼스나 그래프에 조작된 내용을 심어, 검색 단계에서 그것이 근거로 선택되게 만들고 최종 답변을 원하는 방향으로 바꾸는 공격이다. 평면 [Retrieval-Augmented Generation (RAG)](retrieval-augmented-generation.md)에 대한 포이즈닝이 질의와 유사한 텍스트 조각을 벡터 색인에 밀어 넣는 데 집중했다면, GraphRAG 포이즈닝은 [지식 그래프 (Knowledge Graph)](knowledge-graph.md)의 노드·관계·커뮤니티 구조 자체를 겨냥한다.

## 왜 GraphRAG에서 중요한가

"GraphRAG under Fire"가 지적하는 것은 일종의 보안의 역설이다. 그래프 색인·검색 구조는 기존 RAG용 포이즈닝을 덜 통하게 만들지만, 바로 그 특성이 새로운 공격면을 만든다. [Entity & Relationship Extraction](../techniques/entity-relationship-extraction.md)이나 [Community Detection (Leiden)](../techniques/community-detection.md)은 문서를 정규화된 구조로 접어 넣기 때문에, 한 번 자리 잡은 조작은 여러 질의에 걸쳐 반복 사용될 수 있다. KEPo는 반대 방향에서 같은 특성을 짚는다. 주입 콘텐츠를 '검색 유도용'과 '오도용'으로 쪼개는 기존 RAG식 방법은 GraphRAG에서 작고 고립된 커뮤니티를 형성해 검색 순위가 낮아지므로, 그래프 구조를 전제한 전용 설계가 필요하다는 것이다.

## 주요 공격 유형

- **GragPoison** — 기저 지식 그래프의 공유 관계(shared relations)를 악용해, 하나의 조작 텍스트로 여러 질의를 동시에 오염시킨다.
- **LogicPoison** — 조작된 사실이나 적대적 지시문을 주입하는 대신 타입 보존 엔터티 교환으로 그래프의 암묵적 추론 위상을 교란한다. 전역 논리 허브와 질의 중심 추론 다리를 고르고, 타입 버킷 안에서 순환 치환한 뒤, 유효 추론 사슬을 끊고 오답 엔터티로 재라우팅하는 3단계 파이프라인이다.
- **KEPo** — 위의 고립 커뮤니티 문제를 우회하도록 설계된 GraphRAG 전용 포이즈닝이다.
- **ShadowMerge** — 질의 접근만 가능한 블랙박스 환경에서 그래프 기반 에이전트 메모리를 노린다. 페이로드가 구조화된 관계로 자리 잡고, 엔터티 해소와 관계 정규화를 거쳐 표적 앵커 이웃에 진입한 뒤, 다른 사용자의 질의에서 그래프 근거로 검색되어야 공격이 성립한다.

## 방어와 남은 과제

네 연구가 공통으로 시사하는 바는 방어 지점이 텍스트가 아니라 그래프에 있다는 것이다. 엔터티 해소와 관계 정규화는 중복을 줄이는 유용한 단계이지만, 동시에 외부 입력이 기존 이웃에 병합되는 통로이기도 하다. 타입 보존 교환처럼 표면 문장이 자연스럽고 타입 제약도 지키는 조작은 문장 단위 필터로 걸러 내기 어렵고, 손상이 개별 노드가 아니라 추론 경로에 있으므로 무엇을 검증 대상으로 삼을지부터 분명하지 않다. 에이전트 메모리처럼 그래프를 여러 사용자가 공유하는 설정에서는 오염의 영향이 주입자가 아닌 제3자에게 전이된다는 점도 새롭다. 그래프 무결성 검증, 출처 추적, 병합 단계의 신뢰도 관리가 앞으로의 과제로 남아 있다.

## 관련 항목
- [GraphRAG (the paradigm)](graph-rag.md) — 이 보안 논의가 대상으로 삼는 패러다임
- [지식 그래프 (Knowledge Graph)](knowledge-graph.md) — 포이즈닝의 실제 표적이 되는 데이터 구조
- [Retrieval-Augmented Generation (RAG)](retrieval-augmented-generation.md) — GraphRAG 이전 세대 포이즈닝 연구가 다루던 무대
- [Entity & Relationship Extraction](../techniques/entity-relationship-extraction.md) — 조작된 관계가 그래프로 편입되는 관문
- [Community Detection (Leiden)](../techniques/community-detection.md) — KEPo가 지적한 고립 커뮤니티 문제의 배경 기법
- [MemGraphRAG](../methods/memgraphrag.md) — ShadowMerge가 노리는 그래프 기반 에이전트 메모리에 해당하는 구현
- [Hallucination (환각)](hallucination.md) — 포이즈닝이 유발하는 오답과 구분해야 할 인접 현상

## 참고문헌
- *GraphRAG under Fire* (2025). arXiv:2501.14050 — https://arxiv.org/abs/2501.14050
- *LogicPoison: Logical Attacks on Graph Retrieval-Augmented Generation* (2026). ACL 2026 Main (Oral), ACL Anthology 2026.acl-long.252. arXiv:2604.02954 — https://arxiv.org/abs/2604.02954
- *KEPo: Knowledge Evolution Poison on Graph-based Retrieval-Augmented Generation* (2026). The ACM Web Conference (WWW) 2026. DOI 10.1145/3774904.3792547. arXiv:2603.11501 — https://arxiv.org/abs/2603.11501
- *ShadowMerge: A Novel Poisoning Attack on Graph-Based Agent Memory via Relation-Channel Conflicts* (2026). arXiv:2605.09033 — https://arxiv.org/abs/2605.09033
