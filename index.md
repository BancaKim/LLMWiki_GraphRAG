---
okf_version: '0.1'
title: GraphRAG 지식 위키
description: GraphRAG 논문·방법론·기법·도구·벤치마크를 정리한 Open Knowledge Format(OKF) 위키이자 Obsidian
  보관소(vault).
timestamp: '2026-08-31'
---

# GraphRAG 지식 위키

**GraphRAG** — 평면 벡터 저장소 대신 그래프와 지식 그래프 위에서 검색하는 검색 증강 생성(RAG) — 을 다루는, 서로 촘촘히 연결된 한국어 지식 베이스입니다. [Open Knowledge Format(OKF)](https://github.com/GoogleCloudPlatform/knowledge-catalog) (마크다운 + YAML 프런트매터)로 작성되었으며, 동시에 [Obsidian](https://obsidian.md) 보관소이기도 합니다. 이 폴더를 보관소로 열면 그래프 뷰가 전체 80개 노트를 연결해 보여줍니다.

## 여기서 시작하기

- [GraphRAG (패러다임)](concepts/graph-rag.md) — GraphRAG가 무엇이고 왜 등장했는가
- [검색 증강 생성 (RAG)](concepts/retrieval-augmented-generation.md) — 모태가 되는 패러다임
- [Microsoft GraphRAG](methods/microsoft-graphrag.md) — 'GraphRAG'라는 용어를 널리 알린 연구
- [Graph RAG: A Survey](surveys/graph-rag-survey.md) — 전체 지형을 한눈에

## 섹션

- **[개념 (Concepts)](concepts/index.md)** (13) — 검색 증강 생성, 임베딩, 지식 그래프, 그래프 기반 추론의 토대가 되는 핵심 개념.
- **[방법론 (Methods)](methods/index.md)** (35) — Microsoft GraphRAG부터 경량·KG 추론 계열까지, 구체적인 GraphRAG 시스템과 이를 제안한 논문.
- **[기법 (Techniques)](techniques/index.md)** (12) — 그래프 구축, 커뮤니티 탐지, 그래프 순회, GNN 등 여러 GraphRAG 시스템이 공유하는 재사용 가능한 구성 요소와 알고리즘.
- **[서베이 (Surveys)](surveys/index.md)** (6) — GraphRAG / RAG / 지식 그래프 지형을 정리한 서베이 논문.
- **[도구 (Tools)](tools/index.md)** (6) — GraphRAG 파이프라인 구축을 위한 오픈소스 라이브러리와 데이터베이스.
- **[벤치마크 (Benchmarks)](benchmarks/index.md)** (8) — (Graph)RAG, 멀티홉 QA, 지식 그래프 질의응답(KGQA)을 평가하는 데이터셋.

## 위키 사용 방법

- **GitHub에서 보기:** 모든 노트는 순수 마크다운이며, 링크는 GitHub 파일 뷰어에서 그대로 작동합니다.
- **Obsidian에서 열기:** `폴더를 보관소로 열기(Open folder as vault)` → 이 디렉터리 선택. 링크·백링크·태그·그래프 뷰가 바로 동작합니다(자세한 내용은 [README](README.md) 참고).
- **에이전트에 제공:** 이 번들은 OKF를 준수하므로, OKF를 이해하는 에이전트가 읽고 순회하며 확장할 수 있습니다.

매주 월요일 최신 논문이 자동으로 반영됩니다 — [automation/weekly-paper-update.md](automation/weekly-paper-update.md). 변경 이력은 [log.md](log.md)를 참고하세요.
