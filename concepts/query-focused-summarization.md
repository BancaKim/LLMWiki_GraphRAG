---
type: Concept
title: Query-Focused Summarization (QFS)
description: 사용자의 질의에 초점을 맞춰 하나의 문서나 말뭉치 전체를 요약하는 과제로, 특정 구절을 검색하는 대신 코퍼스를 종합해 답하며 Microsoft GraphRAG가 겨냥하는 전역 sensemaking의 핵심 문제 정의이다.
tags: [query-focused-summarization, summarization, graphrag, retrieval, sensemaking]
timestamp: 2026-06-29
---

# Query-Focused Summarization (QFS)

Query-Focused Summarization(QFS, 질의 초점 요약)은 주어진 질의(query)에 관련된 정보를 중심으로 문서나 말뭉치를 요약하는 자연어 처리 과제이다. 질의와 무관하게 전체 내용을 압축하는 일반 요약(generic summarization)과 달리, 사용자의 관심사에 맞춘 응답을 생성하는 데 목표를 둔다. 답이 소수의 구절에 국한되지 않고 여러 출처에 흩어져 있을 때, 이를 종합해 하나의 응답으로 엮어야 한다는 점이 특징이다.

## 정의

QFS의 입력은 질의와 하나 이상의 원본 문서이며, 출력은 그 질의에 답하도록 다듬어진 요약문이다. "이 데이터셋의 주요 주제는 무엇인가?"처럼 답이 코퍼스 전반에 퍼져 있는 *전역(global)* 질문이 전형적인 사례다. 이런 질문은 특정 사실을 찾는 [Knowledge Graph QA (KGQA)](knowledge-graph-question-answering.md)나 단편 검색과 달리, 정답이 어느 한 [청크 (Text Chunking)](text-chunking.md)에 담겨 있지 않으므로 검색만으로는 풀리지 않는다.

## GraphRAG에서 중요한 이유

표준 [RAG (Retrieval-Augmented Generation)](retrieval-augmented-generation.md)는 [Dense Retrieval / Vector Search](dense-retrieval.md)로 상위 몇 개 구절을 가져와 답하므로, 코퍼스 전체를 조망해야 하는 전역 질문에서는 약하다. [Microsoft GraphRAG](../methods/microsoft-graphrag.md)는 이 한계를 QFS 문제로 규정하고, [Community Summarization](../techniques/community-summarization.md)으로 미리 만든 요약을 [Local vs Global Search](../techniques/local-and-global-search.md)의 전역 검색으로 결합해 답한다. 즉 QFS는 [GraphRAG (the paradigm)](graph-rag.md)가 평면 벡터 검색 대비 가지는 차별점을 설명하는 과제 정의 역할을 한다.

## 실제 활용

QFS는 보고서 생성, 의사결정 지원, 대규모 문헌 검토처럼 단일 답이 아니라 종합적 개관이 필요한 상황에 쓰인다. 평가에는 서사 전체 이해를 요구하는 [NarrativeQA](../benchmarks/narrativeqa.md) 같은 벤치마크가 활용되며, 응답의 포괄성·다양성을 [LLM (Large Language Model)](large-language-model.md) 심사로 비교하기도 한다.

## 관련 항목
- [Microsoft GraphRAG](../methods/microsoft-graphrag.md) — QFS를 전역 sensemaking 과제로 정의하고 표적으로 삼은 대표 기법
- [GraphRAG (the paradigm)](graph-rag.md) — 전역 질문에서 QFS로 답하는 설계 방향을 공유하는 패러다임
- [Retrieval-Augmented Generation (RAG)](retrieval-augmented-generation.md) — 단편 검색 중심으로 전역 QFS에 약점을 보이는 상위 개념
- [Community Summarization](../techniques/community-summarization.md) — GraphRAG가 QFS를 위해 미리 계산하는 요약 기술
- [Local vs Global Search](../techniques/local-and-global-search.md) — QFS형 전역 질문과 국소 질문을 구분하는 질의 전략
- [Dense Retrieval / Vector Search](dense-retrieval.md) — 전역 요약에서 한계를 보이는 표준 검색 방식
- [NarrativeQA](../benchmarks/narrativeqa.md) — 종합적 이해를 요구해 QFS 평가에 쓰이는 벤치마크
