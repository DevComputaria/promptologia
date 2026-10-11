#!/usr/bin/env python3
"""Gera e valida o índice navegável do grimório sem dependências externas."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GRIMORIO = ROOT / "grimorio"
INDEX = GRIMORIO / "INDEX.md"
VALID_STATUSES = {"draft", "battle-tested", "imported", "superseded"}


@dataclass(frozen=True)
class Entry:
    path: Path
    metadata: dict[str, object]
    title: str


def spell_files() -> list[Path]:
    files: list[Path] = []
    for path in GRIMORIO.rglob("*.md"):
        relative = path.relative_to(GRIMORIO)
        if path.name in {"README.md", "INDEX.md", "CATALOGO.md"}:
            continue
        if "templates" in relative.parts or "examples" in relative.parts:
            continue
        files.append(path)
    return sorted(files, key=lambda item: item.as_posix().casefold())


def scalar(value: str) -> object:
    value = value.strip()
    if value in {"", "null", "~"}:
        return None
    if value == "[]":
        return []
    if value.startswith("[") and value.endswith("]"):
        return [part.strip().strip("\"'") for part in value[1:-1].split(",") if part.strip()]
    return value.strip("\"'")


def frontmatter(text: str) -> dict[str, object]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    try:
        end = next(index for index, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration:
        return {}

    result: dict[str, object] = {}
    active_list: str | None = None
    for line in lines[1:end]:
        key_match = re.match(r"^([a-z_]+):(?:\s*(.*))?$", line)
        if key_match:
            key, value = key_match.groups()
            result[key] = scalar(value or "")
            active_list = key if not value else None
            continue
        item_match = re.match(r"^\s{2}-\s+(.+)$", line)
        if active_list and item_match:
            current = result.get(active_list)
            if not isinstance(current, list):
                current = []
                result[active_list] = current
            current.append(str(scalar(item_match.group(1))))
    return result


def heading(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            clean = re.sub(r"[^\wÀ-ÿ\s:()/.+-]", "", line[2:]).strip()
            return clean.removeprefix("Nome do Feitiço:").strip() or fallback
    return fallback


def entries() -> list[Entry]:
    result: list[Entry] = []
    for path in spell_files():
        text = path.read_text(encoding="utf-8")
        metadata = frontmatter(text)
        title = str(metadata.get("titulo") or heading(text, path.stem))
        result.append(Entry(path, metadata, title))
    return result


def validate(items: list[Entry]) -> list[str]:
    errors: list[str] = []
    ids: dict[str, Path] = {}
    for entry in items:
        relative = entry.path.relative_to(ROOT).as_posix()
        spell_id = entry.metadata.get("id")
        status = entry.metadata.get("status")

        if not spell_id:
            errors.append(f"{relative}: feitiço sem id")
        if not status:
            errors.append(f"{relative}: feitiço sem status")
        if status and status not in VALID_STATUSES:
            errors.append(f"{relative}: status inválido: {status}")
        if spell_id:
            previous = ids.get(str(spell_id))
            if previous:
                errors.append(f"{relative}: id duplicado com {previous.relative_to(ROOT)}: {spell_id}")
            ids[str(spell_id)] = entry.path
    return errors


def markdown(items: list[Entry]) -> str:
    lines = [
        "# Índice do Grimório",
        "",
        "Este arquivo é gerado por `python3 scripts/index-grimorio.py`. Edite o frontmatter dos feitiços, não a tabela.",
        "Todos os feitiços listados têm frontmatter validado; a rubrica de status segue a RFC-002.",
        "",
        "| Feitiço | Caminho | Câmara | Status | Modelos testados |",
        "|---|---|---|---|---|",
    ]
    for entry in items:
        relative = entry.path.relative_to(GRIMORIO)
        href = "./" + relative.as_posix().replace(" ", "%20")
        chamber = str(entry.metadata.get("camara") or relative.parent.as_posix())
        status = str(entry.metadata.get("status") or "rascunho (legado)")
        models = entry.metadata.get("modelos_testados")
        model_text = ", ".join(str(model) for model in models) if isinstance(models, list) and models else "—"
        lines.append(f"| {entry.title} | [`{relative.as_posix()}`]({href}) | `{chamber}` | `{status}` | {model_text} |")
    lines.extend(["", "## Legenda", "", "- `draft`: ainda sem evidência de execução.", "- `battle-tested`: possui saída real registrada em `exemplos/responses/`.", "- `imported`: veio de uma fonte externa identificada.", "- `superseded`: substituído por outro feitiço.", ""])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="valida metadados e confirma que o índice está atualizado")
    args = parser.parse_args()

    items = entries()
    errors = validate(items)
    expected = markdown(items)

    if args.check:
        current = INDEX.read_text(encoding="utf-8") if INDEX.exists() else ""
        if current != expected:
            errors.append("grimorio/INDEX.md está desatualizado; execute python3 scripts/index-grimorio.py")
    else:
        INDEX.write_text(expected, encoding="utf-8")
        print(f"Índice atualizado com {len(items)} feitiços: {INDEX.relative_to(ROOT)}")

    for error in errors:
        print(f"erro: {error}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
