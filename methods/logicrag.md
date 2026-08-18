---
type: Method
title: LogicRAG
description: 색인 단계에서 그래프를 미리 구축하지 않고 질의 시점에 하위 문제 간 논리 의존 구조를 동적으로 생성해 그 순서대로 검색과 추론을 수행하는 그래프 기반 RAG의 대안 프레임워크.
tags: [graphrag, retrieval, multi-hop-reasoning, graph-free, query-time-reasoning]
authors: [Shengyuan Chen, Chuang Zhou, Zheng Yuan, Qinggang Zhang, Zeyang Cui, Hao Chen, Yilin Xiao, Jiannong Cao, Xiao Huang]
year: 2025
venue: AAAI 2026
arxiv: "2508.06105"
resource: https://arxiv.org/abs/2508.06105
timestamp: 2026-08-18
---

# LogicRAG

LogicRAG는 "RAG에 미리 만들어 둔 그래프가 필요하지 않다"는 주장을 앞세운 [GraphRAG (the paradigm)](../concepts/graph-rag.md)의 대안적 설계다. 색인 단계에서 그래프를 구축하는 대신, 질의가 들어온 시점에 그 질문에 맞는 추론 구조를 동적으로 만들어 검색을 이끈다. 홍콩폴리텍대(PolyU) 연구진이 제안했으며 AAAI 2026에 게재되었다. 코드는 chensyCN/LogicRAG 저장소로 공개되어 있다.

## 개요

대부분의 그래프 기반 [RAG](../concepts/retrieval-augmented-generation.md)는 [Knowledge Graph Construction](../techniques/knowledge-graph-construction.md)을 오프라인 색인 단계에 배치한다. 이 선택에는 세 가지 부담이 따른다. 첫째, 문서 전체를 훑으며 [Large Language Model (LLM)](../concepts/large-language-model.md)을 호출해야 하므로 색인 비용이 크다. 둘째, 코퍼스가 갱신되면 그래프를 다시 만들어야 한다. 셋째, 미리 고정한 그래프 구조가 실제로 들어오는 질의의 추론 요구와 어긋날 수 있다. LogicRAG는 이 부담들이 모두 '사전 구축'이라는 전제에서 비롯된다고 보고, 그 전제를 덜어 내는 쪽을 택한다.

## 핵심 아이디어

LogicRAG는 질의 시점에 적응적 추론 구조(adaptive reasoning structure)를 생성한다. 먼저 입력 질문을 여러 하위 문제로 분해하고, 하위 문제 사이의 논리적 의존 관계를 방향 비순환 그래프(DAG)로 표현한다. 이어 위상 정렬(topological sort)로 이 그래프를 선형화해, 앞선 답이 뒤따르는 질문의 전제가 되도록 일관된 처리 순서를 만든다. 그 순서를 따라가며 각 하위 문제에 필요한 근거만 차례로 검색하고 추론을 이어 붙인다. 여기에 그래프 가지치기와 문맥 가지치기를 적용해 중복 검색과 불필요한 문맥을 줄이고 전체 토큰 비용을 낮춘다.

## 기여

- 사전 구축 그래프 없이도 그래프 기반 RAG의 이점을 얻을 수 있다는 문제 제기를 정면으로 제시했다.
- 질의별 논리 의존 DAG와 위상 정렬 기반 선형화로 [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md)의 처리 순서를 명시적으로 다루는 절차를 설계했다.
- 그래프 가지치기와 문맥 가지치기를 결합해 중복 검색과 토큰 비용을 함께 줄이는 방식을 제안했다.

## 강점과 한계

강점은 오프라인 색인 비용이 사라진다는 데 있다. 코퍼스가 바뀌어도 그래프를 재구축할 필요가 없고, 추론 구조가 질의마다 새로 만들어지므로 구조와 질문 사이의 불일치도 줄어든다. 하위 문제 순서가 겉으로 드러나 추론 경로를 해석하기도 비교적 쉽다. 한계로는 비용이 색인에서 질의 시점으로 옮겨가 질의당 LLM 호출과 응답 지연이 늘 수 있고, 최종 품질이 질문 분해와 의존 관계 판단의 정확도에 크게 좌우된다는 점이 있다. 또한 코퍼스 전역을 조망해야 하는 요약형 질의처럼 사전 그래프가 주는 전역 구조가 유리한 상황은 여전히 남는다.

## 관련 항목

- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — LogicRAG가 사전 구축 전제를 되묻는 상위 패러다임이다.
- [Microsoft GraphRAG](microsoft-graphrag.md) — 사전 구축 그래프 방식의 대표 사례로, LogicRAG의 직접적 비교 대상이다.
- [Knowledge Graph Construction](../techniques/knowledge-graph-construction.md) — LogicRAG가 색인 단계에서 생략하는 절차다.
- [LazyGraphRAG](lazygraphrag.md) — 비용을 질의 시점으로 미룬다는 문제의식을 공유하는 기법이다.
- [LinearRAG](linearrag.md) — 그래프는 유지하되 구축 비용을 낮추는 다른 노선의 대안이다.
- [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md) — 적응적 추론 구조가 겨냥하는 과제 유형이다.
- [MuSiQue](../benchmarks/musique.md) — 하위 문제 분해와 순차 추론이 요구되는 멀티홉 QA 평가 환경이다.
- [When to use Graphs in RAG](../surveys/when-to-use-graphs-in-rag.md) — 그래프 구조가 실제로 이득인 조건을 따진 분석으로, LogicRAG의 문제의식과 맞닿는다.
- [RAGSearch (Do We Still Need GraphRAG?)](../benchmarks/ragsearch.md) — 그래프 없는 대안이 어디까지 따라잡는지 측정한 벤치마크다.

## 참고문헌

- Chen, S., Zhou, C., Yuan, Z., Zhang, Q., Cui, Z., Chen, H., Xiao, Y., Cao, J., & Huang, X. (2025). *You Don't Need Pre-built Graphs for RAG: Retrieval Augmented Generation with Adaptive Reasoning Structures*. AAAI 2026. Proceedings of the AAAI Conference on Artificial Intelligence, 40(36), 30270–30278. arXiv:2508.06105 — https://arxiv.org/abs/2508.06105
- 코드: https://github.com/chensyCN/LogicRAG
