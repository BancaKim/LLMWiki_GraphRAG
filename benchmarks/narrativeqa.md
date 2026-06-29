---
type: Benchmark
title: NarrativeQA
description: 책과 영화 대본 전체를 읽고 사람이 작성한 자유 형식 정답을 생성해야 하는 약 46,765개의 질의응답 쌍으로 구성된 장문 독해 벤치마크다.
tags: [benchmark, question-answering, reading-comprehension, long-context, retrieval, graphrag]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/1712.07040
authors: [Tomáš Kočiský, Jonathan Schwarz, Phil Blunsom, Chris Dyer, Karl Moritz Hermann, Gábor Melis, Edward Grefenstette]
year: 2018
venue: TACL 2018
arxiv: "1712.07040"
---

# NarrativeQA

NarrativeQA는 Kočiský et al.(2018)이 공개한 장문 독해(reading comprehension) 데이터셋이다. 책과 영화 대본 같은 긴 이야기 전체를 읽어야만 답할 수 있는 질문으로 구성되어 있으며, 표면적인 단어 일치만으로는 풀기 어려운 통합적 추론을 요구하도록 설계되었다. 1,567편의 이야기와 약 46,765개의 질의응답 쌍을 포함한다.

## 개요

이야기는 Project Gutenberg의 전문(全文) 도서와 IMSDb, DailyScript 등에서 수집한 영화 대본으로 구성된다. 각 이야기는 사람이 작성한 추상적 요약문과 짝지어지며, 작업자는 요약문만 보고 질문과 정답을 작성한다. 이 때문에 정답이 원문 한 구절에 그대로 담겨 있지 않고 이야기 전반에 분산되어 있어, 단순한 [Dense Retrieval / Vector Search](../concepts/dense-retrieval.md)나 사실형(factoid) 질의응답과 구별된다.

## 과제 및 형식

데이터셋은 두 가지 설정을 제공한다. 요약문만 읽고 답하는 비교적 짧은 설정과, 책이나 대본 전문을 읽어야 하는 긴 설정이다. 후자는 문서가 매우 길어 전체를 한 번에 모델 입력에 넣기 어렵기 때문에, 관련 부분을 먼저 찾아오는 [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md) 방식과 [Text Chunking (청킹)](../concepts/text-chunking.md)이 필요하다. 정답은 선택지나 스팬 추출이 아니라 사람이 직접 쓴 자유 형식 문장이다.

## 평가 지표

답변 생성 품질은 BLEU-1, BLEU-4, Meteor, ROUGE-L로 측정하며, 후보 문장을 순위화하는 검색형 설정에서는 MRR(Mean Reciprocal Rank)을 사용한다. 각 질문에는 보통 두 개의 사람 정답이 주어져 표현의 다양성을 반영한다.

## GraphRAG 연구에서의 활용

긴 단일 문서에 흩어진 인물·사건·관계를 통합해야 한다는 특성 때문에, NarrativeQA는 [GraphRAG (the paradigm)](../concepts/graph-rag.md) 계열 연구에서 장문 맥락 처리와 [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md) 능력을 점검하는 데 쓰인다. 특히 트리 형태로 요약을 계층화하는 [RAPTOR](../methods/raptor.md)는 NarrativeQA에서 장문 이야기에 대한 검색·요약 성능을 보고한 대표 사례다.

## 관련 항목

- [RAPTOR](../methods/raptor.md) — NarrativeQA로 장문 이야기 검색·요약 성능을 평가한 대표 기법
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — 이 벤치마크가 적용되는 연구 패러다임
- [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md) — 이야기 전반의 단서를 통합하는 능력과 관련
- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md) — 전문 설정에서 관련 부분을 검색하는 데 사용되는 방식
- [Text Chunking (청킹)](../concepts/text-chunking.md) — 긴 책·대본을 처리하기 위한 전처리 기법
- [HotpotQA](hotpotqa.md) — 함께 비교되는 독해·질의응답 벤치마크
- [Query-Focused Summarization (QFS)](../concepts/query-focused-summarization.md) — 요약 기반 답변 생성과 맞닿은 과제

## 참고문헌

- Kočiský, T., Schwarz, J., Blunsom, P., Dyer, C., Hermann, K. M., Melis, G., & Grefenstette, E. (2018). *The NarrativeQA Reading Comprehension Challenge*. TACL 2018. arXiv:1712.07040 — https://arxiv.org/abs/1712.07040
