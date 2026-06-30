# 주간 자동 업데이트 루틴 (매주 월요일)

매주 월요일, **GraphRAG 관련 최신 arXiv 논문**을 자동으로 찾아 이 위키에 OKF 노트로 추가하는 루틴입니다.
GitHub Actions(레포 자체 인프라)에서 돌기 때문에, Claude 세션이 켜져 있지 않아도 동작합니다.

## 동작 방식

`.github/workflows/weekly-graphrag-update.yml` → `scripts/weekly_update.py`:

1. **검색** — arXiv API에서 최근 `LOOKBACK_DAYS`(기본 8일)일치 GraphRAG 관련 논문을 가져옵니다.
   (검색어: `GraphRAG`, `graph retrieval-augmented generation`, `knowledge graph`+`retrieval-augmented generation` 등)
2. **중복 제거** — 이미 위키에 있는 arXiv ID·제목은 건너뜁니다.
3. **선별(triage)** — 모델이 "그래프/지식그래프가 검색·추론의 핵심인지"를 엄격히 판단해 무관한 논문을 거릅니다. 적합하면 섹션(`methods`/`surveys`/`techniques`/`concepts`/`tools`/`benchmarks`)과 OKF `type`을 정합니다.
4. **작성** — 한국어 OKF 노트를 생성합니다. **서지정보(저자·연도·arXiv ID·resource URL)는 arXiv 메타데이터로 코드가 직접 채우므로** 환각이 발생하지 않습니다. 모델은 description·tags·본문·관련링크만 작성합니다.
5. **반영** — `scripts/build_wiki.py`로 인덱스/루트/링크를 갱신하고, `log.md`에 날짜별 항목을 추가한 뒤, 변경분을 커밋·푸시합니다.
6. 다음 번 `git pull` 시 **Obsidian 보관소에 그대로 나타납니다.**

한 번에 추가하는 노트는 `MAX_NEW`(기본 6건)로 제한합니다. 새 논문이 없으면 아무것도 커밋하지 않습니다.

## 최초 1회 설정 (필수)

1. GitHub 레포 → **Settings → Secrets and variables → Actions → New repository secret**
   - Name: `ANTHROPIC_API_KEY`
   - Value: 본인의 Anthropic API 키 (<https://console.anthropic.com> → API Keys)
2. (선택) 같은 화면의 **Variables** 탭에서 `ANTHROPIC_MODEL` 변수를 추가하면 사용할 모델을 바꿀 수 있습니다(미설정 시 `claude-sonnet-4-6`).
3. 끝. 다음 월요일 09:13(KST)에 처음 실행됩니다.

> 이 워크플로는 **기본 브랜치**(`claude/llm-wiki-okf-format-ginkwm`)에서 스케줄로 실행되고, 같은 브랜치로 푸시합니다. 기본 브랜치를 바꾸면 워크플로 파일도 그 브랜치에 있어야 스케줄이 동작합니다.

## 바로 한 번 실행해보기 (스케줄 기다리지 않고)

GitHub 레포 → **Actions → "Weekly GraphRAG paper update" → Run workflow**.
- `dry_run = true` 로 돌리면 **아무것도 쓰지 않고** 후보 논문 목록만 로그로 보여줍니다(검색이 잘 되는지 확인용).
- `lookback_days`, `max_new` 도 즉석에서 조정할 수 있습니다.

## 로컬에서 테스트

```bash
# 후보만 출력 (API 키 불필요, 네트워크만 필요)
DRY_RUN=1 LOOKBACK_DAYS=30 python scripts/weekly_update.py

# 실제 작성까지 (푸시는 안 함). API 키 필요.
export ANTHROPIC_API_KEY=sk-...
python scripts/weekly_update.py        # 파일만 생성/수정, git 작업은 WEEKLY_PUSH=1 일 때만
```

## 튜닝

| 무엇 | 어디 |
|---|---|
| 실행 요일·시각 | `.github/workflows/weekly-graphrag-update.yml` 의 `cron` (UTC 기준) |
| 검색어 | `scripts/weekly_update.py` 의 `ARXIV_QUERIES` |
| 검색 기간 / 최대 건수 | 워크플로 입력값 또는 env `LOOKBACK_DAYS` / `MAX_NEW` |
| 선별 기준 | `scripts/weekly_update.py` 의 `triage()` 프롬프트 |
| 노트 형식 | `assemble()` (프런트매터) + `author()` (본문 프롬프트) |

## API 키 없이 쓰고 싶다면 (대안)

완전 자동 대신 **반자동**으로 운영할 수 있습니다. 매주 Claude Code 세션을 하나 열고 다음과 같이 요청하세요:

> "이 레포에서 `automation/weekly-paper-update.md`의 절차대로, 지난 한 주의 GraphRAG 최신 논문을 찾아 새 OKF 노트를 추가하고 인덱스·로그를 갱신한 뒤 `claude/llm-wiki-okf-format-ginkwm`에 커밋·푸시해줘."

이 경우 모델 호출은 세션이 대신 처리하므로 별도 API 키가 필요 없습니다(다만 직접 트리거해야 합니다).
