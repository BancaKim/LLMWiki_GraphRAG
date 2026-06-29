---
type: Technique
title: Entity & Relationship Extraction
description: 텍스트 청크에서 LLM 프롬프트로 유형이 부여된 개체와 그 사이의 관계(및 주장)를 추출하여 지식 그래프의 트리플을 만드는 기법이며, 회수율을 높이기 위해 글리닝/다중 라운드 추출을 사용한다.
tags: [entity-extraction, relation-extraction, knowledge-graph, graphrag, information-extraction]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2404.16130
---

# Entity & Relationship Extraction

개체·관계 추출(Entity & Relationship Extraction)은 비정형 텍스트 [청크 (Text Chunking)](../concepts/text-chunking.md)에서 유형이 부여된 개체(예: 인물, 조직, 개념)와 그 개체들을 잇는 관계를 식별해 내는 [정보 추출](knowledge-graph-construction.md)의 핵심 단계이다. 결과물은 보통 (주어, 술어, 목적어) 형태의 트리플과 부가 설명으로 정리되어, [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)의 노드와 엣지를 구성한다. GraphRAG 계열에서는 별도의 학습된 추출기 대신 [LLM (Large Language Model)](../concepts/large-language-model.md) 프롬프트로 이 작업을 수행하는 방식이 표준이 되었다.

## 개념

전통적인 개체명 인식(NER)·관계 추출은 도메인별로 라벨링된 데이터로 학습한 전용 모델에 의존했다. LLM 기반 접근은 추출할 개체 유형 목록과 출력 형식을 프롬프트로 지시하여, 별도 학습 없이도 다양한 도메인에 적용할 수 있게 한다. 각 개체에는 유형과 짧은 설명이, 각 관계에는 출발·도착 개체와 관계 설명(및 가중치)이 함께 부여되며, 사실 주장(claim)을 별도로 추출하기도 한다.

## 동작 방식

각 텍스트 청크를 LLM에 입력해 개체와 관계를 구조화된 형태로 출력하게 한다. 단일 패스로는 일부 개체가 누락되기 쉽기 때문에, [Microsoft GraphRAG](../methods/microsoft-graphrag.md)는 *글리닝(gleaning)* 이라 부르는 다중 라운드 추출을 사용한다. 즉 1차 추출 후 "놓친 개체가 있는가?"를 LLM에 되묻고, 있다면 추가 라운드를 반복하여 회수율(recall)을 높인다. 여러 청크에 같은 이름으로 나타난 개체는 동일 노드로 병합·집계되어 그래프가 완성된다.

## GraphRAG에서의 활용

이 단계는 [지식 그래프 구축 (Knowledge Graph Construction)](knowledge-graph-construction.md) 파이프라인의 출발점으로, [Microsoft GraphRAG](../methods/microsoft-graphrag.md), [LightRAG](../methods/lightrag.md), [HippoRAG](../methods/hipporag.md) 등이 색인 단계에서 이를 수행한다. 추출 품질은 이후 [커뮤니티 탐지 (Community Detection)](community-detection.md)와 검색 전반에 영향을 미친다. LLM 호출이 청크 수에 비례해 발생하므로 토큰·연산 비용이 크다는 점이 한계이며, [LazyGraphRAG](../methods/lazygraphrag.md)는 이 비용을 줄이려는 시도이다.

## 관련 항목
- [Knowledge Graph Construction](knowledge-graph-construction.md) — 개체·관계 추출을 포함하는 상위 그래프 구축 과정.
- [Knowledge Graph](../concepts/knowledge-graph.md) — 추출 결과인 트리플이 채우는 대상 구조.
- [Text Chunking (청킹)](../concepts/text-chunking.md) — 추출의 입력 단위가 되는 텍스트 분할.
- [Microsoft GraphRAG](../methods/microsoft-graphrag.md) — 글리닝 기반 다중 라운드 추출을 사용하는 대표 기법.
- [LightRAG](../methods/lightrag.md) — 경량 그래프 색인에서 LLM 추출을 활용하는 방법.
- [Community Detection (Leiden)](community-detection.md) — 추출된 개체 그래프를 클러스터링하는 후속 단계.
- [LangChain LLMGraphTransformer](../tools/langchain-graph.md) — LLM으로 텍스트에서 그래프를 추출하는 도구.
- [LlamaIndex PropertyGraphIndex](../tools/llamaindex-property-graph.md) — 추출과 그래프 색인을 함께 제공하는 도구.
