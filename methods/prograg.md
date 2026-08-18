---
type: Method
title: ProgRAG
description: 복잡한 질문을 하위 질문으로 분해하고 부분 추론 경로를 점진적으로 확장하면서 불확실성 인지 가지치기로 근거를 정제하는 환각 저항형 멀티홉 KGQA 프레임워크.
tags: [graphrag, knowledge-graph, knowledge-graph-qa, multi-hop-reasoning, hallucination]
authors: [Minbae Park, Hyemin Yang, Jeonghyun Kim, Kunsoo Park, Hyunjoon Kim]
year: 2025
venue: arXiv preprint
arxiv: "2511.10240"
resource: https://arxiv.org/abs/2511.10240
timestamp: 2026-08-18
---

# ProgRAG

ProgRAG는 복잡한 질문을 하위 질문으로 나누고 부분 추론 경로를 한 단계씩 넓혀 가는 멀티홉 KGQA 프레임워크다. 각 단계에서 외부 리트리버가 후보 근거를 모으고 LLM이 불확실성 인지 가지치기로 이를 정제하여, 환각과 성급한 추론을 함께 억제한다. 한양대학교와 서울대학교 연구진(Park 등, 2025)이 제안했다.

## 개요

LLM은 강한 추론 능력을 보이지만 근거 없는 사실을 지어내는 [Hallucination (환각)](../concepts/hallucination.md) 문제와 낮은 투명성이라는 약점을 함께 안고 있다. [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)를 결합해 이를 보완하려는 기존 시도는 세 지점에서 흔들린다. 첫째, 검색이 부정확하거나 추론이 중간에 실패한다. 둘째, 입력 컨텍스트가 길어지면서 정작 결정적인 근거가 주변 정보에 묻힌다. 셋째, 많은 접근이 [Large Language Model (LLM)](../concepts/large-language-model.md)에게 그래프에서 근거를 직접 가져오는 일과 그것이 충분한지 판단하는 일을 한꺼번에 맡겨, 성급하거나 잘못된 추론으로 이어진다.

## 핵심 아이디어

ProgRAG는 답을 한 번에 구하지 않고 점진적으로 쌓아 올린다. 먼저 복잡한 질문을 여러 하위 질문(sub-question)으로 분해하고, 하위 질문에 하나씩 답하면서 부분 추론 경로(partial reasoning path)를 단계적으로 확장한다. 각 단계에서는 외부 리트리버가 그래프에서 후보 근거를 모으고, LLM은 이를 불확실성 인지 가지치기(uncertainty-aware pruning)로 검증해 확신이 낮은 후보를 걷어낸다. 검색과 판단을 LLM에 통째로 맡기는 대신 역할을 나눈 설계다. 마지막으로 하위 질문 답변에서 얻은 부분 경로들을 정리하고 재배열해 LLM 추론에 쓰일 컨텍스트를 최적화함으로써, 핵심 근거가 긴 프롬프트 속에 묻히지 않도록 만든다.

## 기여

- 질문 분해와 부분 추론 경로의 점진적 확장을 결합한 [Knowledge Graph QA (KGQA)](../concepts/knowledge-graph-question-answering.md) 프레임워크를 제안했다.
- 외부 리트리버의 후보 수집과 LLM의 불확실성 인지 가지치기를 분리해 성급한 추론과 환각을 억제했다.
- 부분 경로를 정리·재배열하는 컨텍스트 최적화로 결정적 근거의 가시성을 높였다.
- 3개 데이터셋에서 정확도를 개선했고, 특히 conjunction·superlative 같은 복잡한 질의 유형에서 이득이 컸다(CR-LT에서 10.9% 향상 보고).

## 강점과 한계

강점은 단계마다 근거를 검증하며 나아가므로 [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md)의 신뢰성과 해석 가능성이 함께 높아지고, 여러 제약이 얽힌 어려운 질의에서 이득이 뚜렷하다는 점이다. 한계로는 하위 질문마다 검색과 가지치기를 반복하므로 LLM 호출 비용과 지연이 늘어나고, 질문 분해가 어긋나면 이후 단계가 연쇄적으로 흔들릴 수 있으며, 성능이 기반 지식 그래프의 완전성에 의존한다는 점을 들 수 있다.

## 관련 항목

- [Think-on-Graph (ToG)](think-on-graph.md) — LLM이 탐색과 충분성 판단을 스스로 맡는 접근으로, ProgRAG가 문제로 지목한 방식이다.
- [Reasoning on Graphs (RoG)](reasoning-on-graphs.md) — 관계 경로를 계획으로 삼아 추론하는 비교 대상 방법이다.
- [PathRAG](pathrag.md) — 경로 가지치기로 컨텍스트 잡음을 줄인다는 문제의식을 공유한다.
- [SubgraphRAG](subgraphrag.md) — 근거 후보를 정제해 LLM에 전달하는 또 다른 KGQA 기법이다.
- [Knowledge Graph QA (KGQA)](../concepts/knowledge-graph-question-answering.md) — ProgRAG가 다루는 과제 설정이다.
- [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md) — 하위 질문 분해가 겨냥하는 핵심 역량이다.
- [Hallucination (환각)](../concepts/hallucination.md) — ProgRAG가 점진적 검증으로 완화하려는 문제다.
- [GraphSearch](graphsearch.md) — 다중 턴 에이전트 검색으로 근거를 반복 수집하는 동시대 접근이다.

## 참고문헌

- Park, M., Yang, H., Kim, J., Park, K., & Kim, H. (2025). *ProgRAG: Hallucination-Resistant Progressive Retrieval and Reasoning over Knowledge Graphs*. arXiv preprint. arXiv:2511.10240 — https://arxiv.org/abs/2511.10240
