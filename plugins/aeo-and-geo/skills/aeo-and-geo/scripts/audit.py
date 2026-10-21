#!/usr/bin/env python3
"""Answer-engine extractability audit.

Usage:
    python audit.py <url-or-local-html-path>

Scores a page 0-7 on whether an LLM can lift an answer from it whole.
Stdlib only, no install step.

Checks 5 and 7 are HEURISTIC and say so in the output. They flag for human
review. Other checks are mechanical signals, not ranking predictions;
FAQ answer parity and markup edge cases still require human review.
"""

import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

UA = "Mozilla/5.0 (compatible; aeo-audit/1.0)"
# A digit that reads as a price, quantity, or timeframe. Bare years excluded.
NUM = re.compile(r"\$\s?\d|(?<!\w)\d+\s?(?:%|/mo|/month|hr|hours?|days?|min)", re.I)
PRICE = re.compile(r"\$\s?[\d,]+(?:\.\d{2})?")
INCLUSION = re.compile(
    r"\b(includ\w+|covered|comes with|plus\b|on top of|additional|you (?:also )?pay|"
    r"no (?:extra|hidden|additional|monthly|setup)|nothing else)\b",
    re.I,
)


def fetch(target: str) -> str:
    p = Path(target)
    if p.exists():
        return p.read_text(encoding="utf-8", errors="replace")
    if not target.startswith(("http://", "https://")):
        sys.exit(f"FAIL: not a URL and not a file on disk: {target}")
    req = urllib.request.Request(target, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        sys.exit(f"FAIL: HTTP {e.code} fetching {target}")
    except Exception as e:  # noqa: BLE001 - surface the real reason, do not mask it
        sys.exit(f"FAIL: could not fetch {target}: {e}")


def strip_tags(html: str) -> str:
    html = re.sub(r"<(script|style)\b.*?</\1>", " ", html, flags=re.S | re.I)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html))


def first(pattern: str, html: str) -> str:
    m = re.search(pattern, html, re.I | re.S)
    return (m.group(1).strip() if m else "")


def headings(html: str):
    return [
        re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", h)).strip()
        for h in re.findall(r"<h[1-4][^>]*>(.*?)</h[1-4]>", html, re.I | re.S)
    ]


def summaries(html: str):
    return [
        re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()
        for s in re.findall(r"<summary[^>]*>(.*?)</summary>", html, re.I | re.S)
    ]


def faq_ld(html: str):
    """Return (found, parsed_ok, n_questions, error)."""
    blocks = re.findall(
        r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', html, re.S | re.I
    )
    if not blocks:
        return False, False, 0, "no ld+json block"
    total, parsed_any, err = 0, False, ""
    for b in blocks:
        try:
            data = json.loads(b)
        except json.JSONDecodeError as e:
            err = f"JSON parse error: {e}"
            continue
        parsed_any = True
        nodes = data.get("@graph", [data]) if isinstance(data, dict) else data
        for node in nodes if isinstance(nodes, list) else [nodes]:
            if isinstance(node, dict) and node.get("@type") == "FAQPage":
                total += len(node.get("mainEntity", []))
    return True, parsed_any, total, err


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    target = sys.argv[1]
    html = fetch(target)
    text = strip_tags(html)

    title = first(r"<title[^>]*>(.*?)</title>", html)
    desc = first(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']', html)
    hs = headings(html) + summaries(html)
    questions = [h for h in hs if h.rstrip().endswith("?")]
    prices = sorted(set(PRICE.findall(text)))
    ld_found, ld_ok, ld_n, ld_err = faq_ld(html)

    results = []
    results.append(("1. Number in <title>", bool(NUM.search(title)),
                    title or "(no title)", False))
    results.append(("2. Number in meta description", bool(NUM.search(desc)),
                    (desc[:90] + "...") if len(desc) > 90 else (desc or "(none)"), False))
    results.append(("3. Money question answered", len(prices) > 0,
                    f"{len(prices)} distinct price tokens: {', '.join(prices[:8])}"
                    or "no prices found", False))
    results.append(("4. Question shaped headings (>=3)", len(questions) >= 3,
                    f"{len(questions)} found" + (f": {questions[0][:60]}..." if questions else ""),
                    False))

    # HEURISTIC: answers are checked for length only; a human must judge self-containment.
    results.append(("5. Standalone answers", len(questions) >= 3,
                    "HEURISTIC - count only. Read each answer: does it stand alone "
                    "with no pronoun pointing at an earlier section?", True))

    results.append(("6. FAQPage JSON-LD", ld_found and ld_ok and ld_n > 0,
                    f"found={ld_found} parses={ld_ok} questions={ld_n}"
                    + (f" ERR: {ld_err}" if ld_err else ""), False))

    # HEURISTIC: inclusion language near prices suggests all-in pricing.
    incl = bool(INCLUSION.search(text)) and bool(prices)
    results.append(("7. All in pricing", incl,
                    "HEURISTIC - inclusion language "
                    + ("present" if INCLUSION.search(text) else "ABSENT")
                    + " near pricing. Confirm every price says what is included.", True))

    print(f"\nAEO EXTRACTABILITY AUDIT\n{target}\n" + "=" * 66)
    score = 0
    for name, ok, detail, heuristic in results:
        if ok:
            score += 1
        flag = "PASS" if ok else "FAIL"
        tag = " [heuristic]" if heuristic else ""
        print(f"[{flag}] {name}{tag}\n       {detail}")

    print("=" * 66)
    print(f"SCORE: {score}/7")
    if score < 5:
        print("VERDICT: limited extractability signals. Investigate the FAILs; citations are not predicted.")
    elif score < 7:
        print("VERDICT: some extractability signals present. Investigate the FAILs and manual checks.")
    else:
        print("VERDICT: structural checks passed. Now run the extraction and schema-parity tests by hand.")
    print(
        "\nEXTRACTION TEST (not automatable, do it yourself):\n"
        "  Can you answer the target question by copying ONE sentence from this\n"
        "  page, with no synthesis and no stitching? If no, the page fails\n"
        "  regardless of the score above.\n"
    )


if __name__ == "__main__":
    main()
