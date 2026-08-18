---
type: Survey
title: When to use Graphs in RAG
description: GraphRAG가 표준 RAG 대비 실제로 효과적인 시점과 그 성공 요인을 GraphRAG-Bench를 통해 체계적으로 규명한 분석 논문이다.
tags: [graphrag, benchmark, evaluation, retrieval, analysis]
authors: [Zhishang Xiang, Chuanjie Wu, Qinggang Zhang, Shengyuan Chen, Zijin Hong, Xiao Huang, Jinsong Su]
year: 2025
venue: ICLR 2026
arxiv: "2506.05690"
resource: https://arxiv.org/abs/2506.05690
timestamp: 2026-08-18
---

# When to use Graphs in RAG

"When to use Graphs in RAG: A Comprehensive Analysis for Graph Retrieval-Augmented Generation"은 Xiang 등이 2025년에 발표한 분석 논문으로, [GraphRAG (the paradigm)](../concepts/graph-rag.md)의 효과를 낙관적 전제가 아니라 측정 결과로 따져 묻는다. 그래프 구조는 개념적으로 유망하지만, 최근 연구들은 실제 과제에서 GraphRAG가 표준(vanilla) [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)보다 오히려 못한 성능을 내는 사례를 반복적으로 보고해 왔다. 저자들은 여기서 "GraphRAG는 정말 효과적인가, 그리고 어떤 시나리오에서 그래프 구조가 측정 가능한 이득을 주는가"라는 질문을 정면으로 제기한다. 이를 검증하기 위한 도구로 GraphRAG-Bench를 제안하며, 위키에 별도로 정리된 [GraphRAG-Bench](../benchmarks/graphrag-bench.md) 벤치마크 노트와 짝을 이루는 '분석 논문'에 해당한다.

## 범위

그래프 기반 검색 파이프라인 전반이 대상이지만, 초점은 새로운 기법 제안이 아니라 기존 GraphRAG 계열과 평면적 [Dense Retrieval / Vector Search](../concepts/dense-retrieval.md) 기반 RAG의 공정한 비교에 있다. 즉 "그래프를 쓸 것인가 말 것인가"라는 설계 의사결정 자체를 연구 대상으로 삼는다.

## 무엇을 다루는가

핵심은 GraphRAG-Bench다. 이 벤치마크는 GraphRAG 모델을 계층적 지식 검색과 심층 맥락 추론이라는 두 축에서 평가하며, 난이도가 단계적으로 올라가는 과제군을 포함한다. 사실 검색(fact retrieval)에서 출발해 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md)이 필요한 복잡 추론(complex reasoning), 맥락 요약(contextual summarization), 그리고 창의적 생성(creative generation)으로 이어지는 구성이다. 저자들은 이 위에서 GraphRAG가 전통적 RAG를 언제 능가하는지, 그리고 그 성공의 근본 원인이 그래프 구축 품질인지 검색 방식인지 생성 단계의 맥락 구성인지를 단계별로 분해해 규명한다.

## 핵심 시사점

그래프의 이득은 균일하지 않다. 단순 사실 검색처럼 근거가 한 청크에 모여 있는 과제에서는 그래프 구축 비용이 이득을 상쇄하는 반면, 여러 개체·문서를 가로질러야 하는 추론과 전역적 요약 성격의 과제로 갈수록 구조적 이점이 뚜렷해진다. 따라서 GraphRAG는 기본값이 아니라 과제 유형에 따라 선택해야 할 옵션이며, 실무 적용에서는 도입 전에 과제 성격을 먼저 진단하는 절차가 필요하다.

## 관련 항목
- [GraphRAG-Bench](../benchmarks/graphrag-bench.md) — 이 논문이 제안한 벤치마크로, 짝을 이루는 노트.
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — 논문이 유효성을 검증 대상으로 삼는 패러다임.
- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md) — 비교 기준이 되는 표준 베이스라인.
- [Graph RAG: A Survey (Peng et al.)](graph-rag-survey.md) — 기법 지형을 정리한 서베이로, 평가 관점의 이 논문과 상호 보완적.
- [Query-Focused Summarization (QFS)](../concepts/query-focused-summarization.md) — 그래프가 이득을 보이는 맥락 요약 과제의 배경 개념.
- [Microsoft GraphRAG](../methods/microsoft-graphrag.md) — 벤치마크에서 비교되는 대표적 GraphRAG 구현.
- [LightRAG](../methods/lightrag.md) — 경량 GraphRAG 계열 비교 대상.
- [RAGSearch (Do We Still Need GraphRAG?)](../benchmarks/ragsearch.md) — 같은 질문을 에이전틱 검색 환경으로 확장한 후속 벤치마크.
- [LogicRAG](../methods/logicrag.md) — 사전 구축 그래프 없이도 되는지를 방법론 쪽에서 되묻는 대안.

## 참고문헌
- Xiang, Z., Wu, C., Zhang, Q., Chen, S., Hong, Z., Huang, X., & Su, J. (2025). *When to use Graphs in RAG: A Comprehensive Analysis for Graph Retrieval-Augmented Generation*. ICLR 2026. arXiv:2506.05690 — https://arxiv.org/abs/2506.05690
- GraphRAG-Bench 코드 및 데이터: https://github.com/GraphRAG-Bench/GraphRAG-Benchmark
