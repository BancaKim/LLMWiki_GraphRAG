#!/usr/bin/env python3
"""Regenerate OKF indexes + validate conformance + repair relative links.

Run from anywhere; the wiki root is the parent of this script's directory
(override with the WIKI_ROOT env var).

What it does, idempotently:
  - rewrites every section `index.md` and the root `index.md` from the notes'
    frontmatter (titles, descriptions, counts),
  - seeds `log.md` only if it is missing (never clobbers the change history),
  - checks every markdown `.md` link, auto-repairs broken relative links by
    slug, and reports any that remain broken or any OKF conformance problems.

Exit code is non-zero if a conformance problem or an unrepairable link remains.
"""
import os
import re
import sys
import glob
import datetime
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.environ.get("WIKI_ROOT") or os.path.dirname(HERE)
TS = datetime.date.today().isoformat()
OKF_VERSION = "0.1"

SECTIONS = [
    ("concepts",   "개념 (Concepts)",     "검색 증강 생성, 임베딩, 지식 그래프, 그래프 기반 추론의 토대가 되는 핵심 개념."),
    ("methods",    "방법론 (Methods)",    "Microsoft GraphRAG부터 경량·KG 추론 계열까지, 구체적인 GraphRAG 시스템과 이를 제안한 논문."),
    ("techniques", "기법 (Techniques)",   "그래프 구축, 커뮤니티 탐지, 그래프 순회, GNN 등 여러 GraphRAG 시스템이 공유하는 재사용 가능한 구성 요소와 알고리즘."),
    ("surveys",    "서베이 (Surveys)",    "GraphRAG / RAG / 지식 그래프 지형을 정리한 서베이 논문."),
    ("tools",      "도구 (Tools)",        "GraphRAG 파이프라인 구축을 위한 오픈소스 라이브러리와 데이터베이스."),
    ("benchmarks", "벤치마크 (Benchmarks)", "(Graph)RAG, 멀티홉 QA, 지식 그래프 질의응답(KGQA)을 평가하는 데이터셋."),
]
SECTION_DIRS = [s[0] for s in SECTIONS]
LINK_RE = re.compile(r'(?<!\!)\[([^\]]+)\]\(([^)]+)\)')


