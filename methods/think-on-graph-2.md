---
type: Method
title: Think-on-Graph 2.0
description: 지식 그래프로 문서를 개체 단위로 연결하고 문서를 개체의 맥락으로 활용하여, 구조화된 지식과 비구조화된 텍스트를 긴밀히 결합한 채 반복적으로 검색하는 하이브리드 GraphRAG 추론 프레임워크다.
tags: [graphrag, retrieval, knowledge-graph, multi-hop-reasoning, hybrid-retrieval, graph-traversal]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2407.10805
authors: [Shengjie Ma, Chengjin Xu, Xuhui Jiang, Muzhi Li, Huaren Qu, Cehao Yang, Jiaxin Mao, Jian Guo]
year: 2024
venue: ICLR 2025
arxiv: "2407.10805"
---

# Think-on-Graph 2.0

Think-on-Graph 2.0(ToG-2)는 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)와 비구조화된 문서를 함께 활용하는 하이브리드 [RAG](../concepts/retrieval-augmented-generation.md) 추론 프레임워크다. Ma et al. (2024)가 제안했으며, 선행 연구인 [Think-on-Graph (ToG)](think-on-graph.md)가 그래프 위만 탐색하던 한계를 넘어, KG가 문서를 개체로 연결하고 문서가 다시 개체의 맥락을 제공하도록 둘을 긴밀히 결합한다. [LLM](../concepts/large-language-model.md)을 활용해 추가 학습 없이도 깊고 충실한(faithful) 추론을 지향한다.

## 개요

순수 텍스트 기반 RAG는 평면적 청크 검색에 머물러 개체 사이의 관계를 따라가는 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md)에 약하고, 그래프만 탐색하는 ToG는 그래프에 담기지 않은 풍부한 본문 정보를 놓친다. ToG-2는 KG를 문서 검색의 길잡이(knowledge-guided)로 삼아 두 정보원을 반복적으로 오가며, 정확한 그래프 탐색과 깊이 있는 문맥 검색을 동시에 달성하려 한다.

## 핵심 아이디어 / 동작 방식

ToG-2는 질의의 개체에서 출발해 KG 위에서 [그래프 순회 추론 (Graph Traversal Reasoning)](../techniques/graph-traversal-reasoning.md)을 수행하는 그래프 검색과, 그 개체에 연결된 문서를 가져오는 문서 검색을 번갈아 반복한다. 각 단계에서 KG는 어떤 문서를 살펴볼지 안내하고, 검색된 문서는 다음에 확장할 관계와 개체를 정하는 단서가 되어 [하이브리드 검색 (Hybrid Retrieval)](../techniques/hybrid-retrieval.md)을 이룬다. LLM은 누적된 단서가 답에 충분한지 판단하여 탐색을 더 깊게 이어갈지 멈출지를 제어한다.

## 기여

- KG와 문서를 느슨히 병치하지 않고, 개체를 매개로 양방향으로 긴밀히 결합한 하이브리드 검색 구조를 제시했다.
- 그래프 탐색과 문서 검색을 반복적으로 교차시켜 추론 깊이를 키우면서도 근거 추적이 가능한 충실한 추론을 지원한다.
- 별도 학습 없이 다양한 규모의 LLM에 적용 가능하며, 기존 LLM 추론 및 RAG 방법 대비 개선을 보고한다.

## 강점과 한계

ToG-2는 추가 학습 비용 없이 작동하고, 검색 경로가 그래프와 문서로 명시되어 해석 가능성과 충실성이 높다. 반면 반복적 검색은 LLM 호출이 누적되어 지연·비용이 늘고, 문서를 연결하는 KG 품질과 개체 연결(entity linking)의 정확도에 성능이 크게 좌우된다.

## 관련 항목

- [Think-on-Graph (ToG)](think-on-graph.md) — ToG-2가 직접 확장한 그래프 탐색 기반 선행 방법
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — 이 방법이 구현하는 더 넓은 패러다임
- [그래프 순회 추론 (Graph Traversal Reasoning)](../techniques/graph-traversal-reasoning.md) — 그래프 위 탐색의 핵심 메커니즘
- [하이브리드 검색 (Hybrid Retrieval)](../techniques/hybrid-retrieval.md) — 그래프와 문서 검색을 결합한 방식
- [Reasoning on Graphs (RoG)](reasoning-on-graphs.md) — 관계 경로를 활용하는 또 다른 KG 기반 추론 방법
- [StructGPT](structgpt.md) — 구조화된 지식을 LLM 추론에 결합한 비교 대상 방법
- [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md) — ToG-2가 겨냥하는 핵심 능력
- [WebQuestionsSP (WebQSP)](../benchmarks/webqsp.md) — 평가에 쓰인 KGQA 벤치마크

## 참고문헌

- Ma, S., Xu, C., Jiang, X., Li, M., Qu, H., Yang, C., Mao, J., & Guo, J. (2024). *Think-on-Graph 2.0: Deep and Faithful Large Language Model Reasoning with Knowledge-guided Retrieval Augmented Generation*. ICLR 2025. arXiv:2407.10805 — https://arxiv.org/abs/2407.10805
