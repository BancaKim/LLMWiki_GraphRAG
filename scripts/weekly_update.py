#!/usr/bin/env python3
"""Weekly GraphRAG paper sweep -> new OKF notes in this wiki.

Pipeline:
  1. Query the arXiv API for recent GraphRAG-related papers (last LOOKBACK_DAYS).
  2. Drop anything already in the wiki (by arXiv id or near-duplicate title).
  3. Ask the model whether each candidate genuinely belongs here, and in which
     section (methods / surveys / techniques / concepts / tools / benchmarks).
  4. For accepted papers, author a Korean OKF note. Frontmatter citation fields
     (authors / year / arxiv / resource) are filled DETERMINISTICALLY from the
     arXiv metadata, so they cannot be hallucinated; the model only writes the
     description, tags, body and related-links.
  5. Rebuild indexes (scripts/build_wiki.py), prepend a log.md entry, and — on
     CI (WEEKLY_PUSH=1) — commit and push.

Env:
  ANTHROPIC_API_KEY   required unless DRY_RUN=1
  ANTHROPIC_MODEL     default 'claude-sonnet-4-6'
  LOOKBACK_DAYS       default 8
  MAX_NEW             default 6   (cap notes added per run)
  DRY_RUN             '1'/'true' -> only fetch + dedup + print candidates
  WEEKLY_PUSH         '1' -> git add/commit/push after writing
  WIKI_ROOT           override repo root (default: parent of scripts/)
"""
import os
import re
import sys
import json
import time
import glob
import subprocess
import datetime
import unicodedata
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.environ.get("WIKI_ROOT") or os.path.dirname(HERE)

MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-6")
LOOKBACK_DAYS = int(os.environ.get("LOOKBACK_DAYS", "8"))
MAX_NEW = int(os.environ.get("MAX_NEW", "6"))
DRY_RUN = os.environ.get("DRY_RUN", "").lower() in ("1", "true", "yes")
DO_PUSH = os.environ.get("WEEKLY_PUSH", "") == "1"
TODAY = datetime.date.today().isoformat()

SECTION_DIRS = ["concepts", "methods", "techniques", "surveys", "tools", "benchmarks"]
VALID_TYPES = {"Concept", "Method", "Technique", "Survey", "Tool", "Benchmark"}

ARXIV_API = "http://export.arxiv.org/api/query"
ARXIV_QUERIES = [
    'all:"GraphRAG" OR abs:"graph retrieval-augmented generation" OR abs:"graph-based retrieval-augmented generation"',
    'abs:"knowledge graph" AND abs:"retrieval-augmented generation"',
    'abs:"knowledge graph" AND abs:"large language model" AND abs:"retrieval"',
]
ATOM = "{http://www.w3.org/2005/Atom}"
ARX = "{http://arxiv.org/schemas/atom}"


# --------------------------------------------------------------------------- #
# arXiv fetch
# --------------------------------------------------------------------------- #
def _http_get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "llmwiki-graphrag-bot/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def fetch_arxiv():
    cutoff = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=LOOKBACK_DAYS)
    seen, papers = set(), []
    for q in ARXIV_QUERIES:
        params = urllib.parse.urlencode({
            "search_query": q,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
            "max_results": "60",
        })
        try:
            raw = _http_get(f"{ARXIV_API}?{params}")
        except Exception as e:  # network/proxy hiccup — skip this query
            print(f"[warn] arXiv query failed ({e}); skipping", file=sys.stderr)
            continue
        for entry in ET.fromstring(raw).findall(f"{ATOM}entry"):
            aid_url = (entry.findtext(f"{ATOM}id") or "").strip()
            m = re.search(r"abs/([0-9]+\.[0-9]+)", aid_url)
            if not m:
                continue
            aid = m.group(1)
            published = (entry.findtext(f"{ATOM}published") or "")[:10]
            try:
                pub_dt = datetime.datetime.fromisoformat(
                    (entry.findtext(f"{ATOM}published") or "").replace("Z", "+00:00"))
            except ValueError:
                continue
            if pub_dt < cutoff or aid in seen:
                continue
            seen.add(aid)
            authors = [a.findtext(f"{ATOM}name").strip()
                       for a in entry.findall(f"{ATOM}author") if a.findtext(f"{ATOM}name")]
            cat_el = entry.find(f"{ARX}primary_category")
            papers.append({
                "id": aid,
                "title": " ".join((entry.findtext(f"{ATOM}title") or "").split()),
                "abstract": " ".join((entry.findtext(f"{ATOM}summary") or "").split()),
                "authors": authors,
                "year": int(published[:4]) if published[:4].isdigit() else datetime.date.today().year,
                "published": published,
                "category": cat_el.get("term") if cat_el is not None else "",
                "abs_url": f"https://arxiv.org/abs/{aid}",
            })
        time.sleep(3)  # be polite to the arXiv API
    papers.sort(key=lambda p: p["published"], reverse=True)
    return papers


