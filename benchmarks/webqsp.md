---
type: Benchmark
title: WebQuestionsSP (WebQSP)
description: Yih et al.(2016)이 공개한 Freebase 기반 KGQA 벤치마크로, WebQuestions 질문에 SPARQL 의미 파싱과 정답을 함께 라벨링한 데이터셋이다.
tags: [benchmark, knowledge-graph, kgqa, question-answering, graphrag]
timestamp: 2026-06-29
resource: https://aclanthology.org/P16-2033/
authors: [Wen-tau Yih, Matthew Richardson, Chris Meek, Ming-Wei Chang, Jina Suh]
year: 2016
venue: ACL 2016
---

# WebQuestionsSP (WebQSP)

WebQuestionsSP(WebQSP)는 Yih et al.(2016)이 공개한 [지식 그래프 QA (KGQA)](../concepts/knowledge-graph-question-answering.md) 벤치마크다. 기존 WebQuestions 데이터셋의 질문들에 대해, 정답뿐 아니라 Freebase에서 직접 실행 가능한 SPARQL 형태의 의미 파싱(semantic parse)을 함께 라벨링한 점이 특징이다. 자연어 질문을 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md) 위의 구조화된 질의로 변환하는 능력을 평가하기 위해 만들어졌다.

## 개요

원본 WebQuestions는 정답만 제공해 의미 파싱 학습에 한계가 있었다. WebQSP는 답을 얻기까지의 추론 경로를 명시적인 SPARQL 질의로 라벨링하여 이를 보완한다. 논문은 전체 의미 파싱을 부여한 4,737개 질문과, 타당한 파싱을 만들 수 없어 부분 라벨만 단 1,073개 질문을 함께 제공한다. 모든 파싱은 표준 Freebase 엔티티 식별자를 사용하므로 Freebase 위에서 그대로 실행된다.

## 과제 및 형식

과제는 자연어 질문을 받아 Freebase에서 정답 엔티티 집합을 산출하는 것이다. 각 질문에는 토픽 엔티티(topic entity)와 SPARQL 질의가 연결되어 있어, 시스템은 정답만 예측하거나 의미 파싱을 거쳐 답을 도출하는 두 방식 모두로 평가될 수 있다. 질문 대부분은 한 개 또는 두 개의 관계를 따라가는 단순·[멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md) 경로로 풀린다. 더 복잡한 합성 질문을 다루는 [ComplexWebQuestions (CWQ)](complexwebquestions.md)는 WebQSP를 토대로 구축되었다.

## 평가 지표

평가는 예측한 정답 엔티티 집합과 정답 집합을 비교하는 방식으로 이루어진다. 한 질문이 여러 정답을 가질 수 있으므로 질문별 Precision, Recall, F1을 계산해 평균한 average F1을 주요 지표로 사용하며, 정확한 집합 일치를 보는 accuracy(Hits@1 계열)도 함께 보고된다.

## GraphRAG 연구에서의 활용

WebQSP는 [GraphRAG (the paradigm)](../concepts/graph-rag.md) 및 KGQA 계열 연구에서 표준 평가 데이터셋으로 널리 쓰인다. [Reasoning on Graphs (RoG)](../methods/reasoning-on-graphs.md), [Think-on-Graph (ToG)](../methods/think-on-graph.md), [GNN-RAG](../methods/gnn-rag.md), [SubgraphRAG](../methods/subgraphrag.md) 등은 [LLM (Large Language Model)](../concepts/large-language-model.md)과 지식 그래프를 결합한 추론·검색 성능을 WebQSP와 [ComplexWebQuestions (CWQ)](complexwebquestions.md) 위에서 비교한다.

## 관련 항목

- [Knowledge Graph QA (KGQA)](../concepts/knowledge-graph-question-answering.md) — WebQSP가 속한 과제 유형
- [ComplexWebQuestions (CWQ)](complexwebquestions.md) — WebQSP를 토대로 만든 더 복잡한 후속 벤치마크
- [Knowledge Graph](../concepts/knowledge-graph.md) — 질의 대상이 되는 Freebase 그래프
- [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md) — 일부 질문이 요구하는 다중 관계 추론
- [Reasoning on Graphs (RoG)](../methods/reasoning-on-graphs.md) — WebQSP로 평가되는 대표 KGQA 기법
- [Think-on-Graph (ToG)](../methods/think-on-graph.md) — WebQSP를 평가에 사용하는 LLM-KG 추론 기법
- [GNN-RAG](../methods/gnn-rag.md) — WebQSP에서 GNN 기반 검색을 평가하는 기법
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — 이 벤치마크가 적용되는 연구 패러다임

## 참고문헌

- Yih, W., Richardson, M., Meek, C., Chang, M.-W., & Suh, J. (2016). *The Value of Semantic Parse Labeling for Knowledge Base Question Answering*. ACL 2016. — https://aclanthology.org/P16-2033/
