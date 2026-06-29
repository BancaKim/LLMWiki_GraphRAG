---
type: Method
title: LazyGraphRAG
description: LLM 기반 사전 요약을 색인 단계에서 생략하고 NLP 명사구 추출로 가벼운 그래프 색인을 만든 뒤, 질의 시점에 LLM 요약과 관련성 평가를 지연 수행하여 vector RAG 수준의 색인 비용으로 국소·전역 질의를 처리하는 그래프 기반 RAG 기법.
tags: [graphrag, retrieval, knowledge-graph, query-focused-summarization, cost-efficiency]
timestamp: 2026-06-29
resource: https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/
authors: [Darren Edge, Ha Trinh, Jonathan Larson]
year: 2024
venue: Microsoft Research Blog
---

# LazyGraphRAG

LazyGraphRAG는 Microsoft Research가 [Microsoft GraphRAG](microsoft-graphrag.md)의 높은 색인 비용을 완화하기 위해 제안한 [그래프 기반 RAG](../concepts/graph-rag.md) 기법이다. 핵심 발상은 "지연(lazy)"이라는 이름대로 LLM(대규모 언어 모델)을 동원하는 비싼 요약 작업을 색인 단계에서 미리 수행하지 않고 질의 시점까지 미루는 것이다. 그 결과 색인 비용은 일반 [vector RAG](../concepts/dense-retrieval.md)와 동일한 수준이면서도 그래프 구조가 주는 이점을 유지한다.

## 개요

[Microsoft GraphRAG](microsoft-graphrag.md)는 [엔터티·관계 추출 (Entity & Relationship Extraction)](../techniques/entity-relationship-extraction.md)과 모든 [커뮤니티 요약 (Community Summarization)](../techniques/community-summarization.md)을 사전 계산하기 때문에 백만 토큰 규모 말뭉치에서 LLM 호출 비용이 크게 든다. LazyGraphRAG는 이 사전 요약을 전부 생략하여, 블로그 기준으로 색인 비용을 full GraphRAG의 약 0.1% 수준, 즉 vector RAG와 동등한 수준으로 낮춘다.

## 핵심 아이디어 / 동작 방식

색인 단계에서는 LLM 대신 NLP 명사구 추출과 그래프 통계만으로 가벼운 개념 그래프를 구성한다([텍스트 청킹 (Text Chunking)](../concepts/text-chunking.md) 위에 노드를 둔다). 질의 시점에는 LLM이 질문을 하위 질의로 분해·재조합한 뒤, 벡터 유사도 기반의 best-first 탐색과 커뮤니티 구조를 따라가는 breadth-first 탐색을 결합한 반복 심화(iterative deepening) 방식으로 후보 청크를 모은다. 이어 LLM 기반 문장 단위 관련성 평가기가 상위 청크의 적합성을 판정하고, 통과한 텍스트만으로 최종 답을 생성한다. 이렇게 요약 비용을 [국소 대 전역 검색 (Local vs Global Search)](../techniques/local-and-global-search.md) 모두에서 질의 시점으로 미룬다.

## 기여

요약을 지연시키는 설계로 GraphRAG의 사전 색인 부담을 제거하면서, 국소 질의에서는 long-context vector RAG와 [DRIFT Search](../techniques/drift-search.md)를 포함한 비교 기법들을 능가하고 전역 질의에서도 경쟁력 있는 품질을 보였다고 보고한다. 또한 비용을 답변 품질과 맞바꿀 수 있는 조정 가능한 파이프라인을 제시한다.

## 강점과 한계

강점은 vector RAG 수준의 낮은 색인 비용으로 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md)이 필요한 질의와 전역 sensemaking을 함께 다룬다는 점이다. 한계로는 사전 요약을 생략하므로 질의응답 외 용도에서 엔터티·관계 요약이 주는 부가 가치를 제공하지 못하고, 비용이 색인에서 질의 시점으로 옮겨가 질의당 LLM 호출이 늘 수 있다는 점이 있다. 별도 arXiv 논문 없이 Microsoft Research 블로그로 공개되었다.

## 관련 항목
- [Microsoft GraphRAG](microsoft-graphrag.md) — LazyGraphRAG가 색인 비용을 줄이려 개선한 직접적 전신 기법.
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — LazyGraphRAG가 속한 상위 패러다임.
- [LightRAG](lightrag.md) — 마찬가지로 경량·저비용 그래프 색인을 지향하는 대안.
- [DRIFT Search](../techniques/drift-search.md) — 국소 질의 비교 대상으로 언급되는 GraphRAG 검색 방식.
- [Local vs Global Search](../techniques/local-and-global-search.md) — LazyGraphRAG가 둘 다 처리하려는 질의 구분.
- [Dense Retrieval / Vector Search](../concepts/dense-retrieval.md) — 색인 비용 기준이자 best-first 탐색의 토대.
- [Query-Focused Summarization (QFS)](../concepts/query-focused-summarization.md) — 전역 질의가 본질적으로 가지는 과제 성격.
- [microsoft/graphrag (library)](../tools/microsoft-graphrag-library.md) — 관련 코드가 공개된 공식 GraphRAG 프로젝트.

## 참고문헌
- Edge, D., Trinh, H., & Larson, J. (2024). *LazyGraphRAG: Setting a new standard for quality and cost*. Microsoft Research Blog. — https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/
