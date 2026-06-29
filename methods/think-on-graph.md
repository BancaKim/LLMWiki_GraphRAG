---
type: Method
title: Think-on-Graph (ToG)
description: LLM을 에이전트로 삼아 지식 그래프 위에서 빔 서치로 추론 경로를 반복 탐색하고, 검색한 지식에 근거해 답을 도출하는 학습이 필요 없는 LLM-KG 통합 추론 기법이다.
tags: [graphrag, retrieval, knowledge-graph, multi-hop-reasoning, graph-traversal, knowledge-graph-qa]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2307.07697
authors: [Jiashuo Sun, Chengjin Xu, Lumingyuan Tang, Saizhuo Wang, Chen Lin, Yeyun Gong, Lionel M. Ni, Heung-Yeung Shum, Jian Guo]
year: 2024
venue: "ICLR 2024"
arxiv: "2307.07697"
---

# Think-on-Graph (ToG)

Think-on-Graph(ToG)는 [LLM](../concepts/large-language-model.md)을 에이전트로 삼아 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md) 위를 직접 탐색하며 추론하는 [GraphRAG](../concepts/graph-rag.md) 기법이다. LLM이 질문 개체에서 출발해 그래프의 개체와 관계를 반복적으로 따라가며 빔 서치(beam search)로 유망한 추론 경로를 찾고, 그 경로에서 모은 지식에 근거해 답을 도출한다. Sun et al.(2024)이 ICLR 2024에서 제안했다.

## 개요

LLM은 내부 지식만으로 깊은 추론을 수행할 때 [환각 (Hallucination)](../concepts/hallucination.md)에 취약하다. ToG는 외부 지식 그래프를 LLM 추론에 끌어들여 이 문제를 완화한다. 기존 방식이 그래프에서 뽑은 정보를 단순히 프롬프트에 넣는 데 그쳤다면, ToG는 LLM이 탐색의 매 단계를 스스로 판단하며 그래프 위를 능동적으로 [순회](../techniques/graph-traversal-reasoning.md)하도록 한다. 별도 학습 없이 다양한 LLM과 KG에 끼워 쓸 수 있는 점이 특징이다.

## 핵심 아이디어 / 동작 방식

ToG는 질문에서 개체를 추출해 탐색 시작점으로 삼은 뒤, 반복적으로 빔 서치를 수행한다. 각 단계에서 현재 경로의 끝 개체에 연결된 후보 관계와 이웃 개체를 탐색(exploration)하고, LLM이 질문과의 관련성을 평가해 폭(beam width) 만큼의 유망한 경로만 남긴다. 이어서 LLM이 모인 경로가 답하기에 충분한지 추론(reasoning)으로 판정하며, 부족하면 탐색을 한 홉(hop) 더 확장하고 충분하면 그 경로를 근거로 답을 [생성 (RAG)](../concepts/retrieval-augmented-generation.md)한다. 논문은 개체 중심의 ToG와 함께 관계 정보를 함께 활용하는 ToG-R 변형도 제시한다.

## 기여

- LLM을 그래프 위의 탐색 에이전트로 두어 검색과 추론을 긴밀히 결합한 LLM-KG 통합 추론 패러다임 제안.
- 그래프 위 빔 서치로 추론 경로를 반복 탐색하는 학습 불필요(plug-and-play) 프레임워크.
- 탐색한 경로를 통해 답의 근거를 추적(traceability)하고 잘못된 지식을 교정(correctability)할 수 있는 책임 있는 추론 지원.
- [WebQSP](../benchmarks/webqsp.md), [ComplexWebQuestions (CWQ)](../benchmarks/complexwebquestions.md) 등 [KGQA](../concepts/knowledge-graph-question-answering.md) 벤치마크에서, 작은 모델로도 일부 설정에서 GPT-4를 능가하는 성능 입증.

## 강점과 한계

ToG는 추가 학습 없이 여러 LLM·KG·프롬프트 전략에 적용되며, 탐색 경로가 그대로 근거가 되어 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md)의 해석 가능성과 교정 가능성을 높인다. 다만 매 탐색 단계마다 LLM을 여러 번 호출하므로 비용과 지연이 크고, 성능이 지식 그래프의 완전성과 정확성에 의존한다. 또한 잘 구조화된 KG를 전제하므로 비정형 텍스트 코퍼스에 곧바로 적용하기는 어렵다.

## 관련 항목
- [Think-on-Graph 2.0](think-on-graph-2.md) — ToG를 텍스트 코퍼스와 결합해 확장한 후속 기법
- [Reasoning on Graphs (RoG)](reasoning-on-graphs.md) — 그래프 경로를 LLM 추론에 활용하는 비교 대상 기법
- [StructGPT](structgpt.md) — LLM이 구조화 데이터를 반복 호출하며 추론하는 유사 접근
- [GNN-RAG](gnn-rag.md) — GNN을 검색기로 쓰는 또 다른 KGQA용 graph-RAG 기법
- [그래프 순회 추론 (Graph Traversal Reasoning)](../techniques/graph-traversal-reasoning.md) — ToG 동작의 핵심을 이루는 기법
- [KGQA (Knowledge Graph QA)](../concepts/knowledge-graph-question-answering.md) — ToG가 다루는 과제 설정
- [환각 (Hallucination)](../concepts/hallucination.md) — ToG가 외부 KG로 완화하려는 문제
- [WebQSP](../benchmarks/webqsp.md) — ToG 평가에 쓰인 대표 KGQA 벤치마크

## 참고문헌
- Sun, J., Xu, C., Tang, L., Wang, S., Lin, C., Gong, Y., Ni, L. M., Shum, H.-Y., & Guo, J. (2024). *Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph*. ICLR 2024. arXiv:2307.07697 — https://arxiv.org/abs/2307.07697
