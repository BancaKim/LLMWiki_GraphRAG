---
type: Method
title: GraphSearch
description: GraphSearch는 검색 과정을 6개 모듈로 나눈 에이전틱 심층 검색 워크플로로, 텍스트 청크에는 의미 질의를 구조적 그래프에는 관계 질의를 던지는 이중 채널 전략으로 GraphRAG의 얕은 검색 문제를 완화한다.
tags: [graphrag, agentic-retrieval, multi-hop-reasoning, hybrid-retrieval, iterative-reasoning]
authors: [Cehao Yang, Xiaojun Wu, Xueyuan Lin, Chengjin Xu, Xuhui Jiang, Yuanliang Sun, Jia Li, Hui Xiong, Jian Guo]
year: 2025
venue: arXiv preprint
arxiv: "2509.22009"
resource: https://arxiv.org/abs/2509.22009
timestamp: 2026-08-18
---

# GraphSearch

GraphSearch는 [GraphRAG (the paradigm)](../concepts/graph-rag.md)의 검색 단계를 다중 턴 에이전트 워크플로로 재구성한 방법이다. 기존 GraphRAG 시스템이 한 번의 얕은 검색으로 답변에 필요한 근거를 모두 확보하지 못하고, 애써 구축해 둔 구조적 그래프 데이터를 충분히 활용하지 못한다는 두 가지 한계에서 출발한다. 저자들은 검색을 여섯 개 모듈로 분해해 반복적 추론을 가능하게 하고, 텍스트와 그래프 두 양식을 각기 다른 질의로 조회하는 이중 채널 전략을 제안한다.

## 개요

단일 라운드 검색은 [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md)처럼 여러 근거를 이어 붙여야 하는 질의에서 특히 취약하다. 필요한 사실 중 일부만 회수되면 이후 생성 단계가 결손을 메우려 하면서 [Hallucination (환각)](../concepts/hallucination.md) 위험이 커진다. GraphSearch는 이 문제를 검색기 자체의 성능이 아니라 검색 절차의 구조 문제로 보고, 질의 분해·검색·근거 충분성 판단·질의 재작성을 오가는 모듈형 루프로 대응한다.

## 핵심 아이디어

핵심은 이중 채널(dual-channel) 검색이다. 청크 단위로 나뉜 원문 텍스트에는 의미 기반 질의를, 사전 구축된 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)에는 관계 기반 질의를 각각 던져 두 양식의 상보적 강점을 함께 활용한다. 여섯 개 모듈은 한 번의 검색으로 끝내지 않고, 확보한 근거가 불충분하다고 판단되면 후속 질의를 생성해 다음 턴으로 넘기는 심층 검색 루프를 이룬다.

## 기여

- 검색을 6개 모듈로 조직해 다중 턴 상호작용과 반복적 추론을 지원하는 에이전틱 심층 검색 워크플로를 제시했다.
- 텍스트 청크와 구조적 그래프를 서로 다른 유형의 질의로 조회하는 이중 채널 검색 전략을 설계했다.
- 6개 멀티홉 RAG 벤치마크에서 기존 단순 검색 전략 대비 답변 정확도와 생성 품질이 일관되게 향상됨을 보고했다.

## 강점과 한계

강점은 기존 GraphRAG 파이프라인의 그래프 자산을 버리지 않고 검색 계층만 교체해 얹을 수 있다는 점, 그리고 반복 루프가 얕은 검색으로 놓치던 근거를 회수한다는 점이다. 한계로는 다중 턴 구성상 질의당 LLM 호출과 지연이 늘어난다는 비용 문제, 여섯 모듈의 조합에 따르는 구현·튜닝 부담, 그리고 성능이 사전 구축된 그래프의 품질에 여전히 의존한다는 점이 있다.

## 관련 항목

- [Think-on-Graph 2.0](think-on-graph-2.md) — 텍스트와 그래프를 함께 오가는 반복적 에이전트 검색이라는 문제의식을 공유한다
- [GraphReader](graphreader.md) — 에이전트가 그래프를 탐색하며 근거를 모으는 선행 접근
- [Microsoft GraphRAG](microsoft-graphrag.md) — GraphSearch가 검색 계층을 덧씌우는 대상이 되는 대표적 그래프 색인 방법
- [LightRAG](lightrag.md) — 텍스트와 그래프를 결합하는 경량 검색 설계의 비교 대상
- [Hybrid Retrieval](../techniques/hybrid-retrieval.md) — 이중 채널 전략이 속하는 상위 기법 범주
- [Text Chunking (청킹)](../concepts/text-chunking.md) — 의미 채널이 조회하는 텍스트 단위를 규정한다
- [GraphRAG-Bench](../benchmarks/graphrag-bench.md) — 멀티홉 설정에서 이런 워크플로의 이득을 재는 평가 기반
- [RAGSearch (Do We Still Need GraphRAG?)](../benchmarks/ragsearch.md) — 에이전틱 검색이 그래프 구조를 대체할 수 있는지 정면으로 평가한 벤치마크
- [ProgRAG](prograg.md) — 질의를 분해해 근거를 점진적으로 모으는 또 다른 반복적 추론 설계

## 참고문헌

- Yang, C., Wu, X., Lin, X., Xu, C., Jiang, X., Sun, Y., Li, J., Xiong, H., & Guo, J. (2025). *GraphSearch: An Agentic Deep Searching Workflow for Graph Retrieval-Augmented Generation*. arXiv preprint. arXiv:2509.22009 — https://arxiv.org/abs/2509.22009
- 코드: https://github.com/DataArcTech/GraphSearch
