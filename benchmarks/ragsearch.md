---
type: Benchmark
title: RAGSearch (Do We Still Need GraphRAG?)
description: 에이전틱 검색 환경에서 밀집 RAG와 GraphRAG를 동일한 LLM 백본·검색 예산·추론 프로토콜로 비교해, 명시적 그래프 구조가 여전히 필요한지를 정확도·비용·안정성 측면에서 평가하는 통합 벤치마크다.
tags: [benchmark, agentic-search, graphrag, dense-retrieval, evaluation]
year: 2026
venue: arXiv preprint
arxiv: "2604.09666"
resource: https://arxiv.org/abs/2604.09666
timestamp: 2026-08-18
---

# RAGSearch (Do We Still Need GraphRAG?)

RAGSearch는 Fan et al.(2026)이 제안한 통합 벤치마크로, "에이전틱 검색(agentic search)이 명시적 그래프 구조의 부재를 보완할 수 있는가, 그렇다면 비용이 큰 GraphRAG 파이프라인이 여전히 필요한가"라는 질문에 답하고자 한다. 핵심 관점은 검색 방법을 완결된 시스템이 아니라 에이전트가 반복 호출하는 **'검색 인프라(retrieval infrastructure)'** 로 재정의하는 데 있다. 학습 없이 동작하는(training-free) 방식과 학습 기반(training-based) 에이전틱 추론을 모두 포괄하며, 정확도와 함께 비용·효율·안정성을 나란히 보고한다.

## 개요

[GraphRAG (the paradigm)](../concepts/graph-rag.md)는 문서에서 개체와 관계를 추출해 그래프 인덱스를 구축함으로써 흩어진 근거를 잇는 이점을 얻지만, 그 대가로 상당한 오프라인 전처리 비용을 치른다. 반면 에이전틱 검색은 대규모 언어 모델이 질의를 스스로 분해하고 검색을 반복하며 근거를 누적하므로, 그래프가 미리 만들어 두던 연결을 추론 시점에 동적으로 만들어낼 여지가 있다. RAGSearch는 이 대체 가능성을 정면으로 검증하기 위해, 단순 [Dense Retrieval / Vector Search](../concepts/dense-retrieval.md) 기반 [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)와 대표적 GraphRAG 방법들을 동일한 에이전틱 프레임 안에 놓고 비교한다.

## 과제 및 형식

여러 QA 벤치마크를 한데 모아 평가하되, 방법 간 비교가 왜곡되지 않도록 **LLM 백본·검색 예산·추론 프로토콜을 표준화**한다. 성능이 부풀려지기 쉬운 부분 샘플링 대신 전체 테스트셋을 기준으로 결과를 보고하는 점도 특징이다. 과제는 단일 사실 조회부터 여러 문서를 가로지르는 [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md)까지 걸쳐 있어, 그래프 구조의 이득이 질의 난이도에 따라 어떻게 달라지는지를 분리해 관찰할 수 있다.

## 평가 지표

답변 정확도에 더해 실제 배치 관점의 비용 항목을 함께 측정한다. 구체적으로 그래프 구축을 포함한 **오프라인 전처리 비용**, 에이전트의 반복 검색에서 발생하는 **온라인 추론 효율**, 그리고 동일 조건 반복 실행에서의 **안정성(stability)** 을 보고한다. 이로써 정확도 우위가 어느 정도의 인덱싱·추론 비용으로 얻어진 것인지를 함께 판단할 수 있다.

## 주요 발견

에이전틱 검색은 밀집 RAG의 성능을 크게 끌어올려 GraphRAG와의 격차를 상당 부분 좁히며, 특히 강화학습(RL) 기반 설정에서 그 효과가 두드러진다. 다만 복잡한 멀티홉 추론에서는 [Microsoft GraphRAG](../methods/microsoft-graphrag.md)를 비롯한 그래프 기반 방법이 여전히 우위를 지킨다. 또한 오프라인 구축 비용이 여러 질의에 걸쳐 상각될 경우, GraphRAG는 더 안정적인 에이전틱 검색 행동을 보인다. 결론적으로 그래프 구조는 보편적 필수 요소는 아니지만, 난도 높은 추론과 반복 사용 환경에서는 여전히 값을 한다.

## 관련 항목

- [GraphRAG-Bench](graphrag-bench.md) — 그래프 구조의 실효성을 묻는 문제의식을 공유하는 선행 벤치마크
- [GraphSearch](../methods/graphsearch.md) — 그래프 검색과 에이전틱 반복 탐색을 결합한 대표 방법
- [LightRAG](../methods/lightrag.md) — 오프라인 비용을 낮춘 경량 GraphRAG 비교 대상
- [HippoRAG](../methods/hipporag.md) — 함께 견주어지는 그래프 기반 검색 인프라
- [HotpotQA](hotpotqa.md) — 표준화된 평가에 포함되는 대표 멀티홉 QA 데이터셋
- [MuSiQue](musique.md) — 더 어려운 멀티홉 구간에서 그래프 우위를 확인하는 데 쓰이는 데이터셋
- [Large Language Model (LLM)](../concepts/large-language-model.md) — 백본을 고정해야 비교가 성립하는 통제 변수
- [When to use Graphs in RAG](../surveys/when-to-use-graphs-in-rag.md) — "그래프가 언제 이득인가"를 먼저 물은 분석 논문
- [LogicRAG](../methods/logicrag.md) — 사전 구축 그래프를 없애는 방향의 대안으로, 같은 질문에 방법론으로 답한다

## 참고문헌

- Fan, D., et al. (2026). *Do We Still Need GraphRAG? Benchmarking RAG and GraphRAG for Agentic Search Systems*. arXiv preprint. arXiv:2604.09666 — https://arxiv.org/abs/2604.09666
