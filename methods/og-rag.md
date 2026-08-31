---
type: Method
title: OG-RAG
description: 도메인 온톨로지에 근거해 문서를 하이퍼그래프로 표현하고, 질의마다 최소 하이퍼엣지 집합을 최적화로 골라 검색하는 온톨로지 기반 RAG 기법이다.
tags: [graphrag, ontology, neurosymbolic, hypergraph, retrieval]
authors: [Kartik Sharma, Peeyush Kumar, Yunqing Li]
year: 2025
venue: EMNLP 2025 (Main)
arxiv: "2412.15235"
resource: https://arxiv.org/abs/2412.15235
timestamp: 2026-08-31
---

# OG-RAG

OG-RAG(Ontology-Grounded RAG)는 검색의 근거를 **도메인 온톨로지**에 묶어 두는 [GraphRAG (the paradigm)](../concepts/graph-rag.md) 기법이다. LLM이 자유롭게 뽑아낸 개체·관계에 의존하는 대신, 해당 분야에서 이미 합의된 개념 체계를 뼈대로 삼아 사실을 조직한다. [온톨로지 기반·뉴로심볼릭 GraphRAG](../concepts/neurosymbolic-graphrag.md) 흐름에서 주요 학회 메인 트랙에 안착한 대표 사례로, EMNLP 2025에 게재되었다.

## 개요

전문 도메인(농업·법률·의료 등)에서는 용어와 관계가 이미 온톨로지로 정리되어 있는 경우가 많다. 그럼에도 일반적인 그래프 RAG는 [엔터티·관계 추출 (Entity & Relationship Extraction)](../techniques/entity-relationship-extraction.md)을 매번 LLM에 맡겨, 같은 개념이 다르게 표현되거나 도메인 규약과 어긋나는 그래프를 만든다. OG-RAG는 이 구조적 지식을 버리지 않고 검색 단계의 제약으로 활용한다.

## 핵심 아이디어

도메인 문서를 **하이퍼그래프(hypergraph)** 로 표현한다. 각 **하이퍼엣지**는 도메인 온톨로지에 근거해 묶인 사실 지식의 클러스터에 대응하므로, 하나의 엣지가 둘 이상의 개체를 한꺼번에 아우르는 n-항 관계를 자연스럽게 담는다. 질의가 들어오면 **최적화 알고리즘으로 최소한의 하이퍼엣지 집합**을 고른다. 즉 "관련 있는 것을 많이" 가져오는 대신, 답을 뒷받침하기에 충분한 최소 근거 묶음을 선택해 컨텍스트를 압축한다.

## 기여

- 도메인 온톨로지를 검색 인덱스의 구성 원리로 승격시켜, 사실 묶음 단위의 하이퍼그래프 표현을 제안했다.
- 질의별 최소 하이퍼엣지 집합 선택을 명시적 최적화 문제로 정식화했다.
- 네 종류의 LLM에서 **정확한 사실의 재현율 55% 향상, 응답 정확성 40% 향상**을 보고했고, 응답을 근거 문맥에 귀속(attribution)시키는 속도가 30% 빨라졌으며 사실 기반 추론 정확도가 27% 향상되었다.

## 강점과 한계

강점은 근거가 온톨로지 개념에 묶여 있어 답변의 출처 추적과 검증이 쉽고, 도메인 규약을 지키므로 [환각 (Hallucination)](../concepts/hallucination.md)이 줄어든다는 점이다. 한계는 **쓸 만한 도메인 온톨로지가 이미 존재해야 한다**는 전제로, 온톨로지가 없거나 빈약한 분야에서는 구축 비용이 선행된다. 온톨로지가 현실 변화를 못 따라가면 그 경직성이 그대로 검색 한계가 되기도 한다.

## 관련 항목

- [온톨로지 기반·뉴로심볼릭 GraphRAG](../concepts/neurosymbolic-graphrag.md) — OG-RAG가 속한 연구 흐름 전반.
- [HyperGraphRAG](hypergraphrag.md) — 같은 하이퍼그래프 표현을 쓰되 온톨로지 근거 없이 n-항 관계를 추출하는 대조군.
- [Entity & Relationship Extraction](../techniques/entity-relationship-extraction.md) — 온톨로지 제약이 대체·보정하는 단계.
- [Knowledge Graph Construction](../techniques/knowledge-graph-construction.md) — 온톨로지가 스키마를 제공하는 상위 절차.
- [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md) — 온톨로지가 유형과 제약을 부여하는 대상 구조.
- [MedGraphRAG](medgraphrag.md) — 전문 도메인 지식 체계를 활용한다는 문제의식을 공유한다.
- [Hallucination (환각)](../concepts/hallucination.md) — 온톨로지 근거가 줄이려는 문제.
- [CLAUSE](clause.md) — 같은 흐름에서 심볼릭 제약을 에이전트 예산으로 다룬 ICLR 2026 연구.

## 참고문헌

- Sharma, K., Kumar, P., & Li, Y. (2025). *OG-RAG: Ontology-Grounded Retrieval-Augmented Generation For Large Language Models*. EMNLP 2025 (Main), pp. 32962–32981, ACL Anthology 2025.emnlp-main.1674. arXiv:2412.15235 — https://arxiv.org/abs/2412.15235
- 구현: https://github.com/microsoft/ograg2
