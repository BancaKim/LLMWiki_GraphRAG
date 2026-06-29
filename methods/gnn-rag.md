---
type: Method
title: GNN-RAG
description: GNN(그래프 신경망)을 지식 그래프 위의 검색기로, LLM을 답변 생성기로 결합한 KGQA 기법으로, GNN이 질문 개체에서 후보 답변으로 이어지는 추론 경로를 뽑아 LLM에게 전달한다.
tags: [graphrag, retrieval, knowledge-graph, graph-neural-network, knowledge-graph-qa, multi-hop-reasoning]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2405.20139
authors: [Costas Mavromatis, George Karypis]
year: 2024
venue: "arXiv preprint (later Findings of ACL 2025)"
arxiv: "2405.20139"
---

# GNN-RAG

GNN-RAG는 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md) 위에서 [GNN (Graph Neural Network)](../techniques/graph-neural-network.md)을 검색기로 사용해 [LLM](../concepts/large-language-model.md)의 추론을 돕는 [GraphRAG](../concepts/graph-rag.md) 기법이다. GNN이 질문과 관련된 부분 그래프 위에서 답변 후보를 추론하면, 거기에 이르는 그래프 경로를 자연어로 풀어 LLM에 전달해 최종 답을 생성한다. Mavromatis and Karypis(2024)가 [KGQA (Knowledge Graph QA)](../concepts/knowledge-graph-question-answering.md)를 겨냥해 제안했다.

## 개요

LLM은 언어 이해에는 강하지만 다수의 사실 간 관계를 따라가는 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md)에는 약하고, 반대로 GNN은 그래프 구조 위에서의 다단계 추론에 강하다. GNN-RAG는 이 둘의 역할을 분리해, 무거운 그래프 추론은 GNN이 맡고 언어 표현과 답변 생성은 LLM이 맡도록 결합한다. 이로써 작은 규모로 미세조정된 LLM만으로도 더 큰 모델에 견주는 성능을 노린다.

## 핵심 아이디어 / 동작 방식

먼저 질문 개체 주변의 부분 그래프를 [부분 그래프 추출 (Subgraph Extraction)](../techniques/subgraph-extraction.md)로 가져온다. GNN은 이 조밀한 부분 그래프 위에서 각 노드가 답변일 확률을 추론하고, 높은 점수를 받은 후보 노드를 선별한다. 그런 다음 질문 개체에서 해당 후보까지의 최단 경로를 추출해 자연어 문장으로 변환하고, 이를 검색 근거로 LLM 프롬프트에 넣어 답을 [생성 (RAG)](../concepts/retrieval-augmented-generation.md)한다. 저자들은 GNN 기반 검색과 LLM 기반 검색을 결합(RA, retrieval augmentation)해 답변 후보의 재현율을 더 높이는 방식도 제시한다.

## 기여

- GNN을 조밀한 부분 그래프 추론기로, LLM을 언어 처리기로 역할 분담한 KGQA용 검색 증강 프레임워크.
- GNN 검색 경로를 자연어로 변환해 LLM에 주입하는 검색 인터페이스 설계.
- [WebQSP](../benchmarks/webqsp.md)와 [ComplexWebQuestions (CWQ)](../benchmarks/complexwebquestions.md)에서 당시 최고 수준의 성능 달성, 작은 미세조정 LLM으로 GPT-4에 필적하거나 능가.

## 강점과 한계

GNN-RAG는 멀티홉·다개체 질문에서 LLM 단독 검색보다 강하고, 그래프 추론을 GNN에 위임해 효율적이다. 다만 성능이 학습된 GNN과 부분 그래프 품질에 의존하며, 잘 구조화된 지식 그래프와 학습 데이터가 필요해 비정형 텍스트 코퍼스에 곧바로 적용하기는 어렵다. 또한 GNN 학습이라는 추가 구성 요소가 파이프라인을 복잡하게 만든다.

## 관련 항목
- [GNN (Graph Neural Network)](../techniques/graph-neural-network.md) — GNN-RAG의 검색기 역할을 하는 핵심 기법
- [G-Retriever](g-retriever.md) — GNN과 LLM을 결합하는 또 다른 graph-RAG 기법
- [SubgraphRAG](subgraphrag.md) — 부분 그래프 검색을 활용하는 KGQA 기법
- [Reasoning on Graphs (RoG)](reasoning-on-graphs.md) — 그래프 경로를 LLM 추론에 쓰는 비교 대상 기법
- [Think-on-Graph (ToG)](think-on-graph.md) — 지식 그래프 탐색으로 LLM 추론을 돕는 대안 접근
- [KGQA (Knowledge Graph QA)](../concepts/knowledge-graph-question-answering.md) — GNN-RAG가 다루는 과제 설정
- [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md) — GNN-RAG가 주로 겨냥하는 역량
- [WebQSP](../benchmarks/webqsp.md) — GNN-RAG 평가에 쓰인 KGQA 벤치마크

## 참고문헌
- Mavromatis, C., & Karypis, G. (2024). *GNN-RAG: Graph Neural Retrieval for Large Language Model Reasoning*. arXiv preprint (later Findings of ACL 2025). arXiv:2405.20139 — https://arxiv.org/abs/2405.20139
