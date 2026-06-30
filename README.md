# GraphRAG 지식 위키 (LLMWiki · GraphRAG)

**GraphRAG**(그래프 기반 검색 증강 생성)에 관한 논문·방법론·기법·도구·벤치마크를 한국어로 정리한 지식 위키입니다.
[Andrej Karpathy의 "LLM Wiki" 패턴](https://github.com/karpathy)을 표준화한 Google의 **OKF(Open Knowledge Format)** 로 작성되어, 사람과 AI 에이전트가 모두 읽고 확장할 수 있으며, 그대로 **Obsidian 보관소(vault)** 로 열 수 있습니다.

> GraphRAG는 평면 벡터 저장소가 아니라 **그래프/지식 그래프** 위에서 검색하는 RAG입니다. 문서에서 개체·관계를 추출해 그래프 인덱스를 만들고, 지역(local)·전역(global) 질의에 맞춰 그래프를 탐색·요약합니다.

---

## OKF(Open Knowledge Format)란?

OKF는 조직의 지식을 **마크다운 + YAML 프런트매터** 파일들의 디렉터리로 저장하는, 벤더 중립적인 개방형 명세입니다(Google Cloud, 2026). 핵심 규칙은 단순합니다.

- 모든 **개념(concept)** 은 하나의 `.md` 파일이며, 프런트매터에 **`type` 필드 1개만 필수**입니다.
- 권장 필드: `title`, `description`, `resource`(대표 URL), `tags`, `timestamp`.
- 파일은 일반 **마크다운 링크**로 서로 연결되어 살아있는 위키(그래프)를 이룹니다.
- 예약 파일: 디렉터리 목록인 `index.md`, 변경 이력인 `log.md`. 루트 `index.md`만 `okf_version`을 선언합니다.

Obsidian 대응: **보관소 ≈ 번들**, **노트 ≈ 개념**, **YAML 블록 ≈ 프런트매터**, **링크 ≈ 위키링크**. 이 저장소는 두 규약을 동시에 만족하도록 상대 경로 마크다운 링크를 사용합니다.

참고: [OKF SPEC](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) · [Google Cloud 발표](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)

---

## 구조

```
.
├── index.md                 # OKF 매니페스트 + 위키 홈 (okf_version: "0.1")
├── log.md                   # 변경 이력
├── README.md                # 이 문서
├── concepts/                # 개념 — RAG, 지식 그래프, 멀티홉 추론 등
├── methods/                 # 방법론 — Microsoft GraphRAG, LightRAG, HippoRAG …
├── techniques/              # 기법 — 커뮤니티 탐지, PPR, 그래프 순회 …
├── surveys/                 # 서베이 논문
├── tools/                   # 오픈소스 라이브러리·DB
├── benchmarks/              # 평가 데이터셋
└── .obsidian/               # Obsidian 보관소 설정(그래프 색상 그룹 등)
```

각 섹션 디렉터리에는 해당 노트를 안내하는 `index.md`가 있습니다. 시작점은 루트 [`index.md`](index.md)입니다.

### 주요 노트

- 패러다임: [GraphRAG](concepts/graph-rag.md) · [RAG](concepts/retrieval-augmented-generation.md) · [지식 그래프](concepts/knowledge-graph.md)
- 대표 시스템: [Microsoft GraphRAG](methods/microsoft-graphrag.md) · [LightRAG](methods/lightrag.md) · [HippoRAG](methods/hipporag.md) · [RAPTOR](methods/raptor.md) · [Think-on-Graph](methods/think-on-graph.md)
- 서베이: [Graph RAG: A Survey](surveys/graph-rag-survey.md) · [RAG for LLMs: A Survey](surveys/rag-survey.md)

---

## Obsidian에서 열기

1. [Obsidian](https://obsidian.md)을 설치합니다.
2. **`폴더를 보관소로 열기`(Open folder as vault)** 를 선택하고 이 저장소 폴더를 지정합니다.
3. 좌측의 **그래프 뷰**를 열면 섹션별로 색이 입혀진 노트 그래프가 보입니다. 백링크·태그·아웃라인 패널도 바로 동작합니다.

`.obsidian/app.json`은 **마크다운 링크 + 상대 경로** 모드로 설정되어 있어, Obsidian에서 새로 만드는 링크도 OKF 규약과 호환됩니다.

---

## 노트 형식

```markdown
---
type: Method
title: Microsoft GraphRAG
description: 문서에서 지식 그래프를 만들고 커뮤니티 요약으로 전역 질의에 답하는 GraphRAG 시스템.
tags: [graphrag, microsoft, knowledge-graph, query-focused-summarization]
authors: [Darren Edge, Ha Trinh, ...]
year: 2024
venue: arXiv
arxiv: "2404.16130"
resource: https://arxiv.org/abs/2404.16130
timestamp: 2026-06-29
---

# Microsoft GraphRAG

(한국어 본문: 개요 / 핵심 아이디어 / 기여 / 강점과 한계 …)

## 관련 항목
- [LightRAG](lightrag.md) — 더 가벼운 그래프 인덱싱·검색 대안

## 참고문헌
- Edge et al. (2024). *From Local to Global: A Graph RAG Approach…*. arXiv:2404.16130 — https://arxiv.org/abs/2404.16130
```

`type` 값: `Concept` · `Method` · `Technique` · `Survey` · `Tool` · `Benchmark`.

---

## 🔄 자동 업데이트 (매주 월요일)

매주 월요일, GraphRAG 관련 **최신 arXiv 논문**을 자동으로 찾아 새 OKF 노트로 추가하는 루틴이 포함되어 있습니다. GitHub Actions에서 동작하며(`.github/workflows/weekly-graphrag-update.yml`), 다음 `git pull` 때 Obsidian에 그대로 반영됩니다.

- **최초 설정:** 레포 `Settings → Secrets and variables → Actions` 에 `ANTHROPIC_API_KEY` 시크릿 1개만 추가하면 됩니다.
- **바로 실행:** `Actions → Weekly GraphRAG paper update → Run workflow` (`dry_run=true` 로 후보만 미리보기 가능).
- 자세한 동작·튜닝·API 키 없이 쓰는 대안: **[automation/weekly-paper-update.md](automation/weekly-paper-update.md)**

서지정보(저자·연도·arXiv ID)는 arXiv 메타데이터로 코드가 직접 채우므로 인용 오류 위험이 낮고, 추가된 논문은 [log.md](log.md)에 날짜별로 기록됩니다.

---

## 유의사항

- 각 노트의 본문은 1차 자료(주로 arXiv 논문)를 바탕으로 작성한 **원작 한국어 요약**이며, 저자·연도·arXiv ID 등 서지 정보는 검증을 거쳤습니다. 다만 자동 생성 과정의 특성상 오류가 있을 수 있으니 중요한 사실은 원문으로 확인하세요.
- 인용된 논문·도구의 저작권은 각 저자/조직에 있습니다. 이 위키 텍스트는 학습·참고용 요약입니다.