# --------------------------------------------------------------------------- #
# existing wiki state
# --------------------------------------------------------------------------- #
def _norm_title(t):
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


def existing_state():
    catalog, arxiv_ids, titles = {}, set(), set()
    for d in SECTION_DIRS:
        for path in glob.glob(os.path.join(ROOT, d, "*.md")):
            base = os.path.basename(path)
            if base in ("index.md", "log.md"):
                continue
            with open(path, encoding="utf-8") as f:
                text = f.read()
            mm = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
            fm = {}
            if mm:
                try:
                    fm = yaml.safe_load(mm.group(1)) or {}
                except yaml.YAMLError:
                    fm = {}
            slug = base[:-3]
            catalog[slug] = {"slug": slug, "dir": d,
                             "title": fm.get("title") or slug,
                             "type": fm.get("type") or ""}
            if fm.get("arxiv"):
                arxiv_ids.add(str(fm["arxiv"]).strip())
            for hit in re.findall(r"arxiv\.org/abs/([0-9]+\.[0-9]+)", text):
                arxiv_ids.add(hit)
            if fm.get("title"):
                titles.add(_norm_title(fm["title"]))
    return catalog, arxiv_ids, titles


def slugify(title, used):
    t = unicodedata.normalize("NFKD", title)
    t = t.split(":")[0] if 0 < len(t.split(":")[0]) <= 40 else t
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t.lower()).strip("-")
    t = "-".join(t.split("-")[:7]) or "paper"
    slug, n = t, 2
    while slug in used:
        slug = f"{t}-{n}"
        n += 1
    used.add(slug)
    return slug


# --------------------------------------------------------------------------- #
# model calls
# --------------------------------------------------------------------------- #
def _client():
    from anthropic import Anthropic
    return Anthropic()


def _ask_json(client, prompt, max_tokens=1500):
    msg = client.messages.create(
        model=MODEL, max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    )
    text = "".join(b.text for b in msg.content if getattr(b, "type", "") == "text").strip()
    m = re.search(r"\{.*\}", text, re.DOTALL)
    return json.loads(m.group(0) if m else text)


def triage(client, p):
    prompt = f"""You curate a wiki about GraphRAG (graph-based / knowledge-graph retrieval-augmented generation, KG-augmented LLM reasoning and QA). Decide whether this arXiv paper genuinely belongs.

Title: {p['title']}
Categories: {p['category']}
Abstract: {p['abstract'][:1500]}

Return ONLY JSON:
{{"relevant": true/false,
  "section": one of "methods","surveys","techniques","concepts","tools","benchmarks",
  "type": one of "Method","Survey","Technique","Concept","Tool","Benchmark",
  "reason": "<=20 words"}}

Be strict: relevant only if graphs or knowledge graphs are central to the retrieval/reasoning method. A generic RAG, plain LLM, or unrelated graph-ML paper is NOT relevant."""
    try:
        d = _ask_json(client, prompt, max_tokens=400)
    except Exception as e:
        print(f"[warn] triage failed for {p['id']}: {e}", file=sys.stderr)
        return None
    if not d.get("relevant"):
        return None
    if d.get("section") not in SECTION_DIRS or d.get("type") not in VALID_TYPES:
        d["section"], d["type"] = "methods", "Method"
    return d


