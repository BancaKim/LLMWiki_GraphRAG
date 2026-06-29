---
type: Method
title: RAPTOR
description: 텍스트 청크를 재귀적으로 임베딩·클러스터링·요약하여 상향식 트리를 구축하고, 추론 시 서로 다른 추상화 수준에서 정보를 검색하는 트리 기반 검색 기법이다.
tags: [retrieval, hierarchical-clustering, summarization, long-document, multi-hop-reasoning]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2401.18059
authors: [Parth Sarthi, Salman Abdullah, Aditi Tuli, Shubh Khanna, Anna Goldie, Christopher D. Manning]
year: 2024
venue: ICLR 2024
arxiv: "2401.18059"
---

# RAPTOR

RAPTOR(Recursive Abstractive Processing for Tree-Organized Retrieval)는 긴 문서를 다층 트리로 조직해 서로 다른 추상화 수준에서 정보를 가져오는 검색 기법이다. 텍스트 청크를 재귀적으로 임베딩하고 클러스터링한 뒤 요약해 상향식으로 트리를 쌓으며, 추론 시 이 트리에서 검색해 문서 전반의 정보를 통합한다. Sarthi et al.(2024)이 제안했으며, 일반적인 [RAG](../concepts/retrieval-augmented-generation.md)가 짧은 인접 청크만 가져와 문서 전체의 맥락을 놓치는 한계를 겨냥한다.

## 개요

표준 [밀집 검색 (Dense Retrieval)](../concepts/dense-retrieval.md)은 코퍼스를 짧은 [청크 (Text Chunking)](../concepts/text-chunking.md)로 나눠 독립적으로 가져오기 때문에, 긴 문서에 흩어져 있거나 여러 단락에 걸쳐 종합해야 하는 정보를 포착하기 어렵다. RAPTOR는 원본 청크를 트리의 잎(leaf)으로 두고, 그 위에 점점 더 추상적인 요약 노드를 쌓아 올린다. 이렇게 하면 세부 사실과 상위 주제를 같은 색인 안에서 함께 검색할 수 있어, 멀티스텝 추론이 필요한 질문에 유리하다.

## 핵심 아이디어 / 동작 방식

색인 단계에서 RAPTOR는 잎 청크를 [텍스트 임베딩 (Text Embedding)](../concepts/text-embedding.md)으로 표현하고, 가우시안 혼합 모델(GMM) 기반의 소프트 [계층적 클러스터링 (Hierarchical Clustering)](../techniques/hierarchical-clustering.md)으로 의미가 가까운 청크를 묶는다. 각 클러스터는 [LLM](../concepts/large-language-model.md)이 요약해 상위 노드로 만들고, 이 요약 노드를 다시 임베딩·클러스터링·요약하는 과정을 반복해 상향식 트리를 완성한다. 질의 시점에는 두 가지 방식을 쓴다. 트리를 층별로 따라 내려가며 후보를 좁히는 트리 순회(tree traversal) 방식과, 모든 층의 노드를 하나의 평면 집합으로 펼쳐 질의와의 유사도로 검색하는 축약 트리(collapsed tree) 방식이다.

## 기여

- 텍스트를 재귀적으로 요약해 다층 트리로 조직하는 새로운 검색 색인 구조 제안.
- 세부 청크와 추상적 요약을 동시에 검색해 긴 문서 전반의 맥락을 통합.
- QuALITY, [NarrativeQA](../benchmarks/narrativeqa.md), QASPER 등 장문 독해·QA 벤치마크에서 당시 최고 성능 달성(GPT-4와 결합 시 QuALITY 정확도 상당 폭 향상).

## 강점과 한계

RAPTOR는 서로 다른 추상화 수준을 함께 색인하므로 긴 문서에 대한 질의와 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md)에서 평탄한 청크 검색보다 강하다. 다만 색인 단계에서 클러스터마다 LLM 요약을 생성해야 해 구축 비용이 들고, 요약 품질이 검색 정확도에 직접 영향을 미친다. 또한 개체·관계로 이루어진 명시적 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)가 아니라 요약 트리에 기반하므로, 구조화된 관계 추적보다는 주제·맥락 통합에 적합하다.

## 관련 항목
- [계층적 클러스터링 (Hierarchical Clustering)](../techniques/hierarchical-clustering.md) — RAPTOR 트리를 쌓는 핵심 기법
- [GraphRAG (패러다임)](../concepts/graph-rag.md) — RAPTOR가 비교·대조되는 상위 graph 기반 검색 패러다임
- [Microsoft GraphRAG](microsoft-graphrag.md) — 커뮤니티 요약으로 계층 구조를 만드는 점에서 유사한 graph-RAG 파이프라인
- [HippoRAG](hipporag.md) — 같은 시기 멀티홉 검색을 겨냥한 비교 대상 기법
- [Text Chunking (청킹)](../concepts/text-chunking.md) — RAPTOR 트리의 잎을 이루는 입력 단위
- [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md) — RAPTOR가 강점을 보이는 질의 유형
- [NarrativeQA](../benchmarks/narrativeqa.md) — RAPTOR 평가에 쓰인 장문 독해 벤치마크
- [밀집 검색 (Dense Retrieval)](../concepts/dense-retrieval.md) — RAPTOR가 개선하려는 기존 검색 방식

## 참고문헌
- Sarthi, P., Abdullah, S., Tuli, A., Khanna, S., Goldie, A., & Manning, C. D. (2024). *RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval*. ICLR 2024. arXiv:2401.18059 — https://arxiv.org/abs/2401.18059
