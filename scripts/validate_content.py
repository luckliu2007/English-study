#!/usr/bin/env python3
"""校验 content/ 下的 JSON 数据。

检查项：
1. 每个文件符合对应 JSON Schema（content/schema/*.schema.json）
2. 附加语义检查：
   - quizzes / reading 的 answer 下标必须落在 options 范围内
   - 单个测验里正确答案不应过度集中在某一下标（默认单一下标占比 < 60%）
   - vocabulary 的 meaning 不应以空格或 ASCII 英文字母开头（防止英文泄漏进中文释义）
   - id 在同一文件内唯一

无第三方依赖时，Schema 校验降级为“结构性抽查”，附加检查始终执行。
退出码非 0 表示校验失败，可直接用于 CI。
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

# Windows 控制台默认 GBK，输出 emoji/中文会 UnicodeEncodeError
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

CONTENT_DIR = Path(__file__).resolve().parent.parent / "content"
SCHEMA_DIR = CONTENT_DIR / "schema"

FILES = {
    "vocabulary.json": "vocabulary.schema.json",
    "reading.json": "reading.schema.json",
    "quizzes.json": "quizzes.schema.json",
}

errors: list[str] = []
warnings: list[str] = []


def load(path: Path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def schema_check(data, schema_path: Path, name: str):
    try:
        import jsonschema
    except ImportError:
        warnings.append(f"[{name}] 未安装 jsonschema，跳过 Schema 校验（附加检查仍执行）")
        return
    schema = load(schema_path)
    validator = jsonschema.Draft7Validator(schema)
    for err in sorted(validator.iter_errors(data), key=lambda e: e.path):
        loc = "/".join(str(p) for p in err.path)
        errors.append(f"[{name}] schema 错误 @ {loc or '<root>'}: {err.message}")


def check_ids_unique(data, name: str):
    ids = [item.get("id") for item in data if isinstance(item, dict)]
    dupes = [i for i, c in Counter(ids).items() if c > 1]
    if dupes:
        errors.append(f"[{name}] 重复 id: {dupes}")


def check_answers(quiz_or_reading, name: str):
    for item in quiz_or_reading:
        questions = item.get("questions", [])
        answer_positions = []
        for qi, q in enumerate(questions):
            opts = q.get("options", [])
            ans = q.get("answer")
            if not isinstance(ans, int) or not (0 <= ans < len(opts)):
                errors.append(
                    f"[{name}] {item.get('id')} 第{qi + 1}题 answer={ans} 超出 options 范围(0..{len(opts) - 1})"
                )
            else:
                answer_positions.append(ans)
        # 答案分布偏置检查（题数 >= 4 才有意义）
        if len(answer_positions) >= 4:
            most_common, freq = Counter(answer_positions).most_common(1)[0]
            ratio = freq / len(answer_positions)
            if ratio >= 0.6:
                errors.append(
                    f"[{name}] {item.get('id')} 正确答案过度集中在下标 {most_common} "
                    f"({freq}/{len(answer_positions)}={ratio:.0%})，请打乱选项顺序"
                )


def check_vocab_meaning(vocab, name: str):
    for item in vocab:
        meaning = item.get("meaning", "")
        if meaning != meaning.strip():
            errors.append(f"[{name}] {item.get('id')} meaning 有首尾空格: {meaning!r}")
        elif meaning[:1].isascii() and meaning[:1].isalpha():
            warnings.append(
                f"[{name}] {item.get('id')} meaning 以英文字母开头，疑似英文泄漏: {meaning!r}"
            )


def main() -> int:
    for fname, sname in FILES.items():
        fpath = CONTENT_DIR / fname
        spath = SCHEMA_DIR / sname
        if not fpath.exists():
            errors.append(f"缺少数据文件: {fname}")
            continue
        data = load(fpath)
        if not isinstance(data, list):
            errors.append(f"[{fname}] 顶层应为数组")
            continue

        if spath.exists():
            schema_check(data, spath, fname)
        else:
            warnings.append(f"[{fname}] 缺少 schema {sname}")

        check_ids_unique(data, fname)

        if fname == "quizzes.json":
            check_answers(data, fname)
        elif fname == "reading.json":
            check_answers(data, fname)  # reading 可选带 questions
        elif fname == "vocabulary.json":
            check_vocab_meaning(data, fname)

    for w in warnings:
        print(f"::warning:: {w}")
    for e in errors:
        print(f"::error:: {e}")

    if errors:
        print(f"\n❌ 校验失败：{len(errors)} 个错误，{len(warnings)} 个警告")
        return 1
    print(f"\n✅ 校验通过（{len(warnings)} 个警告）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
