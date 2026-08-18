---
type: Method
title: AGRAG
description: LLM 기반 엔터티 추출을 n-gram·TF-IDF 통계 방식으로 대체해 색인 단계의 환각을 없애고, 검색을 최소 비용 최대 영향(MCMI) 부분 그래프 생성 문제로 정식화한 그래프 RAG 기법이다.
tags: [graphrag, retrieval, subgraph-extraction, entity-extraction, interpretability]
authors: [Yubo Wang, Haoyang Li, Fei Teng, Lei Chen]
year: 2025
venue: arXiv preprint
arxiv: "2511.05549"
resource: https://arxiv.org/abs/2511.05549
timestamp: 2026-08-18
---

# AGRAG

AGRAG(Advanced Graph-based RAG)는 [GraphRAG (the paradigm)](../concepts/graph-rag.md) 파이프라인의 두 지점 — **그래프 구축**과 **검색** — 을 각각 다시 설계한 기법이다. 색인 단계에서는 LLM에 의존하던 [엔터티·관계 추출 (Entity & Relationship Extraction)](../techniques/entity-relationship-extraction.md)을 통계 기반 방법으로 바꿔 [환각 (Hallucination)](../concepts/hallucination.md)과 오류 전파를 차단하고, 검색 단계에서는 부분 그래프 선택을 명시적인 최적화 문제로 정식화한다.

## 개요

대부분의 그래프 RAG는 색인 시 LLM으로 엔터티를 뽑는데, 이때 생긴 잘못된 엔터티는 그래프에 그대로 굳어져 이후 모든 질의에 영향을 준다. AGRAG는 이 단계를 **결정론적(deterministic)** 으로 바꾸는 데서 출발한다. 또한 검색된 근거가 "왜" 선택됐는지 설명되지 않는다는 문제도 함께 다룬다.

## 핵심 아이디어

**색인** — LLM 추출 대신 **n-gram 열거와 TF-IDF 점수화**로 엔터티를 고른다. 같은 입력에 항상 같은 결과가 나오고 없는 개체를 지어내지 않으므로, 환각과 오류 전파가 원천적으로 차단된다.

**검색** — 그래프 추론 절차를 **MCMI(Minimum Cost Maximum Influence, 최소 비용 최대 영향) 부분 그래프 생성 문제**로 정식화한다. 생성된 MCMI [부분 그래프 (Subgraph Extraction)](../techniques/subgraph-extraction.md)는 단순한 검색 결과가 아니라 **명시적 추론 경로**로 기능해, 특정 청크가 왜 검색됐는지를 LLM에게 알려 준다. 트리 구조 추론 경로와 달리 **순환(cycle)을 포함한 복잡한 구조**를 허용하므로 추론 경로의 포괄성이 높아진다. 마지막으로 MCMI 부분 그래프를 해석 가능한 **그래프 문자열(graph string)** 로 선형화해, 영향도 점수와 의미적 간선 비용으로 각 구절·엔터티가 선택된 이유를 드러낸다.

## 기여

- 색인 단계의 LLM 엔터티 추출을 n-gram + TF-IDF 통계 방식으로 대체해 비환각·결정론적 엔터티 선택을 확보했다.
- 그래프 검색을 MCMI 부분 그래프 생성이라는 명시적 최적화 문제로 정식화했다.
- 부분 그래프를 선형화한 그래프 문자열로 **검색 근거의 해석 가능성**을 제공했다.

## 강점과 한계

강점은 색인 단계에서 LLM 호출과 그로 인한 환각을 함께 제거해 비용과 신뢰성을 동시에 개선하고, 추론 경로를 명시해 결과를 감사(audit)하기 쉽다는 점이다. 한계로는 통계 기반 추출이 문맥 의존적이거나 표현이 다양한 엔터티, 도메인 특수 용어를 LLM만큼 유연하게 포착하지 못할 수 있고, 관계의 의미적 유형이 LLM 추출만큼 풍부하지 않을 수 있다는 점이다. MCMI 부분 그래프 생성 역시 조합 최적화이므로 그래프가 커질수록 계산 부담이 는다.

## 관련 항목

- [Entity & Relationship Extraction](../techniques/entity-relationship-extraction.md) — AGRAG가 통계 방식으로 대체하는 핵심 단계다.
- [Subgraph Extraction](../techniques/subgraph-extraction.md) — MCMI 부분 그래프 생성이 속하는 기법 범주다.
- [LinearRAG](linearrag.md) — 색인 단계의 LLM 의존을 줄인다는 목표를 공유하는 접근이다.
- [SubgraphRAG](subgraphrag.md) — 검색된 부분 그래프를 LLM에 전달하는 선행 기법이다.
- [Microsoft GraphRAG](microsoft-graphrag.md) — LLM 추출과 커뮤니티 요약에 의존하는 대표 비교 대상이다.
- [Hallucination (환각)](../concepts/hallucination.md) — 색인 단계에서 차단하려는 문제다.
- [Knowledge Graph Construction](../techniques/knowledge-graph-construction.md) — 통계 기반 추출이 적용되는 상위 절차다.
- [Text Embedding (텍스트 임베딩)](../concepts/text-embedding.md) — 의미적 간선 비용 산정의 배경이 되는 표현 방식이다.

## 참고문헌

- Wang, Y., Li, H., Teng, F., & Chen, L. (2025). *AGRAG: Advanced Graph-based Retrieval-Augmented Generation for LLMs*. arXiv preprint. arXiv:2511.05549 — https://arxiv.org/abs/2511.05549
