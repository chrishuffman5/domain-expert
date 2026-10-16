#!/usr/bin/env python3
"""Validate the ai-models catalog and its local integration. No network required."""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


def validate(root: Path) -> list[str]:
    errors: list[str] = []

    def check(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    def load(path: Path):
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            errors.append(f"{path.relative_to(root)}: {exc}")
            return None

    catalog = load(root / "catalog.json")
    if not isinstance(catalog, dict):
        return errors or ["catalog.json must contain an object"]
    check(catalog.get("schema_version") == 1, "catalog schema_version must be 1")
    try:
        date.fromisoformat(catalog.get("as_of", ""))
    except (ValueError, TypeError):
        errors.append("catalog as_of must be an ISO date")
    models = catalog.get("models")
    if not isinstance(models, list):
        return errors + ["catalog models must be an array"]
    check(len(models) == 60, f"expected 60 models, found {len(models)}")
    check(bool(catalog.get("selection_policy")), "selection_policy is required")
    required = {"id", "name", "provider", "family", "category", "status", "release", "capabilities", "context", "pricing", "availability", "license", "strengths", "limitations", "adoption", "sources", "retrieved", "reference", "selection_reason", "evidence_class", "identity_kind", "callable_id"}
    ids: list[str] = []
    references: list[str] = []
    families: set[str] = set()
    required_sources: set[str] = set()
    for i, model in enumerate(models):
        if not isinstance(model, dict):
            errors.append(f"model {i}: must be an object")
            continue
        label = str(model.get("id", f"model {i}"))
        check(not (required - model.keys()), f"{label}: missing {sorted(required - model.keys())}")
        for field in ("id", "name", "provider", "family", "status", "retrieved", "reference"):
            check(isinstance(model.get(field), str) and bool(model.get(field)), f"{label}: {field} must be a nonempty string")
        if isinstance(model.get("id"), str):
            ids.append(model["id"])
        family = model.get("family", "")
        if not isinstance(family, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", family):
            errors.append(f"{label}: invalid family slug")
            continue
        families.add(family)
        try:
            retrieved = date.fromisoformat(model.get("retrieved", ""))
            check(retrieved <= date.fromisoformat(catalog["as_of"]), f"{label}: retrieved after catalog as_of")
        except (ValueError, TypeError, KeyError):
            errors.append(f"{label}: invalid retrieved date")
        for field in ("capabilities", "availability", "strengths", "limitations", "sources"):
            check(isinstance(model.get(field), list) and bool(model.get(field)), f"{label}: {field} must be a nonempty array")
        sources = model.get("sources", [])
        if isinstance(sources, list):
            for source in sources:
                if not isinstance(source, str) or urlparse(source).scheme != "https" or not urlparse(source).netloc:
                    errors.append(f"{label}: source must be an HTTPS URL: {source!r}")
                else:
                    required_sources.add(source)
        check(isinstance(model.get("adoption"), dict) and bool(model.get("adoption")), f"{label}: adoption evidence or explicit unknown object is required")
        check(model.get("evidence_class") in ("observed", "proxy", "unknown"), f"{label}: invalid evidence_class")
        for field in ("selection_reason", "identity_kind", "callable_id"):
            check(isinstance(model.get(field), str) and bool(model.get(field)), f"{label}: {field} must be a nonempty string")
        ref = model.get("reference", "")
        if not isinstance(ref, str):
            continue
        references.append(ref)
        path = root / ref
        check(path.resolve().is_relative_to(root.resolve()), f"{label}: reference escapes plugin")
        check(ref.startswith(f"skills/{family}/references/versions/") and ref.endswith(".md"), f"{label}: reference must be in its family's references/versions directory")
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            check(label in text, f"{label}: reference does not mention canonical id")
            check("## Sources" in text and "Fetched:" in text, f"{label}: reference lacks provenance footer")
            if isinstance(sources, list):
                for source in sources:
                    if isinstance(source, str):
                        check(source in text, f"{label}: reference omits catalog source {source}")
        else:
            errors.append(f"{label}: missing reference {ref}")
    for label, values in (("model id", ids), ("reference", references)):
        check(len(set(values)) == len(values), f"duplicate {label}: {[k for k, v in Counter(values).items() if v > 1]}")
    dirs = {p.name for p in (root / "skills").iterdir() if p.is_dir()} if (root / "skills").is_dir() else set()
    check(dirs == families, f"skill families differ from catalog: extra={sorted(dirs-families)}, missing={sorted(families-dirs)}")
    for family in sorted(families):
        skill = root / "skills" / family / "SKILL.md"
        if not skill.is_file():
            errors.append(f"missing skill {family}")
            continue
        text = skill.read_text(encoding="utf-8")
        check(not re.search(r"^(name|description|license):\S", text, re.M), f"{family}: frontmatter fields need a space after ':'")
        check(bool(re.search(rf"^name: {re.escape(family)}$", text, re.M)), f"{family}: frontmatter name mismatch")
        check("Do NOT use" in text, f"{family}: missing overlap exclusion")
        check("## Sources" in text and "Fetched:" in text, f"{family}: missing Sources/Fetched footer")
        check(not list((root / "skills" / family).glob("*/**/SKILL.md")), f"{family}: nested SKILL.md")
    evals = load(root / "evals" / "trigger-evals.json")
    if isinstance(evals, dict):
        check(evals.get("plugin") == "ai-models", "eval plugin must be ai-models")
        cases = evals.get("cases", [])
        check(isinstance(cases, list), "eval cases must be an array")
        if isinstance(cases, list):
            seen = set()
            for case in cases:
                if not isinstance(case, dict):
                    errors.append("eval case must be an object")
                    continue
                case_id = case.get("id")
                check(isinstance(case_id, str) and case_id not in seen, f"duplicate/missing eval id {case_id}")
                seen.add(case_id)
                check(case.get("skill") in families, f"eval targets unknown family {case.get('skill')}")
                check(isinstance(case.get("should_trigger"), bool), f"{case_id}: should_trigger must be boolean")
                check(bool(case.get("prompt")), f"{case_id}: missing prompt")
            for family in families:
                for trigger in (True, False):
                    check(any(c.get("skill") == family and c.get("should_trigger") is trigger for c in cases if isinstance(c, dict)), f"{family}: missing {'positive' if trigger else 'negative'} eval")
    manifest = load(root / ".claude-plugin" / "plugin.json")
    if isinstance(manifest, dict):
        check(manifest.get("name") == "ai-models", "manifest name must be ai-models")
        check(bool(re.fullmatch(r"\d+\.\d+\.\d+", manifest.get("version", ""))), "manifest requires semver version")
    agents = list((root / "agents").glob("*.md"))
    check(len(agents) == 1, "expected one specialist agent")
    if agents:
        text = agents[0].read_text(encoding="utf-8")
        for family in families:
            check(f"skills/{family}/" in text, f"specialist map omits {family}")
    readme = root / "README.md"
    if readme.is_file():
        text = readme.read_text(encoding="utf-8")
        for model_id in ids:
            check(f"`{model_id}`" in text, f"plugin README omits {model_id}")
    else:
        errors.append("missing plugin README.md")
    repo = root.parent.parent
    marketplace_path = repo / ".claude-plugin" / "marketplace.json"
    if marketplace_path.is_file():
        marketplace = json.loads(marketplace_path.read_text(encoding="utf-8"))
        matches = [p for p in marketplace["plugins"] if p.get("name") == "ai-models"]
        check(len(matches) == 1 and matches[0].get("source") == "./plugins/ai-models", "marketplace must register ai-models exactly once with relative source")
        repo_text = (repo / "README.md").read_text(encoding="utf-8")
        counts = {p.name: len(list((p / "skills").glob("*/SKILL.md"))) for p in (repo / "plugins").iterdir() if p.is_dir()}
        rows = {name: int(n) for name, n in re.findall(r"^\| \*\*([^*]+)\*\* \| (\d+) \|", repo_text, re.M)}
        check(rows == counts, "root README plugin counts differ from skill inventory")
        headline = re.search(r"\*\*(\d+) plugins \| (\d+) domains \| (\d+) skills \|.*?\| (\d+) agents\*\*", repo_text)
        check(bool(headline), "missing root README inventory headline")
        if headline:
            check(int(headline[1]) == len(counts), "root README plugin total differs from inventory")
            check(int(headline[2]) == len(counts) - 1, "root README domain total differs from inventory")
            check(int(headline[3]) == sum(counts.values()), "root README skill total differs from inventory")
            check(int(headline[4]) == len(list((repo / "plugins").glob("*/agents/*.md"))), "root README agent total differs from inventory")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plugin", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(args.plugin.resolve())
    for error in errors:
        print(f"FAIL: {error}")
    if errors:
        print(f"{len(errors)} validation failure(s)")
        return 1
    print("PASS: 60 model identities, family references, provenance, trigger evals, specialist map and marketplace/README inventory")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
