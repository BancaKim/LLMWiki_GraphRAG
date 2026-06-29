---
type: Method
title: GraphReader
description: 긴 텍스트를 key element와 atomic fact로 이루어진 그래프로 구조화한 뒤, LLM 에이전트가 이 그래프를 자율적으로 탐색하며 멀티홉 질문에 답하도록 하는 graph 기반 장문 처리 기법이다.
tags: [graphrag, long-context, agent, multi-hop-reasoning, graph-traversal]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2406.14550
authors: [Shilong Li, Yancheng He, Hangyu Guo, Xingyuan Bu, Ge Bai, Jie Liu, Jiaheng Liu, Xingwei Qu, Yangguang Li, Wanli Ouyang, Wenbo Su, Bo Zheng]
year: 2024
venue: Findings of EMNLP 2024
arxiv: "2406.14550"
---

# GraphReader

GraphReader는 긴 텍스트를 그래프로 구조화한 뒤 [LLM](../concepts/large-language-model.md) 에이전트가 그 그래프를 자율적으로 탐색해 답을 찾도록 하는 장문 처리 기법이다. 텍스트를 한 번에 모델의 컨텍스트 창에 넣는 대신, 핵심 요소(key element)와 원자적 사실(atomic fact)로 압축한 노드 그래프 위에서 단계적으로 정보를 수집한다. Li et al.(2024)이 제안했으며, 작은 컨텍스트 창만으로도 매우 긴 문서에 대한 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md)을 수행하는 것을 목표로 한다.

## 개요

LLM은 컨텍스트 창이 길어질수록 흩어진 단서를 종합하는 능력이 떨어지고, 단순히 창 크기를 키우면 비용과 잡음이 함께 늘어난다. GraphReader는 문서를 [청크 (Text Chunking)](../concepts/text-chunking.md)로 나눈 뒤 각 청크를 atomic fact와 key element로 요약해 그래프 노드를 만들고, 에이전트가 이 그래프를 거칠게(coarse) 훑은 뒤 점점 세밀하게(fine) 파고드는 방식으로 필요한 정보만 선택적으로 읽는다. 이를 통해 4k 수준의 작은 컨텍스트 창으로도 긴 문서 전반의 정보를 다룬다.

## 핵심 아이디어 / 동작 방식

색인 단계에서는 각 청크를 [LLM](../concepts/large-language-model.md)으로 처리해 가장 작은 정보 단위인 atomic fact와 그 안의 명사·동사 등 key element를 추출하고, key element를 노드로, 동일 atomic fact를 공유하는 관계를 간선으로 삼아 장거리 의존성을 담은 그래프를 구성한다. 질의가 들어오면 에이전트는 먼저 단계별 분석을 거쳐 합리적 계획(rational plan)을 세우고, 미리 정의된 함수들을 호출해 초기 노드를 고른 뒤 이웃 노드와 청크 내용을 읽으며 그래프를 [순회 추론 (Graph Traversal Reasoning)](../techniques/graph-traversal-reasoning.md)한다. 탐색 도중에는 노트북(notebook)에 근거가 되는 사실을 계속 기록하고 현재 상황을 점검하며, 충분한 정보가 모이면 답을 생성한다.

## 기여

- 긴 텍스트를 key element와 atomic fact 노드로 이루어진 그래프로 [구축 (Knowledge Graph Construction)](../techniques/knowledge-graph-construction.md)하는 방식 제안.
- rational plan과 notebook을 갖춘 에이전트가 그래프를 coarse-to-fine으로 자율 탐색하는 절차 설계.
- 작은 4k 컨텍스트 창의 GraphReader가 16k~256k 길이 구간에서 GPT-4-128k를 큰 폭으로 능가함을 보고.

## 강점과 한계

GraphReader는 문서 전체를 한꺼번에 입력하지 않고 그래프를 선택적으로 탐색하므로, 작은 컨텍스트 창으로도 매우 긴 문서와 멀티홉 질문을 다룰 수 있고 에이전트의 추론 경로가 비교적 해석 가능하다. 반면 색인 단계에서 청크마다 atomic fact·key element 추출을 위한 LLM 호출이 필요해 전처리 비용이 들고, 추출 품질이 그래프와 검색 정확도에 직접 영향을 준다. 또한 다단계 에이전트 탐색은 여러 차례의 LLM 호출을 수반해 지연이 커질 수 있으며, 개체·관계로 정의된 명시적 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)라기보다 사실 공유에 기반한 그래프라는 점에서 정형 관계 추적과는 성격이 다르다.

## 관련 항목
- [GraphRAG (패러다임)](../concepts/graph-rag.md) — GraphReader가 속하는 graph 기반 검색·추론 패러다임
- [순회 추론 (Graph Traversal Reasoning)](../techniques/graph-traversal-reasoning.md) — 에이전트가 그래프를 탐색하는 핵심 동작
- [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md) — GraphReader가 겨냥하는 질의 유형
- [RAPTOR](raptor.md) — 같은 장문 처리 문제를 트리 요약 구조로 푸는 비교 대상 기법
- [Think-on-Graph (ToG)](think-on-graph.md) — LLM 에이전트가 그래프를 단계적으로 탐색한다는 점에서 유사한 접근
- [지식 그래프 구축 (Knowledge Graph Construction)](../techniques/knowledge-graph-construction.md) — atomic fact·key element로 노드 그래프를 만드는 전처리
- [HotpotQA](../benchmarks/hotpotqa.md) — GraphReader 평가에 쓰인 멀티홉 QA 벤치마크
- [MuSiQue](../benchmarks/musique.md) — 평가에 사용된 멀티홉 QA 벤치마크
- [2WikiMultiHopQA](../benchmarks/2wikimultihopqa.md) — 평가에 사용된 멀티홉 QA 벤치마크

## 참고문헌
- Li, S., He, Y., Guo, H., Bu, X., Bai, G., Liu, J., Liu, J., Qu, X., Li, Y., Ouyang, W., Su, W., & Zheng, B. (2024). *GraphReader: Building Graph-based Agent to Enhance Long-Context Abilities of Large Language Models*. Findings of EMNLP 2024. arXiv:2406.14550 — https://arxiv.org/abs/2406.14550
