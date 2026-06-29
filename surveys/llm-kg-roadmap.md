---
type: Survey
title: "Unifying LLMs and KGs: A Roadmap"
description: LLM과 KG의 통합을 KG-enhanced LLMs, LLM-augmented KGs, Synergized LLMs + KGs의 세 프레임워크로 정리하고 양자를 상호 보완적으로 결합하는 방향을 제시한 서베이 논문.
tags: [knowledge-graph, large-language-model, survey, taxonomy, reasoning]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2306.08302
authors: [Shirui Pan, Linhao Luo, Yufei Wang, Chen Chen, Jiapu Wang, Xindong Wu]
year: 2024
venue: IEEE Transactions on Knowledge and Data Engineering (TKDE)
arxiv: "2306.08302"
---

# Unifying LLMs and KGs: A Roadmap

"Unifying Large Language Models and Knowledge Graphs: A Roadmap"는 Shirui Pan 등이 2024년 IEEE TKDE에 발표한 서베이로, [Large Language Model (LLM)](../concepts/large-language-model.md)과 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)를 통합하는 연구 흐름을 체계적으로 정리한다. LLM이 방대한 파라미터 지식을 갖지만 [환각 (Hallucination)](../concepts/hallucination.md)과 해석 가능성 부족이라는 한계를 가지는 반면, KG는 사실을 명시적·구조적으로 저장하지만 구축과 진화가 어렵다는 점에서 양자가 상호 보완적임을 출발점으로 삼는다.

## 범위

LLM과 KG의 결합 전반을 다룬다. KG로 LLM을 보강하는 연구, LLM으로 KG 관련 과제를 수행하는 연구, 그리고 둘을 대등하게 결합하는 연구를 모두 포괄한다. KG 임베딩·완성·구축, graph-to-text 생성, [지식 그래프 질의응답 (KGQA)](../concepts/knowledge-graph-question-answering.md) 등 다운스트림 과제와 향후 연구 방향까지 조망한다.

## 다루는 내용(분류 체계)

저자들은 통합 방식을 세 프레임워크로 구분한다. (1) KG-enhanced LLMs는 사전학습·추론 단계나 학습된 지식의 해석에 KG를 주입한다. (2) LLM-augmented KGs는 LLM을 활용해 [지식 그래프 구축 (Knowledge Graph Construction)](../techniques/knowledge-graph-construction.md), [개체·관계 추출 (Entity & Relationship Extraction)](../techniques/entity-relationship-extraction.md), KG 완성, KGQA 등을 수행한다. (3) Synergized LLMs + KGs는 둘이 대등한 역할로 상호 강화하며 데이터와 지식 양쪽에 기반한 양방향 추론을 지향한다.

## 핵심 시사점

KG가 제공하는 외부의 명시적 사실은 LLM의 환각을 줄이고 추론 근거를 검증 가능하게 만든다. 반대로 LLM은 KG 구축·보완을 자동화한다. 이런 통합 관점은 이후 [GraphRAG (the paradigm)](../concepts/graph-rag.md) 및 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md) 연구의 개념적 토대가 되었다.

## 관련 항목
- [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md) — 서베이가 다루는 두 축 중 하나.
- [Large Language Model (LLM)](../concepts/large-language-model.md) — 통합의 다른 한 축.
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — KG-LLM 통합을 검색 증강 형태로 구체화한 후속 패러다임.
- [Graph RAG: A Survey (Peng et al.)](graph-rag-survey.md) — 그래프 기반 RAG로 초점을 좁힌 인접 서베이.
- [Knowledge Graph QA (KGQA)](../concepts/knowledge-graph-question-answering.md) — LLM-augmented KGs가 다루는 핵심 과제.
- [Reasoning on Graphs (RoG)](../methods/reasoning-on-graphs.md) — 통합 추론 관점을 구현한 대표 방법.
- [Think-on-Graph (ToG)](../methods/think-on-graph.md) — LLM과 KG의 상호작용형 추론 사례.
- [환각 (Hallucination)](../concepts/hallucination.md) — KG 통합이 완화하려는 핵심 문제.

## 참고문헌
- Pan, S., Luo, L., Wang, Y., Chen, C., Wang, J., & Wu, X. (2024). *Unifying Large Language Models and Knowledge Graphs: A Roadmap*. IEEE Transactions on Knowledge and Data Engineering (TKDE), 36(7), 3580–3599. arXiv:2306.08302 — https://arxiv.org/abs/2306.08302
