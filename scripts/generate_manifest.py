#!/usr/bin/env python3
"""根据 content/*.json 自动生成 content/manifest.json。

manifest 是给 App 端做增量同步/校验的契约：记录每个文件的 SHA256 和条目数。
此前靠手工维护，容易与实际文件不一致；本脚本让它可复现地自动生成。

用法：
  python scripts/generate_manifest.py            # 生成/更新 manifest
  python scripts/generate_manifest.py --check     # 只校验 manifest 是否与实际一致（CI 用），不写文件
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

CONTENT_DIR = Path(__file__).resolve().parent.parent / "content"
MANIFEST = CONTENT_DIR / "manifest.json"
DATA_FILES = ["vocabulary.json", "reading.json", "quizzes.json"]
REPO = "luckliu2007/English-study"
SCHEMA_VERSION = 1


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def count_of(path: Path) -> int:
    data = json.loads(path.read_text(encoding="utf-8"))
    return len(data) if isinstance(data, list) else 0


def build_manifest(preserve_version: str | None = None) -> dict:
    files = {}
    for name in DATA_FILES:
        p = CONTENT_DIR / name
        if not p.exists():
            print(f"::error:: 缺少 {name}", file=sys.stderr)
            sys.exit(2)
        files[name] = {"sha": sha256_of(p), "count": count_of(p)}

    now = datetime.now(timezone.utc)
    version = preserve_version or now.strftime("%Y.%m.%d.1")
    return {
        "schemaVersion": SCHEMA_VERSION,
        "version": version,
        "generatedAt": now.isoformat(timespec="milliseconds").replace("+00:00", "Z"),
        "repo": REPO,
        "branch": "main",
        "files": files,
    }


def files_section(manifest: dict) -> dict:
    return manifest.get("files", {})


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="只校验一致性，不写文件")
    args = ap.parse_args()

    fresh = build_manifest()

    if args.check:
        if not MANIFEST.exists():
            print("::error:: manifest.json 不存在，请先运行不带 --check 的生成命令")
            return 1
        current = json.loads(MANIFEST.read_text(encoding="utf-8"))
        if files_section(current) != files_section(fresh):
            print("::error:: manifest.json 的 files(sha/count) 与实际内容不一致，请运行 "
                  "`python scripts/generate_manifest.py` 重新生成")
            print("  期望:", json.dumps(files_section(fresh), ensure_ascii=False))
            print("  实际:", json.dumps(files_section(current), ensure_ascii=False))
            return 1
        print("✅ manifest 与实际内容一致")
        return 0

    # 生成时保留已有 version（除非文件内容变化需人工 bump），仅刷新 sha/count/generatedAt
    preserve = None
    if MANIFEST.exists():
        try:
            preserve = json.loads(MANIFEST.read_text(encoding="utf-8")).get("version")
        except Exception:
            preserve = None
    out = build_manifest(preserve_version=preserve)
    MANIFEST.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"✅ 已生成 {MANIFEST.relative_to(CONTENT_DIR.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