def author(client, p, section, typ, catalog):
    cat_lines = "\n".join(f"- {c['slug']}  [{c['dir']}/, {c['type']}]  \"{c['title']}\""
                          for c in catalog.values())
    prompt = f"""당신은 GraphRAG 한국어 지식 위키에 새 노트를 작성하는 전문 연구자입니다. 아래 arXiv 논문에 대한 OKF 노트의 '본문'을 작성하세요. (프런트매터의 서지정보는 코드가 자동으로 채우므로 작성하지 않습니다.)

논문 제목: {p['title']}
저자: {', '.join(p['authors'][:12])}
연도: {p['year']}  · arXiv:{p['id']}  · 분류: {p['category']}
초록: {p['abstract'][:2500]}

이 노트는 `{section}/` 디렉터리에 들어가며 OKF type 은 `{typ}` 입니다.

다음 JSON 만 반환하세요(설명/코드펜스 없이):
{{
  "description": "<한 문장의 한국어 요약>",
  "tags": ["<소문자-하이픈 태그 3~6개, 예: graphrag, retrieval, knowledge-graph>"],
  "body": "<마크다운 본문. '# 제목'으로 시작한 뒤 2~4문장 리드, 이어서 ## 섹션들(예: 개요 / 핵심 아이디어 / 기여 / 강점과 한계). 한국어. 약 160~360단어. '## 관련 항목'과 '## 참고문헌'은 넣지 마세요 — 코드가 추가합니다.>",
  "related": ["<아래 카탈로그의 slug 중 4~7개>"]
}}

본문 안에서 다른 노트로 링크할 때 규칙(그래프 연결용):
- 모든 노트는 정확히 한 단계 깊이입니다. 같은 디렉터리({section}) 슬러그 S 는 [제목](S.md), 다른 디렉터리 D 는 [제목](../D/S.md).
- 카탈로그에 있는 slug 에만 링크하세요.

카탈로그(slug — [dir, type] — 제목):
{cat_lines}"""
    return _ask_json(client, prompt, max_tokens=2200)


# --------------------------------------------------------------------------- #
# note assembly
# --------------------------------------------------------------------------- #
def _scalar(x):
    """Render a YAML scalar, quoting whenever a bare value would be unsafe or
    would round-trip to a non-string (e.g. the arXiv id '2410.05779' -> float)."""
    if isinstance(x, bool):
        return "true" if x else "false"
    if isinstance(x, (int, float)):
        return str(x)
    s = str(x)
    needs = (s == "" or s[0] in "!&*?|>%@`\"'#,[]{} " or ": " in s
             or s.endswith(":") or " #" in s)
    if not needs:
        try:
            needs = not isinstance(yaml.safe_load(s), str)
        except yaml.YAMLError:
            needs = True
    if needs:
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s


def _frontmatter(d):
    out = ["---"]
    for k, v in d.items():
        if isinstance(v, list):
            out.append(f"{k}: [{', '.join(_scalar(x) for x in v)}]")
        else:
            out.append(f"{k}: {_scalar(v)}")
    out.append("---")
    return "\n".join(out)


def _rel(from_dir, slug, catalog):
    e = catalog[slug]
    path = f"{slug}.md" if e["dir"] == from_dir else f"../{e['dir']}/{slug}.md"
    return f"[{e['title']}]({path})"


def assemble(p, section, typ, slug, authored, catalog):
    tags = []
    for t in (authored.get("tags") or [])[:6]:
        t = re.sub(r"[^a-z0-9-]+", "-", t.lower()).strip("-")
        if t:
            tags.append(t)
    if "graphrag" not in tags:
        tags.insert(0, "graphrag")
    fm = {
        "type": typ,
        "title": p["title"],
        "description": authored.get("description", "").strip() or p["title"],
        "tags": tags,
        "authors": p["authors"][:15],
        "year": p["year"],
        "venue": "arXiv preprint",
        "arxiv": str(p["id"]),
        "resource": p["abs_url"],
        "timestamp": TODAY,
    }
    body = (authored.get("body") or "").strip()
    if not body.startswith("#"):
        body = f"# {p['title']}\n\n" + body

    related = [s for s in (authored.get("related") or []) if s in catalog and s != slug]
    rel_block = ""
    if related:
        rel_block = "\n\n## 관련 항목\n\n" + "\n".join(f"- {_rel(section, s, catalog)}" for s in related)

    auth = ", ".join(p["authors"][:6]) + (" et al." if len(p["authors"]) > 6 else "")
    refs = (f"\n\n## 참고문헌\n\n- {auth} ({p['year']}). *{p['title']}*. "
            f"arXiv preprint. arXiv:{p['id']} — {p['abs_url']}\n")
    return _frontmatter(fm) + "\n\n" + body + rel_block + refs


