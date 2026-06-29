---
type: Survey
title: "Graph RAG: A Survey (Peng et al.)"
description: GraphRAG(그래프 기반 검색 증강 생성) 연구를 graph-based indexing, graph-guided retrieval, graph-enhanced generation의 3단계 워크플로로 체계화하고 관련 기법·과제·벤치마크를 정리한 서베이 논문.
tags: [graphrag, retrieval, knowledge-graph, survey, taxonomy]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2408.08921
authors: [Boci Peng, Yun Zhu, Yongchao Liu, Xiaohe Bo, Haizhou Shi, Chuntao Hong, Yan Zhang, Siliang Tang]
year: 2024
venue: arXiv preprint
arxiv: "2408.08921"
---

# Graph RAG: A Survey (Peng et al.)

"Graph Retrieval-Augmented Generation: A Survey"는 Boci Peng 등이 2024년에 발표한 서베이로, [GraphRAG (the paradigm)](../concepts/graph-rag.md)를 하나의 통일된 워크플로로 정형화한 초기 종합 정리에 해당한다. 일반 [RAG (Retrieval-Augmented Generation)](../concepts/retrieval-augmented-generation.md)가 평면적인 텍스트 [청킹 (Text Chunking)](../concepts/text-chunking.md)과 [Dense Retrieval / Vector Search](../concepts/dense-retrieval.md)에 의존해 개체 간 관계나 전역적 맥락을 놓치는 한계를 출발점으로 삼는다. 이를 보완하기 위해 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md)와 같은 그래프 구조를 검색 단위로 끌어들이는 흐름을 정리한다.

## 범위

검색 대상이 평면 문서가 아니라 그래프(특히 지식 그래프)인 RAG 연구 전반을 다룬다. 그래프 구축·색인부터 검색, 생성까지의 파이프라인과, 이를 적용하는 다운스트림 과제·도메인·벤치마크를 포괄한다. 100편 이상의 논문을 인용하며 [Large Language Model (LLM)](../concepts/large-language-model.md) 시대의 그래프 기반 검색을 조망한다.

## 다루는 내용(분류 체계)

저자들은 GraphRAG를 세 단계의 워크플로로 정형화한다. (1) graph-based indexing은 자체 구축 데이터나 공개 KG로부터 그래프 데이터베이스를 만드는 [지식 그래프 구축 (Knowledge Graph Construction)](../techniques/knowledge-graph-construction.md) 단계다. (2) graph-guided retrieval은 다양한 검색 패러다임과 강화 기법으로 [부분그래프 추출 (Subgraph Extraction)](../techniques/subgraph-extraction.md)이나 [그래프 순회 추론 (Graph Traversal Reasoning)](../techniques/graph-traversal-reasoning.md)을 통해 관련 그래프 정보를 뽑는다. (3) graph-enhanced generation은 검색된 그래프 정보를 생성기에 맞는 형태로 변환한다. 또한 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md)을 포함한 QA, 생물의학 등 여러 도메인의 응용과 평가 데이터셋을 함께 정리한다.

## 핵심 시사점

그래프 구조를 도입하면 다중 문서·다중 개체에 걸친 관계를 명시적으로 검색할 수 있어, 평면 벡터 검색이 약한 멀티홉·전역 질의에서 [환각 (Hallucination)](../concepts/hallucination.md)을 줄이는 데 유리하다. 동시에 그래프 구축·유지 비용, 검색 방식의 표준화 부재, 평가 체계의 미성숙이 공통 과제로 지적된다.

## 관련 항목
- [GraphRAG (the paradigm)](../concepts/graph-rag.md) — 이 서베이가 정형화한 핵심 패러다임.
- [RAG with Graphs (Han et al.)](graphrag-with-graphs-survey.md) — 같은 주제를 다루는 대표적 후속 서베이.
- [RAG for LLMs: A Survey (Gao et al.)](rag-survey.md) — 그래프 이전의 일반 RAG 지형을 정리한 상위 서베이.
- [Unifying LLMs and KGs: A Roadmap](llm-kg-roadmap.md) — LLM과 KG 통합을 다루는 인접 서베이.
- [Microsoft GraphRAG](../methods/microsoft-graphrag.md) — 서베이가 분류하는 전역 검색형 대표 기법.
- [HippoRAG](../methods/hipporag.md) — graph-guided retrieval에 해당하는 대표 검색 기법.
- [Think-on-Graph (ToG)](../methods/think-on-graph.md) — 그래프 순회 추론 계열의 대표 사례.
- [Knowledge Graph QA (KGQA)](../concepts/knowledge-graph-question-answering.md) — 서베이가 다루는 핵심 다운스트림 과제.

## 참고문헌
- Peng, B., Zhu, Y., Liu, Y., Bo, X., Shi, H., Hong, C., Zhang, Y., & Tang, S. (2024). *Graph Retrieval-Augmented Generation: A Survey*. arXiv preprint. arXiv:2408.08921 — https://arxiv.org/abs/2408.08921
