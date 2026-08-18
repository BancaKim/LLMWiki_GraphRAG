---
type: Method
title: LinearRAG
description: 관계 추출을 배제한 계층 그래프 Tri-Graph를 코퍼스 크기에 선형으로 구축해, 대규모 코퍼스에서도 저비용·고신뢰 인덱싱과 정밀한 구절 검색을 제공하는 그래프 기반 RAG 프레임워크.
tags: [graphrag, retrieval, knowledge-graph, relation-free, scalability]
authors: [Luyao Zhuang, Shengyuan Chen, Yilin Xiao, Huachi Zhou, Yujing Zhang, Hao Chen, Qinggang Zhang, Xiao Huang]
year: 2025
venue: ICLR 2026
arxiv: "2510.10114"
resource: https://arxiv.org/abs/2510.10114
timestamp: 2026-08-18
---

# LinearRAG

LinearRAG는 대규모 코퍼스에서 신뢰할 수 있는 그래프 구축과 정밀한 구절 검색을 함께 달성하려는 효율 중심의 [GraphRAG (the paradigm)](../concepts/graph-rag.md) 프레임워크다. 핵심은 관계 모델링을 아예 배제한(relation-free) 계층 그래프 'Tri-Graph'로, 가벼운 엔터티 추출과 의미 연결(semantic linking)만으로 인덱스를 만든다. Zhuang et al.(2025)이 제안했으며 ICLR 2026에 게재되었다. 코드는 DEEP-PolyU/LinearRAG 저장소로 공개되어 있다.

## 개요

기존 그래프 기반 [RAG](../concepts/retrieval-augmented-generation.md)는 [Large Language Model (LLM)](../concepts/large-language-model.md)에게 문서마다 개체와 관계를 함께 추출시켜 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)를 만든다. 그러나 관계 추출은 결과가 불안정하고 표현이 제각각이어서 그래프 품질을 떨어뜨리며, 코퍼스가 커질수록 호출 횟수와 토큰 비용이 급격히 불어난다. LinearRAG는 이 병목이 관계 추출에서 비롯된다고 보고, 관계를 그래프에서 덜어 내는 쪽을 택한다.

## 핵심 아이디어

Tri-Graph는 원본 구절, 엔터티, 그리고 이들을 잇는 의미 연결로 이루어진 계층 구조다. 구축 단계에서는 [Text Chunking (청킹)](../concepts/text-chunking.md)으로 나눈 구절에서 엔터티만 가볍게 추출하고, 관계 문장을 생성하는 대신 [Text Embedding (텍스트 임베딩)](../concepts/text-embedding.md) 기반의 의미 유사도로 엔터티와 구절을 연결한다. 관계 생성이 없으므로 그래프 구축 비용은 코퍼스 크기에 선형으로 확장(linear scaling)되고 추가 토큰 소비가 발생하지 않는다. 검색 단계에서는 질의에서 얻은 엔터티를 그래프의 진입점으로 삼아 관련 구절로 활성화를 전파하고, 답에 필요한 원본 구절만 정밀하게 회수한다.

## 기여

- 관계 추출 없이 엔터티와 의미 연결만으로 구성되는 계층 그래프 Tri-Graph를 제안했다.
- 그래프 구축을 코퍼스 크기에 선형이고 추가 토큰 비용이 없는 절차로 만들어, 대규모 코퍼스 인덱싱을 경제적으로 바꿨다.
- 엔터티에서 구절로 이어지는 검색 경로를 설계해, 요약이 아닌 원본 구절 수준의 정밀한 근거 회수를 지원한다.

## 강점과 한계

강점은 비용과 신뢰성을 동시에 잡는다는 데 있다. 관계 추출에서 오는 잡음과 토큰 폭증을 제거하므로 코퍼스가 커져도 인덱싱이 무너지지 않고, 원본 구절을 근거로 삼아 [Hallucination (환각)](../concepts/hallucination.md) 위험도 낮춘다. 한계로는 명시적 관계가 없어 관계 유형 자체를 따져야 하는 질의나 긴 추론 경로에서 표현력이 제한될 수 있고, 검색 품질이 임베딩 모델의 의미 연결 정확도에 크게 좌우된다는 점이 있다.

## 관련 항목

- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — LinearRAG가 효율 측면에서 재설계하는 상위 패러다임이다.
- [Entity & Relationship Extraction](../techniques/entity-relationship-extraction.md) — LinearRAG가 의도적으로 관계 부분을 덜어 내는 대상 단계다.
- [Knowledge Graph Construction](../techniques/knowledge-graph-construction.md) — Tri-Graph 구축이 대체하려는 기존 인덱싱 절차다.
- [Microsoft GraphRAG](microsoft-graphrag.md) — LLM 관계 추출과 커뮤니티 요약에 의존하는 대표적 비교 대상이다.
- [LightRAG](lightrag.md) — 비용 절감을 노린 또 다른 경량 그래프 RAG로 문제의식을 공유한다.
- [MiniRAG](minirag.md) — 소형 모델과 저자원 환경을 겨냥한 효율 지향 그래프 RAG다.
- [Dense Retrieval / Vector Search](../concepts/dense-retrieval.md) — 의미 연결과 구절 회수의 기반이 되는 검색 방식이다.
- [LogicRAG](logicrag.md) — 그래프 구축 비용 문제에 대해 '사전 구축 자체를 없애는' 반대 노선의 대안이다.
- [When to use Graphs in RAG](../surveys/when-to-use-graphs-in-rag.md) — 이런 효율 개선이 실제로 이득이 되는 조건을 따진 분석이다.

## 참고문헌

- Zhuang, L., Chen, S., Xiao, Y., Zhou, H., Zhang, Y., Chen, H., Zhang, Q., & Huang, X. (2025). *LinearRAG: Linear Graph Retrieval Augmented Generation on Large-scale Corpora*. ICLR 2026. arXiv:2510.10114 — https://arxiv.org/abs/2510.10114
- 코드: https://github.com/DEEP-PolyU/LinearRAG
