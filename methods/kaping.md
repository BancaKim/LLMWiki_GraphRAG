---
type: Method
title: KAPING
description: 질문에서 추출한 개체 주변의 지식 그래프 트리플을 의미 유사도로 골라 프롬프트에 덧붙임으로써, 별도 학습 없이 LLM의 영샷 지식 그래프 질의응답 성능을 끌어올리는 프레임워크다.
tags: [graphrag, retrieval, knowledge-graph, knowledge-graph-qa, zero-shot, llm]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2306.04136
authors: [Jinheon Baek, Alham Fikri Aji, Amir Saffari]
year: 2023
venue: "NLRSE Workshop @ ACL 2023"
arxiv: "2306.04136"
---

# KAPING

KAPING(Knowledge-Augmented language model PromptING)은 [LLM](../concepts/large-language-model.md)에 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)에서 가져온 사실을 프롬프트로 주입해 영샷(zero-shot) [KGQA](../concepts/knowledge-graph-question-answering.md)를 수행하는 프레임워크다. 질문과 연결된 KG 트리플을 검색해 텍스트로 변환한 뒤 입력 프롬프트 앞에 덧붙이는 방식으로, 모델 학습이나 미세조정 없이 동작한다. Baek et al.(2023)이 ACL 2023의 NLRSE 워크숍에서 제안했다.

## 개요

LLM은 사전학습에 담긴 지식만으로 사실 질의에 답할 때 [환각 (Hallucination)](../concepts/hallucination.md)을 일으키거나 최신·세부 사실을 놓치기 쉽다. KAPING은 이를 외부 KG의 사실로 보강한다. 핵심은 질문에 관련된 트리플만 골라 프롬프트에 넣는 것으로, 이는 [RAG](../concepts/retrieval-augmented-generation.md)의 발상을 구조화된 지식 그래프에 적용한 사례다. 저자들은 이를 학습이 필요 없는 첫 KG 보강 LLM KGQA 기법으로 제시한다.

## 핵심 아이디어 / 동작 방식

먼저 질문에서 개체(entity)를 인식하고 이를 KG의 노드에 매칭한 뒤, 그 개체 주변의 트리플(주어-관계-목적어)을 모은다. 이 후보 트리플들을 텍스트 문자열로 변환(verbalize)하고, 질문과 각 트리플을 임베딩 공간에 표현한다. 그다음 질문 임베딩과 가까운 상위 트리플만 의미 유사도로 추려, 관련 없는 사실로 LLM이 흐트러지지 않게 한다. 이렇게 선택된 트리플을 입력 질문 앞에 프롬프트로 덧붙여 LLM이 답을 생성하게 한다. 검색기는 별도 학습 없는 임베딩 기반 [밀집 검색 (Dense Retrieval)](../concepts/dense-retrieval.md) 방식을 쓴다.

## 기여

- 학습이나 미세조정 없이 KG 사실을 프롬프트로 주입하는 영샷 KGQA 프레임워크 제안.
- 트리플을 텍스트로 변환하고 질문과의 의미 유사도로 선별하는 단순한 검색-증강 파이프라인 제시.
- T5, T0, OPT, GPT-3 등 여러 LLM과 WebQSP, Mintaka 벤치마크에서 지식 증강이 성능을 끌어올림을 확인.

## 강점과 한계

KAPING은 추가 학습 비용 없이 적용되며 구조가 단순해 다양한 LLM에 쉽게 결합된다. 다만 성능이 질문 개체 인식과 KG 매칭의 정확도, 그리고 관련 트리플을 골라내는 검색기의 품질에 크게 의존한다. 학습 없는 유사도 검색이라 복잡한 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md)에는 약하며, 답을 담은 트리플이 검색되지 않으면 보강 효과가 사라진다. 이후 [Reasoning on Graphs (RoG)](reasoning-on-graphs.md)나 [Think-on-Graph (ToG)](think-on-graph.md)처럼 그래프를 다단계로 탐색·추론하는 기법으로 발전한다.

## 관련 항목
- [GraphRAG (패러다임)](../concepts/graph-rag.md) — 그래프 지식을 검색해 LLM에 결합하는 상위 패러다임
- [KGQA (Knowledge Graph QA)](../concepts/knowledge-graph-question-answering.md) — KAPING이 다루는 과제 설정
- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md) — 외부 지식을 프롬프트로 결합하는 기반 발상
- [밀집 검색 (Dense Retrieval)](../concepts/dense-retrieval.md) — 트리플과 질문을 임베딩으로 비교하는 검색 방식
- [환각 (Hallucination)](../concepts/hallucination.md) — KG 사실 주입으로 완화하려는 문제
- [StructGPT](structgpt.md) — 구조화 데이터를 LLM 추론에 결합하는 학습 없는 인접 기법
- [Think-on-Graph (ToG)](think-on-graph.md) — 그래프를 반복 탐색하며 추론하는 후속 발전 기법
- [WebQSP](../benchmarks/webqsp.md) — KAPING의 KGQA 평가에 쓰인 벤치마크

## 참고문헌
- Baek, J., Aji, A. F., & Saffari, A. (2023). *Knowledge-Augmented Language Model Prompting for Zero-Shot Knowledge Graph Question Answering*. Proceedings of the 1st Workshop on Natural Language Reasoning and Structured Explanations (NLRSE 2023), ACL, pp. 78–106. arXiv:2306.04136 — https://arxiv.org/abs/2306.04136
