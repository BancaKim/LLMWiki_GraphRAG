# 변경 이력 (Changelog)

GraphRAG 지식 위키의 시간순 변경 기록입니다.

## 2026-07-23 — 주간 자동 업데이트 (최신 논문 반영)

최신 GraphRAG 논문 8건을 반영해 노트를 57 → 65개로 확장했습니다:

- `methods/gfm-rag.md` — GFM-RAG (arXiv:2502.01113)
- `methods/hypergraphrag.md` — HyperGraphRAG (arXiv:2503.21322)
- `methods/noderag.md` — NodeRAG (arXiv:2504.11544)
- `methods/kag.md` — KAG (Knowledge Augmented Generation) (arXiv:2409.13731)
- `methods/pathrag.md` — PathRAG (arXiv:2502.14902)
- `methods/minirag.md` — MiniRAG (arXiv:2501.06713)
- `methods/youtu-graphrag.md` — Youtu-GraphRAG (arXiv:2508.19855)
- `benchmarks/graphrag-bench.md` — GraphRAG-Bench (arXiv:2506.02404)

## 2026-06-29 — 최초 번들 (OKF v0.1)

6개 섹션에 걸쳐 **57개의 노트**로 위키를 생성했습니다:

- **개념 (Concepts)** (11): Dense Retrieval / Vector Search, GraphRAG (the paradigm), Hallucination (환각), Knowledge Graph QA (KGQA), Large Language Model (LLM), Multi-hop Reasoning (멀티홉 추론), Query-Focused Summarization (QFS), Retrieval-Augmented Generation (RAG), Text Chunking (청킹), Text Embedding (텍스트 임베딩), 지식 그래프 (Knowledge Graph)
- **방법론 (Methods)** (18): G-Retriever, GNN-RAG, GRAG, GraphReader, HippoRAG, HippoRAG 2, KAPING, Knowledge Graph Prompting (KGP), LazyGraphRAG, LightRAG, MedGraphRAG, Microsoft GraphRAG, RAPTOR, Reasoning on Graphs (RoG), StructGPT, SubgraphRAG, Think-on-Graph (ToG), Think-on-Graph 2.0
- **기법 (Techniques)** (12): Community Detection (Leiden), Community Summarization, DRIFT Search, Entity & Relationship Extraction, Graph Neural Network (GNN), Graph Traversal Reasoning, Hierarchical Clustering, Hybrid Retrieval, Knowledge Graph Construction, Local vs Global Search, Personalized PageRank, Subgraph Extraction
- **서베이 (Surveys)** (4): Graph RAG: A Survey (Peng et al.), RAG for LLMs: A Survey (Gao et al.), RAG with Graphs (Han et al.), Unifying LLMs and KGs: A Roadmap
- **도구 (Tools)** (6): LangChain LLMGraphTransformer, LightRAG (HKUDS library), LlamaIndex PropertyGraphIndex, Neo4j, microsoft/graphrag (library), nano-graphrag
- **벤치마크 (Benchmarks)** (6): 2WikiMultiHopQA, ComplexWebQuestions (CWQ), HotpotQA, MuSiQue, NarrativeQA, WebQuestionsSP (WebQSP)

이와 함께 루트 `index.md`(OKF 매니페스트 + 보관소 홈), 섹션별 `index.md` 목록, `.obsidian/` 보관소 설정, 그리고 이 변경 이력을 추가했습니다.
