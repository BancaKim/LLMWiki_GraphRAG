---
type: Method
title: EA-GraphRAG
description: 질의의 구문적 복잡도를 점수화해 단순한 질의는 밀집 RAG로, 복잡한 질의는 그래프 검색으로 보내고 경계 사례는 융합하는 적응적 라우팅 프레임워크다.
tags: [graphrag, retrieval, adaptive-routing, efficiency, hybrid-retrieval]
authors: [Su Dong, Qinggang Zhang, Yilin Xiao, Shengyuan Chen, Chuang Zhou, Xiao Huang]
year: 2026
venue: arXiv preprint
arxiv: "2602.03578"
resource: https://arxiv.org/abs/2602.03578
timestamp: 2026-08-18
---

# EA-GraphRAG

EA-GraphRAG는 "**필요할 때만 그래프를 쓰자(Use Graph When It Needs)**"는 문제의식에서 출발한 적응적 프레임워크다. [GraphRAG (the paradigm)](../concepts/graph-rag.md)는 복잡한 질의에서 이득을 보이지만 실제 환경에서는 오히려 표준 [RAG](../concepts/retrieval-augmented-generation.md)보다 정확도가 떨어지고 지연이 커지는 역설이 보고되어 왔다. 이 논문은 그 원인을 **질의 복잡도와 무관하게 모든 질의에 GraphRAG를 일률 적용한 것**으로 지목하고, 질의별로 검색 경로를 갈라 준다.

## 개요

같은 코퍼스라도 "X의 설립 연도는?" 같은 단일 홉 질의와 여러 문서를 이어야 하는 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md) 질의는 요구하는 검색의 성격이 다르다. 전자에 그래프 순회를 동원하면 비용만 늘고 잡음이 섞이기 쉽다. EA-GraphRAG는 이 판단을 **질의를 보는 것만으로, 가볍게** 내리는 것을 목표로 한다.

## 핵심 아이디어

세 요소로 구성된다. 첫째 **구문 특징 구성기(syntactic feature constructor)** 가 각 질의를 파싱해 구조적 특징 집합을 추출한다. 둘째 **경량 복잡도 점수기(complexity scorer)** 가 그 특징들을 연속적인 복잡도 점수로 사상한다. 셋째 **점수 기반 라우팅 정책**이 점수가 낮은 질의는 [밀집 검색 (Dense Retrieval)](../concepts/dense-retrieval.md)으로, 높은 질의는 그래프 기반 검색으로 보낸다. 애매한 경계 사례에는 **복잡도 인지 상호 순위 융합(complexity-aware reciprocal rank fusion)** 을 적용해 두 결과를 섞는다. 즉 [하이브리드 검색 (Hybrid Retrieval)](../techniques/hybrid-retrieval.md)을 고정 비율이 아니라 질의별로 조절하는 셈이다.

## 기여

- GraphRAG가 표준 RAG에 뒤지는 원인을 '일률 적용'으로 진단하고, 질의 수준의 적응적 라우팅으로 대응했다.
- 무거운 LLM 판단 없이 구문 특징만으로 복잡도를 매기는 경량 점수기를 설계했다.
- 단일 홉 2종·멀티홉 2종 QA 벤치마크에서 **정확도 향상과 지연 감소를 동시에** 달성하고, 단순·복잡 질의가 섞인 혼합 시나리오에서 최고 성능을 보고했다.

## 강점과 한계

강점은 기존 GraphRAG 구현을 대체하지 않고 그 앞단에 얹을 수 있어 도입 비용이 낮고, 단순 질의의 지연을 실질적으로 줄인다는 점이다. 한계로는 복잡도 점수기가 구문 특징에 기반하므로 문장은 단순하지만 실제로는 멀티홉인 질의를 놓칠 수 있고, 라우팅 임계값과 융합 가중치가 데이터셋 특성에 민감할 수 있다는 점이다. 또한 판단 근거가 질의 표면에 한정되어, 코퍼스 쪽 사정(해당 근거가 실제로 흩어져 있는지)은 반영하지 못한다.

## 관련 항목

- [When to use Graphs in RAG](../surveys/when-to-use-graphs-in-rag.md) — "그래프가 언제 이득인가"를 분석으로 물은 논문으로, EA-GraphRAG는 그 답을 시스템으로 구현한다.
- [Is GraphRAG Needed?](../surveys/is-graphrag-needed.md) — 여러 RAG 구성을 실증 비교하며 같은 질문을 다룬다.
- [RAGSearch (Do We Still Need GraphRAG?)](../benchmarks/ragsearch.md) — 그래프 없는 대안이 어디까지 따라잡는지 측정한 벤치마크다.
- [LogicRAG](logicrag.md) — 사전 구축 그래프 자체를 없애는 더 급진적인 노선이다.
- [Hybrid Retrieval](../techniques/hybrid-retrieval.md) — 라우팅과 순위 융합이 속하는 상위 기법이다.
- [Dense Retrieval / Vector Search](../concepts/dense-retrieval.md) — 단순 질의를 처리하는 저비용 경로다.
- [LinearRAG](linearrag.md) — 같은 연구 그룹의 효율 지향 접근으로, 색인 쪽에서 비용을 낮춘다.
- [Local vs Global Search](../techniques/local-and-global-search.md) — 질의 성격에 따라 검색 방식을 나눈다는 발상의 선행 사례다.

## 참고문헌

- Dong, S., Zhang, Q., Xiao, Y., Chen, S., Zhou, C., & Huang, X. (2026). *Use Graph When It Needs: Efficiently and Adaptively Integrating Retrieval-Augmented Generation with Graphs*. arXiv preprint. arXiv:2602.03578 — https://arxiv.org/abs/2602.03578
