---
type: Tool
title: LangChain LLMGraphTransformer
description: LLM의 함수 호출·구조화 출력 기능으로 문서에서 엔티티와 관계를 추출해 그래프 문서로 변환하는 LangChain 유틸리티로, 그래프 스토어와 함께 GraphRAG 파이프라인 구축에 쓰인다.
tags: [langchain, knowledge-graph, graphrag, entity-relationship-extraction, neo4j]
timestamp: 2026-06-29
resource: https://github.com/langchain-ai/langchain-experimental
---

# LangChain LLMGraphTransformer

`LLMGraphTransformer`는 LangChain의 그래프 변환 유틸리티로, 비정형 텍스트 문서를 입력받아 [LLM](../concepts/large-language-model.md)(대규모 언어 모델)으로 엔티티(노드)와 관계(엣지)를 추출하고 이를 `GraphDocument` 객체로 변환한다. `langchain_experimental.graph_transformers` 모듈에 들어 있으며, 추출된 그래프 문서는 LangChain의 그래프 스토어(예: `Neo4jGraph`)에 적재해 질의에 활용한다. 즉 텍스트에서 [지식 그래프](../concepts/knowledge-graph.md)를 만드는 [엔티티·관계 추출](../techniques/entity-relationship-extraction.md) 단계를 담당하는 도구다.

## 개요

`LLMGraphTransformer`는 두 가지 동작 모드를 지원한다. 기본값은 LLM의 함수 호출(function calling)·구조화 출력 기능(`with_structured_output`)을 쓰는 모드로, 정해진 스키마에 맞춰 노드와 관계, 속성을 추출한다. 해당 기능을 지원하지 않는 모델에서는 프롬프트 기반 모드로 동작하며, 이 경우 모델 응답을 JSON으로 파싱한다(속성 추출은 제한된다). 핵심 입력 메서드는 `convert_to_graph_documents`이며, 각 입력 문서를 노드·관계 목록을 담은 `GraphDocument`로 변환한다.

## 주요 기능

- `allowed_nodes`, `allowed_relationships`로 추출할 노드·관계 유형을 제약해 [지식 그래프 구축](../techniques/knowledge-graph-construction.md) 스키마를 통제
- `node_properties`, `relationship_properties`로 엔티티·관계 속성까지 추출
- `strict_mode`로 지정한 유형 외의 결과를 걸러내 일관성 유지
- 구조화 출력을 지원하는 다양한 채팅 LLM과 연동(`convert_to_graph_documents` 동기 메서드 및 비동기 변형 제공)

## GraphRAG에서의 일반적 사용

GraphRAG 파이프라인에서 `LLMGraphTransformer`는 색인 단계의 그래프 추출을 맡는다. 문서를 [청킹](../concepts/text-chunking.md)한 뒤 변환기로 엔티티와 관계를 뽑아 `GraphDocument`를 생성하고, `Neo4jGraph.add_graph_documents` 등으로 [Neo4j](neo4j.md) 같은 그래프 스토어에 적재한다. 질의 시점에는 벡터 검색과 그래프 탐색을 결합해 [멀티홉 추론](../concepts/multi-hop-reasoning.md)과 [서브그래프 추출](../techniques/subgraph-extraction.md)을 지원하며, 이런 구성은 [Microsoft GraphRAG](../methods/microsoft-graphrag.md)와 유사한 그래프 기반 [RAG](../concepts/retrieval-augmented-generation.md) 패턴을 LangChain 위에서 구현하는 데 쓰인다. 다만 이 모듈이 속한 `langchain-experimental` 패키지는 더 이상 유지보수되지 않으며(2026년 5월 아카이브), 기능 일부는 `langchain-neo4j` 등 통합 패키지로 이전되었다.

## 관련 항목

- [GraphRAG (패러다임)](../concepts/graph-rag.md) — 이 도구가 구축을 돕는 그래프 기반 검색 증강 패러다임
- [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md) — 변환기가 생성하는 데이터 구조
- [엔티티·관계 추출 (Entity & Relationship Extraction)](../techniques/entity-relationship-extraction.md) — 변환기가 수행하는 핵심 작업
- [지식 그래프 구축 (Knowledge Graph Construction)](../techniques/knowledge-graph-construction.md) — 추출 결과를 그래프로 만드는 상위 과정
- [Neo4j](neo4j.md) — 변환 결과를 적재하는 대표 그래프 스토어
- [LlamaIndex PropertyGraphIndex](llamaindex-property-graph.md) — 유사한 목적의 그래프 인덱스 도구
- [Microsoft GraphRAG](../methods/microsoft-graphrag.md) — 동일한 추출·적재 흐름을 쓰는 대표 GraphRAG 방법

## 참고문헌

- LangChain. *langchain-experimental (source code)*. GitHub. — https://github.com/langchain-ai/langchain-experimental/blob/main/libs/experimental/langchain_experimental/graph_transformers/llm.py
- LangChain. *LLMGraphTransformer — API Reference*. — https://python.langchain.com/api_reference/experimental/graph_transformers/langchain_experimental.graph_transformers.llm.LLMGraphTransformer.html
- LangChain Blog. *Enhancing RAG-based application accuracy by constructing and leveraging knowledge graphs*. — https://www.langchain.com/blog/enhancing-rag-based-applications-accuracy-by-constructing-and-leveraging-knowledge-graphs
