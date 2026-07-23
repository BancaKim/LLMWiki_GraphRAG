---
type: Method
title: KAG (Knowledge Augmented Generation)
description: 지식 그래프와 벡터 검색을 결합해 LLM과 KG를 양방향으로 강화하는, 법률·의료·행정 등 전문 도메인 지식 서비스용 프레임워크다.
tags: [graphrag, knowledge-graph, hybrid-retrieval, logical-reasoning, domain-specialization]
authors: [Lei Liang, Mengshu Sun, Zhengke Gui, Zhongshu Zhu, Zhouyu Jiang, Ling Zhong, Yuan Qu]
year: 2024
venue: arXiv preprint (Ant Group / OpenSPG)
arxiv: "2409.13731"
resource: https://arxiv.org/abs/2409.13731
timestamp: 2026-07-23
---

# KAG (Knowledge Augmented Generation)

KAG는 법률·의료·행정과 같이 정확성과 논리적 엄밀성이 요구되는 전문 도메인의 지식 서비스를 겨냥한 [GraphRAG](../concepts/graph-rag.md) 프레임워크다. [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)의 구조적 엄밀성과 벡터 검색의 유연성을 결합해, [LLM](../concepts/large-language-model.md)과 KG를 양방향으로 강화한다. Ant Group의 OpenSPG 팀이 제안했으며, 일반적인 [RAG (Retrieval-Augmented Generation)](../concepts/retrieval-augmented-generation.md)가 전문 영역에서 겪는 사실성 및 추론 한계를 보완하려 한다.

## 개요

표준 벡터-RAG는 청크를 유사도로만 가져오기 때문에 논리적 관계나 수치·시간 제약이 얽힌 전문 질의에서 근거를 놓치기 쉽다. KAG는 KG의 명시적 스키마와 원문 청크를 함께 색인하여, 검색과 생성 모두가 구조화된 지식 위에서 이루어지도록 설계한다. 이를 통해 단순 사실 조회를 넘어 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md)이 필요한 도메인 질문을 다룬다.

## 핵심 아이디어

KAG는 다섯 축으로 구성된다. (1) LLM 친화적 지식 표현으로 스키마와 텍스트를 동시에 다루고, (2) KG와 원문 청크 사이의 상호 인덱싱(mutual-indexing)으로 구조와 원문을 연결하며, (3) 논리형식 유도 하이브리드 추론(logical-form-guided hybrid reasoning)으로 질의를 실행 가능한 논리 형식으로 분해해 [하이브리드 검색 (Hybrid Retrieval)](../techniques/hybrid-retrieval.md)과 결합한다. (4) 의미 추론 기반 지식 정합(knowledge alignment)으로 개념·개체를 정규화하고, (5) 모델 능력 강화 단계로 도메인 특화 성능을 높인다.

## 기여

지식 표현·상호 인덱싱·논리형식 추론·지식 정합·모델 강화를 하나의 파이프라인으로 통합했다. HotpotQA에서 F1 +19.6%, 2WikiMultiHopQA에서 +33.5%의 상대 향상을 보고했으며, Ant Group의 E-Government·E-Health 서비스에 실제로 적용되었다.

## 강점과 한계

강점은 논리형식 추론과 상호 인덱싱을 통해 전문 도메인에서 사실성과 다단계 추론 정확도를 함께 끌어올린다는 점, 그리고 실서비스 검증을 거쳤다는 점이다. 한계로는 KG 구축과 정합에 드는 파이프라인 복잡성과 비용, 도메인 스키마 설계 의존성, 그리고 KG 추출 품질에 결과가 좌우된다는 점을 들 수 있다.

## 관련 항목
- [Microsoft GraphRAG](microsoft-graphrag.md) — 커뮤니티 요약형과 대비되는 KG 기반 RAG 접근.
- [HippoRAG](hipporag.md) — Personalized PageRank로 멀티홉 근거를 모으는 대조적 그래프-RAG 기법.
- [LightRAG](lightrag.md) — 경량 그래프 색인을 지향하는 동시대 graph-RAG 기법.
- [Reasoning on Graphs (RoG)](reasoning-on-graphs.md) — KG 위 논리적 경로 추론을 다루는 관련 방법.
- [Knowledge Graph Construction](../techniques/knowledge-graph-construction.md) — KAG의 상호 인덱싱이 전제하는 핵심 색인 단계.
- [HotpotQA](../benchmarks/hotpotqa.md) — KAG 평가에 쓰인 멀티홉 QA 벤치마크.
- [2WikiMultiHopQA](../benchmarks/2wikimultihopqa.md) — KAG가 큰 상대 향상을 보고한 멀티홉 QA 벤치마크.

## 참고문헌
- Liang, L., Sun, M., Gui, Z., Zhu, Z., Jiang, Z., Zhong, L., Qu, Y., et al. (2024). *KAG: Boosting LLMs in Professional Domains via Knowledge Augmented Generation*. arXiv preprint (Ant Group / OpenSPG). arXiv:2409.13731 — https://arxiv.org/abs/2409.13731
