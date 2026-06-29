---
type: Survey
title: RAG with Graphs (Han et al.)
description: Haoyu Han 등이 발표한 GraphRAG(그래프 기반 검색 증강 생성) 서베이로, 그래프를 query processor·retriever·organizer·generator·data source로 이루어진 통합 프레임워크로 정형화하고 도메인별 그래프 유형에 따른 기법을 폭넓게 정리한다.
tags: [graphrag, retrieval, knowledge-graph, survey, taxonomy]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2501.00309
authors: [Haoyu Han, Yu Wang, Harry Shomer, Kai Guo, Jiayuan Ding, Yongjia Lei, Mahantesh Halappanavar, Ryan A. Rossi, Subhabrata Mukherjee, Xianfeng Tang, Qi He, Zhigang Hua, Bo Long, Tong Zhao, Neil Shah, Amin Javari, Yinglong Xia, Jiliang Tang]
year: 2025
venue: arXiv preprint
arxiv: "2501.00309"
---

# RAG with Graphs (Han et al.)

"Retrieval-Augmented Generation with Graphs (GraphRAG)"는 Haoyu Han 등이 발표한 종합 서베이로, 노드와 엣지로 이질적·관계적 정보를 담는 그래프를 [RAG (Retrieval-Augmented Generation)](../concepts/retrieval-augmented-generation.md)의 외부 지식원으로 활용하는 [GraphRAG (the paradigm)](../concepts/graph-rag.md) 연구 전반을 정리한다. 검색기·생성기·데이터원을 단일 신경 임베딩 공간에서 통일적으로 설계할 수 있는 일반 RAG와 달리, 그래프 데이터는 형식이 다양하고 도메인마다 관계 패턴이 달라 별도의 설계가 필요하다는 점을 핵심 문제의식으로 삼는다.

## 범위

검색 대상이 평면 텍스트가 아니라 그래프 구조인 RAG 연구를 폭넓게 다룬다. [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)뿐 아니라 문서 그래프, 과학·사회·계획·표 형태 등 여러 도메인의 그래프를 포괄하며, 각 도메인의 관계 특성에 맞춘 GraphRAG 기법을 함께 검토한다. 일반 RAG의 [Dense Retrieval / Vector Search](../concepts/dense-retrieval.md)가 놓치는 관계 정보를 그래프로 보완하는 흐름을 [Large Language Model (LLM)](../concepts/large-language-model.md) 시대 관점에서 조망한다.

## 다루는 내용(분류 체계)

저자들은 GraphRAG를 query processor, retriever, organizer, generator, data source의 다섯 구성 요소로 이루어진 통합(holistic) 프레임워크로 정형화한다. query processor가 질의를 그래프에 맞게 변환하고, retriever가 노드·트리플·경로·[부분그래프 추출 (Subgraph Extraction)](../techniques/subgraph-extraction.md) 등 관련 그래프 요소를 뽑으며, organizer가 검색 결과를 생성에 적합한 형태로 재구성하고, generator가 최종 응답을 만든다. 이 틀 위에서 [지식 그래프 구축 (Knowledge Graph Construction)](../techniques/knowledge-graph-construction.md), [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md), 그리고 도메인별로 특화된 설계를 분류해 정리한다.

## 핵심 시사점

그래프를 검색 단위로 끌어들이면 다중 문서·다중 개체에 걸친 관계를 명시적으로 활용해 멀티홉·전역 질의에서 [환각 (Hallucination)](../concepts/hallucination.md)을 줄이는 데 유리하다. 다만 도메인마다 그래프 유형과 관계 패턴이 달라 단일 설계로 일반화하기 어렵고, 그래프 구축 비용과 평가 표준의 부재가 공통 과제로 남는다는 점을 강조한다.

## 관련 항목
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — 이 서베이가 통합 프레임워크로 정형화하는 핵심 패러다임.
- [Graph RAG: A Survey (Peng et al.)](graph-rag-survey.md) — 같은 주제를 3단계 워크플로로 다루는 인접 서베이.
- [RAG for LLMs: A Survey (Gao et al.)](rag-survey.md) — 그래프 이전의 일반 RAG 지형을 정리한 상위 서베이.
- [Unifying LLMs and KGs: A Roadmap](llm-kg-roadmap.md) — LLM과 KG 통합을 다루는 인접 서베이.
- [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md) — 서베이가 다루는 대표적 데이터원.
- [Microsoft GraphRAG](../methods/microsoft-graphrag.md) — 서베이가 분류 대상으로 삼는 전역 검색형 대표 기법.
- [HippoRAG](../methods/hipporag.md) — 그래프 기반 검색을 구현한 대표 방법 사례.
- [Multi-hop Reasoning (멀티홉 추론)](../concepts/multi-hop-reasoning.md) — 그래프 검색이 강점을 보이는 핵심 과제.

## 참고문헌
- Han, H., Wang, Y., Shomer, H., Guo, K., Ding, J., Lei, Y., Halappanavar, M., Rossi, R. A., Mukherjee, S., Tang, X., He, Q., Hua, Z., Long, B., Zhao, T., Shah, N., Javari, A., Xia, Y., & Tang, J. (2025). *Retrieval-Augmented Generation with Graphs (GraphRAG)*. arXiv preprint. arXiv:2501.00309 — https://arxiv.org/abs/2501.00309
