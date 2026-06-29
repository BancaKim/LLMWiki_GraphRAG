---
type: Benchmark
title: ComplexWebQuestions (CWQ)
description: Talmor and Berant(2018)이 WebQuestionsSP를 기반으로 구축한 복잡·멀티홉 KGQA 벤치마크로, 자동 합성한 SPARQL 질의를 자연어로 의역해 만든 34,689개의 복합 질문으로 이루어져 있다.
tags: [benchmark, knowledge-graph, kgqa, multi-hop, question-answering, graphrag]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/1803.06643
authors: [Alon Talmor, Jonathan Berant]
year: 2018
venue: NAACL-HLT 2018
arxiv: "1803.06643"
---

# ComplexWebQuestions (CWQ)

ComplexWebQuestions(CWQ)는 Talmor and Berant(2018)이 공개한 복잡한 질문 응답 벤치마크다. 자연어 질문을 Freebase 위의 구조화된 질의로 풀어야 하는 [지식 그래프 QA (KGQA)](../concepts/knowledge-graph-question-answering.md) 데이터셋으로, 여러 관계를 따라가는 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md)을 요구한다. 기존 [WebQuestionsSP (WebQSP)](webqsp.md)의 단순 질문을 합성·확장해 더 어려운 합성 질문을 다룬다.

## 개요

CWQ는 WebQSP의 질문-SPARQL 쌍을 표본으로 삼아, 자동으로 더 복잡한 SPARQL 질의를 생성하고 이를 기계가 만든 질문으로 변환한 뒤, AMT(Amazon Mechanical Turk) 작업자가 자연스러운 자연어로 의역(paraphrase)하는 방식으로 구축되었다. v1.1 기준 총 34,689개 질문(train 27,734 / dev 3,480 / test 3,475)으로 구성된다. 원 논문은 질문을 검색 엔진(웹)과 상호작용하며 푸는 방식을 함께 제안해, [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md) 외부의 웹 텍스트도 지식원으로 활용할 수 있음을 보였다.

## 과제 및 형식

각 질문은 Freebase에서 실행 가능한 SPARQL 질의와 연결되어, 정답 엔티티 집합을 산출하는 것을 목표로 한다. 복잡도 유형은 합성(composition), 결합(conjunction), 비교(comparative), 최상급(superlative)의 네 가지로 분류된다. 질문은 의미 파싱 과제로 풀 수도 있고, 정답을 직접 예측하거나 웹 스니펫에 대한 독해(reading comprehension) 과제로 다룰 수도 있다.

## 평가 지표

원 논문은 상위 1개 예측의 정확도인 precision@1을 주요 지표로 사용한다. 한 질문이 여러 정답을 가질 수 있어, 예측 집합과 정답 집합을 비교하는 F1과 정확 일치 기반의 accuracy(Hits@1) 등도 후속 연구에서 함께 보고된다.

## GraphRAG 연구에서의 활용

CWQ는 [GraphRAG (the paradigm)](../concepts/graph-rag.md) 및 KGQA 계열에서 멀티홉 질의 성능을 측정하는 표준 벤치마크로 쓰인다. [Reasoning on Graphs (RoG)](../methods/reasoning-on-graphs.md), [Think-on-Graph (ToG)](../methods/think-on-graph.md), [GNN-RAG](../methods/gnn-rag.md), [SubgraphRAG](../methods/subgraphrag.md) 등 [LLM (Large Language Model)](../concepts/large-language-model.md)과 지식 그래프를 결합한 기법들이 WebQSP와 함께 CWQ 위에서 검색·추론 능력을 비교한다.

## 관련 항목

- [WebQuestionsSP (WebQSP)](webqsp.md) — CWQ가 토대로 삼아 확장한 모(母) 데이터셋
- [Knowledge Graph QA (KGQA)](../concepts/knowledge-graph-question-answering.md) — CWQ가 속한 과제 유형
- [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md) — 복합 질문이 요구하는 다중 관계 추론
- [Knowledge Graph](../concepts/knowledge-graph.md) — 질의 대상이 되는 Freebase 그래프
- [Reasoning on Graphs (RoG)](../methods/reasoning-on-graphs.md) — CWQ로 평가되는 대표 KGQA 기법
- [Think-on-Graph (ToG)](../methods/think-on-graph.md) — CWQ를 평가에 사용하는 LLM-KG 추론 기법
- [GNN-RAG](../methods/gnn-rag.md) — CWQ에서 GNN 기반 검색을 평가하는 기법
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — 이 벤치마크가 적용되는 연구 패러다임

## 참고문헌

- Talmor, A., & Berant, J. (2018). *The Web as a Knowledge-Base for Answering Complex Questions*. NAACL-HLT 2018. arXiv:1803.06643 — https://arxiv.org/abs/1803.06643
