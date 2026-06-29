---
type: Tool
title: LlamaIndex PropertyGraphIndex
description: 비정형 문서에서 라벨드 속성 그래프를 추출하고 이를 질의해 GraphRAG를 구축하는 LlamaIndex의 모듈형 인덱스다.
tags: [llamaindex, graphrag, knowledge-graph, retrieval, property-graph]
timestamp: 2026-06-29
resource: https://github.com/run-llama/llama_index
---

# LlamaIndex PropertyGraphIndex

LlamaIndex PropertyGraphIndex는 오픈소스 LLM 데이터 프레임워크 LlamaIndex(`run-llama/llama_index`)의 핵심 패키지 `llama-index-core`에 포함된 인덱스다. 비정형 문서에서 라벨드 속성 그래프(labeled property graph, 노드와 관계에 타입·속성을 붙인 그래프)를 추출하고, 이를 다양한 방식으로 질의할 수 있게 한다. 2024년 5월 도입되었으며, MIT 라이선스로 배포된다.

## 개요

PropertyGraphIndex는 입력 문서를 청크로 나눈 뒤 일련의 추출기(kg_extractor)를 적용해 엔티티와 관계를 [지식 그래프](../concepts/knowledge-graph.md)로 만든다. 추출된 노드는 선택적으로 임베딩되어 그래프 저장소(기본값 `SimplePropertyGraphStore`)와 벡터 저장소에 적재된다. 그래프 구성과 검색을 각각 교체 가능한 컴포넌트로 분리한 모듈형 설계가 특징으로, 구성 요소를 조합해 [GraphRAG](../concepts/graph-rag.md) 파이프라인을 만들 수 있다.

## 주요 기능

- 추출기: 스키마 없이 추출하는 `SimpleLLMPathExtractor`·`ImplicitPathExtractor`(기본값)와, 엔티티·관계 타입을 미리 지정하는 `SchemaLLMPathExtractor` 등 ([엔티티·관계 추출](../techniques/entity-relationship-extraction.md))
- 검색기: 동의어 확장 기반 `LLMSynonymRetriever`, 벡터 유사도로 진입 노드를 찾고 인접 경로를 가져오는 `VectorContextRetriever`, 자연어를 Cypher로 변환하는 `TextToCypherRetriever` 등 ([하이브리드 검색](../techniques/hybrid-retrieval.md))
- [Neo4j](neo4j.md)를 비롯한 외부 속성 그래프 저장소 연동
- 여러 추출기·검색기를 조합하는 커스터마이즈 가능한 구조

## GraphRAG에서의 일반적 사용

GraphRAG에서 PropertyGraphIndex는 [LLM](../concepts/large-language-model.md)으로 문서에서 그래프를 구축하는 단계와, 질의 시점에 관련 [서브그래프](../techniques/subgraph-extraction.md)를 검색하는 단계를 함께 담당한다. `VectorContextRetriever`로 벡터 검색과 그래프 탐색을 결합하면 [멀티홉 추론](../concepts/multi-hop-reasoning.md)을 지원하는 컨텍스트를 만들 수 있고, [Microsoft GraphRAG](../methods/microsoft-graphrag.md) 스타일의 파이프라인을 LlamaIndex 위에서 재현하는 데도 쓰인다.

## 관련 항목

- [GraphRAG (패러다임)](../concepts/graph-rag.md) — PropertyGraphIndex가 구현을 돕는 검색 증강 패러다임
- [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md) — 이 인덱스가 추출·저장하는 데이터 구조
- [지식 그래프 구축 (Knowledge Graph Construction)](../techniques/knowledge-graph-construction.md) — 추출기가 수행하는 핵심 과정
- [엔티티·관계 추출 (Entity & Relationship Extraction)](../techniques/entity-relationship-extraction.md) — kg_extractor의 작동 원리
- [하이브리드 검색 (Hybrid Retrieval)](../techniques/hybrid-retrieval.md) — 벡터·그래프 검색기를 결합하는 방식
- [Neo4j](neo4j.md) — PropertyGraphIndex가 백엔드로 연동하는 그래프 저장소
- [LangChain LLMGraphTransformer](langchain-graph.md) — 같은 목적의 그래프 추출 도구
- [Microsoft GraphRAG](../methods/microsoft-graphrag.md) — 유사하게 재현 가능한 대표 GraphRAG 방법

## 참고문헌

- LlamaIndex. *Introducing the Property Graph Index: A Powerful New Way to Build Knowledge Graphs with LLMs* (2024). — https://www.llamaindex.ai/blog/introducing-the-property-graph-index-a-powerful-new-way-to-build-knowledge-graphs-with-llms
- LlamaIndex Documentation. *Using a Property Graph Index*. — https://docs.llamaindex.ai/en/stable/module_guides/indexing/lpg_index_guide/
- run-llama. *llama_index (source code)*. GitHub. — https://github.com/run-llama/llama_index
