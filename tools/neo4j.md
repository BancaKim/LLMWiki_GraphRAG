---
type: Tool
title: Neo4j
description: Cypher 질의 언어와 네이티브 벡터 인덱스를 지원하는 속성 그래프 데이터베이스로, GraphRAG의 지식 그래프 저장소로 널리 쓰인다.
tags: [neo4j, graph-database, knowledge-graph, vector-search, graphrag]
timestamp: 2026-06-29
resource: https://github.com/neo4j/neo4j
---

# Neo4j

Neo4j는 데이터를 노드와 관계(엣지)로 표현하는 속성 그래프(property graph) 데이터베이스다. 선언적 질의 언어인 Cypher로 그래프를 탐색하며, ACID 트랜잭션을 지원하는 운영용 데이터베이스다. Community Edition은 GPLv3 라이선스의 오픈소스로 제공되며, 상용 Enterprise Edition도 함께 배포된다. GraphRAG(그래프 기반 검색 증강 생성)에서는 추출된 엔티티와 관계를 저장·질의하는 백엔드로 흔히 사용된다.

## 개요

Neo4j는 그래프를 디스크에 네이티브로 저장하고 인접 노드를 포인터로 따라가는 방식으로 다단계 탐색을 효율적으로 처리한다. 최근 버전은 노드·관계 속성에 벡터 임베딩을 저장하고 근사 최근접 이웃 검색을 수행하는 네이티브 벡터 인덱스를 제공해, 같은 데이터베이스 안에서 [텍스트 임베딩](../concepts/text-embedding.md) 기반 [밀집 검색](../concepts/dense-retrieval.md)과 그래프 질의를 결합할 수 있다.

## 주요 기능

- 속성 그래프 모델과 선언적 질의 언어 Cypher
- 벡터 인덱스와 전문(full-text) 인덱스를 활용한 [하이브리드 검색](../techniques/hybrid-retrieval.md)
- 그래프 알고리즘 라이브러리(Graph Data Science), Python·Java·JavaScript 등 다수의 드라이버
- ACID 트랜잭션, 클러스터링, Aura 관리형 클라우드 서비스

## GraphRAG에서의 일반적 사용

GraphRAG 파이프라인에서 [LLM](../concepts/large-language-model.md)이 문서에서 추출한 엔티티와 관계는 Neo4j에 [지식 그래프](../concepts/knowledge-graph.md)로 적재된다. 질의 시점에는 벡터 검색으로 진입 노드를 찾은 뒤 Cypher로 인접 노드와 경로를 탐색하는 방식이 흔히 쓰이며, 이는 [멀티홉 추론](../concepts/multi-hop-reasoning.md)과 [서브그래프 추출](../techniques/subgraph-extraction.md)을 뒷받침한다. 공식 `neo4j-graphrag-python` 패키지와 [LlamaIndex PropertyGraphIndex](llamaindex-property-graph.md), [LangChain LLMGraphTransformer](langchain-graph.md) 등이 Neo4j를 저장소로 연동한다.

## 관련 항목

- [GraphRAG (패러다임)](../concepts/graph-rag.md) — Neo4j가 저장소 역할을 하는 검색 증강 패러다임
- [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md) — Neo4j가 저장·질의하는 데이터 구조
- [지식 그래프 구축 (Knowledge Graph Construction)](../techniques/knowledge-graph-construction.md) — 적재되는 그래프를 만드는 과정
- [하이브리드 검색 (Hybrid Retrieval)](../techniques/hybrid-retrieval.md) — 벡터+그래프 질의를 결합하는 방식
- [밀집 검색 / 벡터 검색 (Dense Retrieval)](../concepts/dense-retrieval.md) — Neo4j 벡터 인덱스가 지원하는 검색 방식
- [LlamaIndex PropertyGraphIndex](llamaindex-property-graph.md) — Neo4j를 백엔드로 쓸 수 있는 그래프 인덱스 도구
- [LangChain LLMGraphTransformer](langchain-graph.md) — 추출 결과를 Neo4j에 적재하는 도구
- [Microsoft GraphRAG](../methods/microsoft-graphrag.md) — Neo4j 등 그래프 저장소와 연동되는 대표 GraphRAG 방법

## 참고문헌

- Neo4j, Inc. *Neo4j: Graphs for Everyone (source code)*. GitHub. — https://github.com/neo4j/neo4j
- Neo4j Documentation. *Vector indexes — Cypher Manual*. — https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/vector-indexes/
- Neo4j Documentation. *neo4j-graphrag-python — User Guide: RAG*. — https://neo4j.com/docs/neo4j-graphrag-python/current/user_guide_rag.html
