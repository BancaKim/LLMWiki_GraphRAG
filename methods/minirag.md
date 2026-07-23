---
type: Method
title: MiniRAG
description: 텍스트와 엔터티를 하나의 의미 인지 이질 그래프로 통합하고 경량 위상 강화 검색을 써서 소형 언어모델로도 잘 작동하도록 설계된 극도로 단순한 그래프 기반 RAG 방법.
tags: [graphrag, retrieval, small-language-model, heterogeneous-graph, knowledge-graph]
authors: [Tianyu Fan, Jingyuan Wang, Xubin Ren, Chao Huang]
year: 2025
venue: arXiv preprint (HKUDS)
arxiv: "2501.06713"
resource: https://arxiv.org/abs/2501.06713
timestamp: 2026-07-23
---

# MiniRAG

MiniRAG는 소형 언어모델(SLM)만으로도 잘 작동하도록 설계된 극도로 단순한 [RAG (검색 증강 생성)](../concepts/retrieval-augmented-generation.md) 방법이다. 텍스트 청크와 엔터티를 하나의 의미 인지(semantic-aware) 이질 그래프로 통합하고, 경량 위상 강화(topology-enhanced) 검색으로 지식에 효율적으로 접근한다. [LightRAG](lightrag.md)를 만든 HKUDS 팀의 후속 작업으로, 작은 모델과 저자원 환경에서도 성능 저하를 최소화하는 것을 목표로 한다.

## 개요

대형 [LLM](../concepts/large-language-model.md)에 의존하는 기존 [GraphRAG](../concepts/graph-rag.md) 파이프라인은 복잡한 의미 이해와 다단계 추론을 요구하기 때문에, 그대로 소형 모델로 옮기면 성능이 크게 떨어진다. MiniRAG는 검색이 모델의 언어 능력보다 그래프 구조 자체에 더 의존하도록 재설계해 이 격차를 줄인다.

## 핵심 아이디어

색인 단계에서 MiniRAG는 [지식 그래프 구축 (Knowledge Graph Construction)](../techniques/knowledge-graph-construction.md)을 확장해, 텍스트 청크 노드와 명명 엔터티 노드를 함께 담는 의미 인지 이질 그래프를 만든다. 각 노드에는 임베딩이 부여되어 의미 근접성이 보존된다. 질의 시점에는 위상 강화 검색이 쿼리와 관련된 엔터티에서 출발해 그래프의 연결 구조를 따라 관련 청크로 전파하므로, SLM이 정교한 의미 판단을 내리지 않아도 필요한 근거를 모을 수 있다. 이는 벡터 유사도와 그래프 경로를 함께 쓰는 하이브리드 검색의 한 형태다.

## 기여

- 텍스트와 엔터티를 하나의 이질 그래프로 통합하는 의미 인지 색인 구조를 제안한다.
- 언어 능력 대신 그래프 위상에 의존하는 경량 위상 강화 검색 기법을 제시한다.
- SLM으로도 LLM 기반 방법에 근접한 성능을 내면서 저장 공간을 크게 줄임을 보이고, 오픈소스 구현과 온디바이스 시나리오용 벤치마크를 공개한다.

## 강점과 한계

가장 큰 강점은 저자원·온디바이스 환경 적합성이다. 작은 모델과 적은 저장 공간으로도 경쟁력 있는 정확도를 유지한다. 한계로는 그래프 품질이 여전히 엔터티 추출 정확도에 의존한다는 점, 그리고 매우 복잡한 다단계 추론 질의에서는 대형 모델 기반 파이프라인에 못 미칠 수 있다는 점이 있다.

## 관련 항목
- [LightRAG](lightrag.md) — MiniRAG가 계승하고 경량화한 직전 그래프 RAG 방법이다.
- [GraphRAG (패러다임)](../concepts/graph-rag.md) — MiniRAG가 속하는 더 넓은 패러다임이다.
- [Microsoft GraphRAG](microsoft-graphrag.md) — 대형 모델 비용이 큰, 대비되는 그래프 RAG 계열이다.
- [소형·대형 언어모델 (LLM)](../concepts/large-language-model.md) — MiniRAG가 겨냥하는 SLM을 포함하는 모델 범주다.
- [Hybrid Retrieval](../techniques/hybrid-retrieval.md) — 위상 강화 검색이 취하는 벡터·그래프 결합 형태다.
- [지식 그래프 구축 (Knowledge Graph Construction)](../techniques/knowledge-graph-construction.md) — 이질 그래프 색인을 만드는 단계다.
- [LightRAG (HKUDS library)](../tools/lightrag-library.md) — 같은 팀의 관련 오픈소스 구현이다.

## 참고문헌
- Fan, T., Wang, J., Ren, X., & Huang, C. (2025). *MiniRAG: Towards Extremely Simple Retrieval-Augmented Generation*. arXiv preprint (HKUDS). arXiv:2501.06713 — https://arxiv.org/abs/2501.06713
