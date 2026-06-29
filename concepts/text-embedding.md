---
type: Concept
title: Text Embedding (텍스트 임베딩)
description: 단어·문장·구절 등의 텍스트를 의미적 유사성이 거리로 반영되도록 고정 차원의 밀집 벡터로 사상한 표현으로, 유사도 검색과 그래프 노드·개체의 특징 벡터로 쓰인다.
tags: [text-embedding, retrieval, dense-retrieval, graphrag, vector-search]
timestamp: 2026-06-29
---

# Text Embedding (텍스트 임베딩)

Text Embedding(텍스트 임베딩)은 단어, 문장, 단락 같은 텍스트를 고정된 차원의 실수 벡터로 변환한 표현이다. 의미가 비슷한 텍스트일수록 벡터 공간에서 서로 가깝게 배치되도록 학습되며, 이를 통해 코사인 유사도 같은 거리 척도로 의미적 관련성을 수치로 계산할 수 있다. 오늘날에는 주로 [LLM (Large Language Model)](large-language-model.md) 계열의 인코더 모델이 임베딩을 생성한다.

## 정의

임베딩 모델은 입력 텍스트를 받아 보통 수백~수천 차원의 밀집 벡터(dense vector)를 출력한다. 대규모 말뭉치로 학습하는 과정에서, 함께 등장하거나 비슷한 맥락에서 쓰이는 표현들이 벡터 공간상 가까운 위치로 모이도록 매개변수가 조정된다. 그 결과 어휘가 정확히 일치하지 않아도 의미가 통하는 텍스트를 가까운 벡터로 인식할 수 있어, 키워드 일치에 의존하는 희소(sparse) 표현의 한계를 보완한다.

## GraphRAG에서 중요한 이유

임베딩은 [Dense Retrieval / Vector Search](dense-retrieval.md)의 토대로, 질의와 후보 텍스트를 같은 공간에 사상해 가장 가까운 것을 검색한다. 이는 [RAG (Retrieval-Augmented Generation)](retrieval-augmented-generation.md)에서 관련 [청크 (Text Chunking)](text-chunking.md)를 찾는 표준 수단이다. [GraphRAG (the paradigm)](graph-rag.md)에서는 검색뿐 아니라 그래프의 노드·개체·관계, 그리고 [Knowledge Graph](knowledge-graph.md)에서 추출된 요소에 특징 벡터를 부여하는 데도 쓰인다. 예를 들어 [HippoRAG](../methods/hipporag.md)는 질의와 그래프 개체를 임베딩으로 연결하고, 여러 시스템이 벡터 검색과 그래프 구조를 결합한 [Hybrid Retrieval](../techniques/hybrid-retrieval.md)을 구성한다.

## 실제 활용

임베딩은 색인을 미리 구축해 두면 질의 시점에 근사 최근접 이웃 탐색으로 빠르게 검색할 수 있어, 검색 파이프라인의 1차 후보 선별에 널리 쓰인다. 또한 [Graph Neural Network (GNN)](../techniques/graph-neural-network.md)의 초기 노드 특징, 개체 정규화·중복 병합, 텍스트 군집화 등 그래프 구축 전반에서 입력 표현으로 활용된다.

## 관련 항목
- [Dense Retrieval / Vector Search](dense-retrieval.md) — 임베딩 벡터를 직접 이용해 유사도로 검색하는 방식
- [Retrieval-Augmented Generation (RAG)](retrieval-augmented-generation.md) — 임베딩 기반 검색으로 관련 문맥을 가져오는 상위 프레임워크
- [Text Chunking (청킹)](text-chunking.md) — 임베딩을 부여해 색인하는 검색 단위를 만드는 전처리
- [GraphRAG (the paradigm)](graph-rag.md) — 노드·개체 특징과 검색에 임베딩을 활용하는 패러다임
- [Knowledge Graph](knowledge-graph.md) — 임베딩으로 개체·관계를 벡터화해 연결하는 그래프 구조
- [Hybrid Retrieval](../techniques/hybrid-retrieval.md) — 벡터 임베딩 검색과 그래프 검색을 결합하는 전략
- [Graph Neural Network (GNN)](../techniques/graph-neural-network.md) — 텍스트 임베딩을 초기 노드 특징으로 받는 그래프 학습 모델
- [HippoRAG](../methods/hipporag.md) — 질의와 그래프 개체를 임베딩으로 연결하는 대표 기법