def parse_frontmatter(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = re.match(r'^---\n(.*?)\n---\n?', text, re.DOTALL)
    if not m:
        return None, text
    try:
        return (yaml.safe_load(m.group(1)) or {}), text
    except yaml.YAMLError as e:
        return {"__error__": str(e)}, text


def collect():
    data = {d: [] for d in SECTION_DIRS}
    for d in SECTION_DIRS:
        for path in sorted(glob.glob(os.path.join(ROOT, d, "*.md"))):
            base = os.path.basename(path)
            if base in ("index.md", "log.md"):
                continue
            slug = base[:-3]
            fm = parse_frontmatter(path)[0] or {}
            data[d].append({
                "slug": slug,
                "title": fm.get("title") or slug.replace("-", " ").title(),
                "description": (fm.get("description") or "").strip(),
                "fm": fm,
            })
    return data


def validate(data):
    problems = []
    for d in SECTION_DIRS:
        for e in data[d]:
            fm = e["fm"]
            if "__error__" in fm:
                problems.append(f"{d}/{e['slug']}.md: YAML error: {fm['__error__']}")
                continue
            if not (fm.get("type") and str(fm["type"]).strip()):
                problems.append(f"{d}/{e['slug']}.md: missing/empty required `type`")
            if not fm.get("title"):
                problems.append(f"{d}/{e['slug']}.md: missing `title`")
            if not fm.get("description"):
                problems.append(f"{d}/{e['slug']}.md: missing `description`")
    return problems


def write_section_indexes(data):
    for d, title, desc in SECTIONS:
        entries = sorted(data[d], key=lambda e: e["title"].lower())
        lines = [f"# {title}", "", desc, "", f"이 섹션에는 {len(entries)}개의 노트가 있습니다.", ""]
        for e in entries:
            tail = f" — {e['description']}" if e["description"] else ""
            lines.append(f"- [{e['title']}]({e['slug']}.md){tail}")
        lines += ["", "---", "", "[← 위키 홈](../index.md)", ""]
        with open(os.path.join(ROOT, d, "index.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines))


def write_root_index(data):
    total = sum(len(data[d]) for d in SECTION_DIRS)
    fm = {
        "okf_version": OKF_VERSION,
        "title": "GraphRAG 지식 위키",
        "description": "GraphRAG 논문·방법론·기법·도구·벤치마크를 정리한 Open Knowledge Format(OKF) 위키이자 Obsidian 보관소(vault).",
        "timestamp": TS,
    }
    b = []
    b.append("# GraphRAG 지식 위키")
    b.append("")
    b.append(
        "**GraphRAG** — 평면 벡터 저장소 대신 그래프와 지식 그래프 위에서 검색하는 검색 증강 생성(RAG) — 을 "
        "다루는, 서로 촘촘히 연결된 한국어 지식 베이스입니다. "
        "[Open Knowledge Format(OKF)](https://github.com/GoogleCloudPlatform/knowledge-catalog) "
        "(마크다운 + YAML 프런트매터)로 작성되었으며, 동시에 [Obsidian](https://obsidian.md) 보관소이기도 합니다. "
        f"이 폴더를 보관소로 열면 그래프 뷰가 전체 {total}개 노트를 연결해 보여줍니다."
    )
    b += ["", "## 여기서 시작하기", ""]
    b.append("- [GraphRAG (패러다임)](concepts/graph-rag.md) — GraphRAG가 무엇이고 왜 등장했는가")
    b.append("- [검색 증강 생성 (RAG)](concepts/retrieval-augmented-generation.md) — 모태가 되는 패러다임")
    b.append("- [Microsoft GraphRAG](methods/microsoft-graphrag.md) — 'GraphRAG'라는 용어를 널리 알린 연구")
    b.append("- [Graph RAG: A Survey](surveys/graph-rag-survey.md) — 전체 지형을 한눈에")
    b += ["", "## 섹션", ""]
    for d, title, desc in SECTIONS:
        b.append(f"- **[{title}]({d}/index.md)** ({len(data[d])}) — {desc}")
    b += ["", "## 위키 사용 방법", ""]
    b.append("- **GitHub에서 보기:** 모든 노트는 순수 마크다운이며, 링크는 GitHub 파일 뷰어에서 그대로 작동합니다.")
    b.append("- **Obsidian에서 열기:** `폴더를 보관소로 열기(Open folder as vault)` → 이 디렉터리 선택. 링크·백링크·태그·그래프 뷰가 바로 동작합니다(자세한 내용은 [README](README.md) 참고).")
    b.append("- **에이전트에 제공:** 이 번들은 OKF를 준수하므로, OKF를 이해하는 에이전트가 읽고 순회하며 확장할 수 있습니다.")
    b += ["", "매주 월요일 최신 논문이 자동으로 반영됩니다 — [automation/weekly-paper-update.md](automation/weekly-paper-update.md). 변경 이력은 [log.md](log.md)를 참고하세요.", ""]
    out = "---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip() + "\n---\n\n" + "\n".join(b)
    with open(os.path.join(ROOT, "index.md"), "w", encoding="utf-8") as f:
        f.write(out)
    return total


def seed_log_if_missing(data, total):
    p = os.path.join(ROOT, "log.md")
    if os.path.exists(p):
        return  # never clobber an existing change history
    lines = ["# 변경 이력 (Changelog)", "", "GraphRAG 지식 위키의 시간순 변경 기록입니다.", "",
             f"## {TS} — 최초 번들 (OKF v{OKF_VERSION})", "",
             f"6개 섹션에 걸쳐 **{total}개의 노트**로 위키를 생성했습니다.", ""]
    with open(p, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def all_md_files():
    out = [os.path.join(ROOT, b) for b in ("index.md", "log.md", "README.md") if os.path.exists(os.path.join(ROOT, b))]
    for d in SECTION_DIRS:
        out += sorted(glob.glob(os.path.join(ROOT, d, "*.md")))
    return out


def build_slug_map():
    m = {}
    for d in SECTION_DIRS:
        for path in glob.glob(os.path.join(ROOT, d, "*.md")):
            m[os.path.basename(path)] = os.path.relpath(path, ROOT)
    for b in ("index.md", "log.md", "README.md"):
        if os.path.exists(os.path.join(ROOT, b)):
            m.setdefault(b, b)
    return m


def check_and_fix_links(slug_map):
    broken, fixed = [], []
    for path in all_md_files():
        src_dir = os.path.dirname(path)
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()

        def repl(match):
            label, url = match.group(1), match.group(2)
            if re.match(r'^[a-z]+://', url) or url.startswith("mailto:") or url.startswith("#"):
                return match.group(0)
            target = url.split("#", 1)[0]
            anchor = url[len(target):]
            if not target.endswith(".md"):
                return match.group(0)
            if os.path.exists(os.path.normpath(os.path.join(src_dir, target))):
                return match.group(0)
            base = os.path.basename(target)
            if base in slug_map:
                newrel = os.path.relpath(os.path.join(ROOT, slug_map[base]), src_dir)
                if newrel != target:
                    fixed.append(f"{os.path.relpath(path, ROOT)}: '{url}' -> '{newrel}{anchor}'")
                    return f"[{label}]({newrel}{anchor})"
                broken.append(f"{os.path.relpath(path, ROOT)}: unresolved '{url}'")
                return match.group(0)
            broken.append(f"{os.path.relpath(path, ROOT)}: unresolved '{url}' (no note named {base})")
            return match.group(0)

        in_fence, out = False, []
        for line in lines:
            s = line.lstrip()
            if s.startswith("```") or s.startswith("~~~"):
                in_fence = not in_fence
                out.append(line)
                continue
            out.append(line if in_fence else LINK_RE.sub(repl, line))
        new_text = "".join(out)
        if new_text != "".join(lines):
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_text)
    return broken, fixed


def main():
    data = collect()
    problems = validate(data)
    total = write_root_index(data)
    write_section_indexes(data)
    seed_log_if_missing(data, total)
    broken, fixed = check_and_fix_links(build_slug_map())

    print(f"Notes: {total} across {len(SECTIONS)} sections")
    for d, title, _ in SECTIONS:
        print(f"  {title}: {len(data[d])}")
    print(f"Conformance problems: {len(problems)}")
    for p in problems:
        print("  - " + p)
    print(f"Links auto-fixed: {len(fixed)}")
    for x in fixed:
        print("  - " + x)
    print(f"Links still broken: {len(broken)}")
    for b in broken:
        print("  - " + b)
    return 0 if not problems and not broken else 1


if __name__ == "__main__":
    sys.exit(main())
