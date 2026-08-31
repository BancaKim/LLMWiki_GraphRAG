# 변경 이력 (Changelog)

GraphRAG 지식 위키의 시간순 변경 기록입니다.

## 2026-08-31 — 온톨로지 기반·뉴로심볼릭 GraphRAG 반영

"온톨로지 기반 뉴로심볼릭 GraphRAG가 주요 학회에 억셉됐는가"를 조사해, 확인된 사례를 반영했습니다. 노트 77 → 80개.

- `methods/og-rag.md` — OG-RAG (arXiv:2412.15235, **EMNLP 2025 Main**) — 도메인 온톨로지에 근거한 하이퍼그래프 표현, 질의별 최소 하이퍼엣지 집합을 최적화로 선택. 사실 재현율 +55%, 응답 정확성 +40%.
- `methods/clause.md` — CLAUSE (arXiv:2509.21035, **ICLR 2026**) — 그래프 컨텍스트 구성을 예산 제약 순차 의사결정으로 정식화, 3개 에이전트를 LC-MAPPO로 공동 최적화.
- `concepts/neurosymbolic-graphrag.md` — 온톨로지 기반·뉴로심볼릭 GraphRAG (신규 주제 축) — 두 축(온톨로지 근거 / 뉴로심볼릭 추론)과 학회 게재 현황, 남은 과제 정리.

`graph-rag`·`knowledge-graph-construction`·`hypergraphrag`에서 역방향 링크를 연결했습니다.

## 2026-08-18 — AGRAG · EA-GraphRAG · Is GraphRAG Needed? 추가

- `methods/agrag.md` — AGRAG (arXiv:2511.05549) — LLM 엔터티 추출을 n-gram·TF-IDF 통계 방식으로 대체하고, 검색을 MCMI(최소 비용 최대 영향) 부분 그래프 생성 문제로 정식화.
- `methods/ea-graphrag.md` — EA-GraphRAG / "Use Graph When It Needs" (arXiv:2602.03578) — 질의 구문 복잡도를 점수화해 밀집 RAG와 그래프 검색으로 라우팅하고 경계 사례는 RRF로 융합.
- `surveys/is-graphrag-needed.md` — Is GraphRAG Needed? (arXiv:2606.25656, GEM 2026 / ACL Anthology 2026.gem-main.40) — 표준·그래프·모듈형·에이전틱 RAG를 9가지 표준 시나리오로 구현해 비교하고, 토큰 19~53% 절감 컨텍스트 엔지니어링 제시 (AWS·Cisco).

세 편 모두 '그래프가 정말 필요한가' 클러스터(`when-to-use-graphs-in-rag`·`ragsearch`·`logicrag`)와 양방향으로 연결했습니다.

## 2026-08-18 — Deep GraphRAG 추가

- `methods/deep-graphrag.md` — Deep GraphRAG (arXiv:2601.11144) — 전역·지역 검색의 상충을 계층적 global-to-local 3단계 검색으로 절충하고, DW-GRPO 강화학습으로 1.5B 소형 모델이 지식 통합을 맡도록 한 기법.

직전 갱신에서 누락된 논문으로, 표기가 `DeepGraphRAG`가 아닌 `Deep GraphRAG`(띄어쓰기)여서 검색에 걸리지 않았습니다. `local-and-global-search`·`drift-search`에서 역방향 링크를 연결했습니다.

## 2026-08-18 — 최신 논문 반영 (2025 하반기 ~ 2026)

직전 갱신이 2025년 8월(arXiv 2508)까지만 다루고 있어, 이후 1년치 주요 연구를 반영했습니다. 노트 65 → 73개.

- `methods/linearrag.md` — LinearRAG (arXiv:2510.10114, ICLR 2026)
- `methods/graphsearch.md` — GraphSearch (arXiv:2509.22009, arXiv)
- `methods/prograg.md` — ProgRAG (arXiv:2511.10240, arXiv)
- `methods/logicrag.md` — LogicRAG (arXiv:2508.06105, AAAI 2026)
- `methods/memgraphrag.md` — MemGraphRAG (arXiv:2606.00610, KDD 2026)
- `benchmarks/ragsearch.md` — RAGSearch (Do We Still Need GraphRAG?) (arXiv:2604.09666, arXiv)
- `surveys/when-to-use-graphs-in-rag.md` — When to use Graphs in RAG (arXiv:2506.05690, ICLR 2026)
- `concepts/graphrag-security.md` — GraphRAG 보안과 지식 포이즈닝 (신규 주제 축; GraphRAG under Fire·LogicPoison·KEPo·ShadowMerge 정리)

이번 갱신의 축: **효율화**(LinearRAG·LogicRAG), **에이전틱 검색**(GraphSearch·ProgRAG·MemGraphRAG), **'그래프가 정말 필요한가' 논쟁**(When to use Graphs in RAG·RAGSearch), **보안**(신규).

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
