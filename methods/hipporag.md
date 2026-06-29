---
type: Method
title: HippoRAG
description: 인간 장기 기억의 해마 색인 이론에서 착안한 GraphRAG 기법으로, 코퍼스로부터 지식 그래프를 구축하고 Personalized PageRank를 실행해 여러 문서에 흩어진 근거를 단일 검색 단계로 모은다.
tags: [graphrag, retrieval, knowledge-graph, personalized-pagerank, multi-hop-reasoning, long-term-memory]
timestamp: 2026-06-29
resource: https://arxiv.org/abs/2405.14831
authors: [Bernal Jiménez Gutiérrez, Yiheng Shu, Yu Gu, Michihiro Yasunaga, Yu Su]
year: 2024
venue: NeurIPS 2024
arxiv: "2405.14831"
---

# HippoRAG

HippoRAG는 인간 장기 기억의 해마 색인 이론(hippocampal indexing theory)에서 착안해 여러 문서에 흩어진 지식을 통합하는 [GraphRAG](../concepts/graph-rag.md) 기법이다. [LLM](../concepts/large-language-model.md), 코퍼스에서 만든 [지식 그래프 (Knowledge Graph)](../concepts/knowledge-graph.md), 그리고 [Personalized PageRank](../techniques/personalized-pagerank.md) 알고리즘을 함께 엮어, 단일 검색 단계만으로 여러 구절에 걸친 근거를 한 번에 모은다. Gutiérrez et al.(2024)이 제안했으며, 일반적인 [RAG](../concepts/retrieval-augmented-generation.md)가 어려워하는 멀티홉 상황을 겨냥한다.

## 개요

표준 밀집 검색(dense retrieval)은 각 구절을 독립적으로 가져오기 때문에, 여러 문서에 걸쳐 연결해야 하는 사실을 놓치고 값비싼 반복 검색에 의존하게 된다. HippoRAG는 대신 오프라인에서 연상 기억처럼 동작하는 색인을 미리 만든다. 여기서 LLM은 지식을 추출하는 "신피질(neocortex)" 역할을, 그래프와 PageRank는 관련 항목을 잇는 "해마 색인(hippocampal index)" 역할을 맡아, 더 저렴한 단일 단계 [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md)을 가능하게 한다.

## 핵심 아이디어 / 동작 방식

색인 단계에서 LLM이 코퍼스에 대해 [개체 및 관계 추출 (Entity & Relationship Extraction)](../techniques/entity-relationship-extraction.md)을 수행해 개념들의 개방형 지식 그래프를 구성하고, 검색 인코더가 유사한 개체 사이에 동의어 간선을 추가한다. 질의 시점에는 LLM이 질문 속 개체를 식별하고, 이들이 [Personalized PageRank](../techniques/personalized-pagerank.md)의 시드 노드가 된다. PageRank는 그래프 위로 확률을 전파하며 연결된 개체를 기준으로 구절에 점수를 매긴다. 이 패턴 완성(pattern completion) 단계는 반복적인 [밀집 검색 (Dense Retrieval)](../concepts/dense-retrieval.md) 없이 한 번의 패스로 연결된 근거 집합을 가져온다.

## 기여

- LLM 추출, 지식 그래프, PageRank를 신피질과 해마의 역할에 대응시킨 신경생물학적 동기의 설계.
- IRCoT 같은 반복 방식에 필적하거나 이를 능가하면서 훨씬 저렴하고 빠른 단일 단계 멀티홉 검색.
- [MuSiQue](../benchmarks/musique.md), [2WikiMultiHopQA](../benchmarks/2wikimultihopqa.md) 등 멀티홉 QA 벤치마크에서의 성능 향상.

## 강점과 한계

HippoRAG는 질의당 여러 번의 LLM 호출 없이도 멀티홉 정확도를 높이는 효율적이고 온라인 갱신이 가능한 검색을 제공한다. 한계로는 그래프 충실도가 LLM 추출 품질에 의존한다는 점, 개체 연결 오류에 민감하다는 점, 그리고 개체 연상보다 관계 자체에 의존하는 질문을 다소 약하게 처리한다는 점이 있다.

## 관련 항목
- [HippoRAG 2](hipporag-2.md) — 지속 학습과 더 깊은 구절 통합으로 이 프레임워크를 확장한 후속 기법
- [GraphRAG (패러다임)](../concepts/graph-rag.md) — HippoRAG가 구현하는 상위 패러다임
- [LightRAG](lightrag.md) — 이중 수준 검색을 쓰는 동시대의 graph-RAG 기법
- [Microsoft GraphRAG](microsoft-graphrag.md) — 비교 대상이 되는 커뮤니티 요약형 graph-RAG 파이프라인
- [Personalized PageRank](../techniques/personalized-pagerank.md) — HippoRAG 검색의 핵심 그래프 알고리즘
- [멀티홉 추론 (Multi-hop Reasoning)](../concepts/multi-hop-reasoning.md) — HippoRAG가 주로 겨냥하는 역량
- [MuSiQue](../benchmarks/musique.md) — HippoRAG 평가에 쓰인 멀티홉 QA 벤치마크
- [개체 및 관계 추출 (Entity & Relationship Extraction)](../techniques/entity-relationship-extraction.md) — HippoRAG의 지식 그래프를 만드는 단계

## 참고문헌
- Gutiérrez, B. J., Shu, Y., Gu, Y., Yasunaga, M., & Su, Y. (2024). *HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models*. NeurIPS 2024. arXiv:2405.14831 — https://arxiv.org/abs/2405.14831