def prepend_log(added):
    p = os.path.join(ROOT, "log.md")
    text = open(p, encoding="utf-8").read() if os.path.exists(p) else "# 변경 이력 (Changelog)\n"
    entry = (f"## {TODAY} — 주간 자동 업데이트\n\n새 논문 노트 {len(added)}건 추가:\n\n"
             + "\n".join(f"- `{a['dir']}/{a['slug']}.md` — {a['title']} (arXiv:{a['id']})" for a in added)
             + "\n")
    idx = text.find("\n## ")
    new = (text[:idx + 1] + entry + "\n" + text[idx + 1:]) if idx != -1 else text.rstrip() + "\n\n" + entry
    with open(p, "w", encoding="utf-8") as f:
        f.write(new)


# --------------------------------------------------------------------------- #
# git
# --------------------------------------------------------------------------- #
def _git(*args):
    return subprocess.run(["git", "-C", ROOT, *args], check=True, capture_output=True, text=True)


def commit_and_push(added):
    if not _git("config", "user.email").stdout.strip():
        _git("config", "user.email", "actions@users.noreply.github.com")
        _git("config", "user.name", "graphrag-update-bot")
    _git("add", "-A")
    if not _git("status", "--porcelain").stdout.strip():
        print("Nothing to commit.")
        return
    body = "\n".join(f"- {a['dir']}/{a['slug']}.md — {a['title']} (arXiv:{a['id']})" for a in added)
    msg = f"chore: weekly GraphRAG update ({TODAY}) — +{len(added)} paper(s)\n\n{body}"
    _git("commit", "-m", msg)
    for attempt in range(4):
        try:
            _git("push", "origin", "HEAD")
            print("Pushed.")
            return
        except subprocess.CalledProcessError as e:
            if attempt == 3:
                raise
            print(f"[warn] push failed, retrying: {e.stderr}", file=sys.stderr)
            time.sleep(2 ** (attempt + 1))


# --------------------------------------------------------------------------- #
def main():
    papers = fetch_arxiv()
    catalog, arxiv_ids, titles = existing_state()
    candidates = [p for p in papers
                  if p["id"] not in arxiv_ids and _norm_title(p["title"]) not in titles]
    print(f"Fetched {len(papers)} recent papers; {len(candidates)} new after dedup "
          f"(lookback {LOOKBACK_DAYS}d).")

    if DRY_RUN:
        for p in candidates[:25]:
            print(f"  - {p['published']}  arXiv:{p['id']}  {p['title']}")
        return 0

    if not candidates:
        print("No new papers this week.")
        return 0

    client = _client()
    used_slugs = set(catalog.keys())
    added = []
    for p in candidates:
        if len(added) >= MAX_NEW:
            print(f"[info] reached MAX_NEW={MAX_NEW}; {len(candidates) - MAX_NEW} candidate(s) deferred.")
            break
        decision = triage(client, p)
        if not decision:
            continue
        section, typ = decision["section"], decision["type"]
        try:
            authored = author(client, p, section, typ, catalog)
        except Exception as e:
            print(f"[warn] author failed for {p['id']}: {e}", file=sys.stderr)
            continue
        slug = slugify(p["title"], used_slugs)
        content = assemble(p, section, typ, slug, authored, catalog)
        dest = os.path.join(ROOT, section, f"{slug}.md")
        with open(dest, "w", encoding="utf-8") as f:
            f.write(content)
        catalog[slug] = {"slug": slug, "dir": section, "title": p["title"], "type": typ}
        added.append({"slug": slug, "dir": section, "title": p["title"], "id": p["id"]})
        print(f"  + {section}/{slug}.md  ({decision.get('reason', '')})")

    if not added:
        print("No relevant new papers after triage.")
        return 0

    prepend_log(added)
    subprocess.run([sys.executable, os.path.join(HERE, "build_wiki.py")],
                   check=False, env={**os.environ, "WIKI_ROOT": ROOT})
    if DO_PUSH:
        commit_and_push(added)
    else:
        print(f"Wrote {len(added)} note(s). (WEEKLY_PUSH not set — skipping git.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
