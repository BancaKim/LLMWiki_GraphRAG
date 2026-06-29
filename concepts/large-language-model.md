---
type: Concept
title: Large Language Model (LLM)
description: 대규모 텍스트로 사전학습된 트랜스포머 기반 생성 모델로, 다음 토큰을 예측하도록 학습되어 자연어를 이해·생성하지만 매개변수에 갇힌 지식과 제한된 컨텍스트 윈도 때문에 외부 지식 보강이 필요하다.
tags: [large-language-model, transformer, generation, rag, foundational]
timestamp: 2026-06-29
---

# Large Language Model (LLM)

LLM(거대 언어 모델, Large Language Model)은 방대한 텍스트 코퍼스로 사전학습된 트랜스포머(Transformer) 기반의 생성 모델이다. 주어진 문맥에서 다음 토큰을 예측하도록 학습되며, 그 결과로 자연어를 이해하고 새로운 텍스트를 생성하는 폭넓은 능력을 얻는다. 학습으로 습득한 지식은 모델의 매개변수(parameter)에 암묵적으로 저장되는데, 이 지식은 학습 시점에 고정되고 출처를 추적하기 어렵다. 이 한계가 [RAG (Retrieval-Augmented Generation)](retrieval-augmented-generation.md)와 [GraphRAG (the paradigm)](graph-rag.md) 같은 외부 지식 보강 기법의 출발점이 된다.

## 정의

LLM은 트랜스포머의 자기어텐션(self-attention) 구조를 기반으로, 입력 토큰 시퀀스가 주어졌을 때 다음 토큰의 확률 분포를 모델링한다. 대규모 비지도 사전학습으로 언어의 통계적 규칙성과 사실 지식을 매개변수에 압축해 담으며, 이렇게 저장된 지식을 매개변수 기억(parametric memory)이라 부른다. 한 번에 처리할 수 있는 토큰의 길이는 컨텍스트 윈도(context window)로 제한되며, 이 안에 들어온 정보만 생성의 근거로 삼을 수 있다.

## GraphRAG에서 중요한 이유

LLM의 매개변수 기억은 학습 시점 이후의 정보를 담지 못하고, 사적이거나 도메인 특화된 지식을 포함하지 않으며, 근거 없이 그럴듯한 답을 지어내는 [환각 (Hallucination)](hallucination.md)을 일으킬 수 있다. 또한 여러 사실을 이어 답해야 하는 [멀티홉 추론 (Multi-hop Reasoning)](multi-hop-reasoning.md)에 약하다. RAG와 GraphRAG는 외부 지식, 특히 [Knowledge Graph](knowledge-graph.md)의 구조화된 사실을 검색해 컨텍스트 윈도에 넣어 줌으로써 이러한 약점을 보완한다. 이때 LLM은 그래프 구축 단계에서 [개체·관계 추출 (Entity & Relationship Extraction)](../techniques/entity-relationship-extraction.md)을 수행하는 도구이자, 검색된 근거를 종합해 최종 답을 만드는 생성기로서 GraphRAG 파이프라인의 양 끝에 모두 관여한다.

## 실제 활용

LLM은 질의응답, 요약, 코드 생성, 대화형 어시스턴트 등 다양한 과제에 쓰인다. 지식 집약적 응용에서는 단독으로 쓰기보다 검색 시스템과 결합하는 경우가 많은데, 모델을 재학습하지 않고 검색 색인만 갱신해도 최신·전용 지식을 반영할 수 있기 때문이다. GraphRAG 계열에서는 [Microsoft GraphRAG](../methods/microsoft-graphrag.md), [LightRAG](../methods/lightrag.md) 등이 LLM을 그래프 인덱싱과 답변 생성 양쪽에 활용한다.

## 관련 항목
- [Retrieval-Augmented Generation (RAG)](retrieval-augmented-generation.md) — LLM의 고정된 매개변수 지식을 외부 검색으로 보강하는 패러다임.
- [GraphRAG (the paradigm)](graph-rag.md) — 검색 대상을 그래프 구조로 확장해 LLM을 보강하는 상위 패러다임.
- [Knowledge Graph](knowledge-graph.md) — LLM의 답변을 그라운딩하는 구조화된 외부 지식.
- [Hallucination (환각)](hallucination.md) — 매개변수 기억의 한계에서 비롯되는 LLM의 대표적 실패 양상.
- [Multi-hop Reasoning (멀티홉 추론)](multi-hop-reasoning.md) — LLM이 단독으로 취약하고 그래프 구조가 보완하는 추론 유형.
- [Entity & Relationship Extraction](../techniques/entity-relationship-extraction.md) — LLM이 그래프 구축 단계에서 수행하는 핵심 작업.
- [Unifying LLMs and KGs: A Roadmap](../surveys/llm-kg-roadmap.md) — LLM과 지식 그래프의 통합 방향을 정리한 서베이.
