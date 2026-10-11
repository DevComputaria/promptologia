#!/usr/bin/env python3
"""Contrato do grimório.

Sem dependência externa. Falha com código 1 se o frontmatter, o catálogo
ou um nome de arquivo quebrarem a regra descrita em PLANO-DE-MUDANCAS.md.

    python3 ferramentas/cli/check_grimorio.py
    python3 ferramentas/cli/check_grimorio.py --write-catalog
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / "grimorio" / "CATALOGO.md"

REQUIRED_KEYS = (
    "id",
    "titulo",
    "camara",
    "categoria",
    "objetivo",
    "entrada",
    "saida",
    "placeholders",
    "modelos_testados",
    "versao",
    "status",
    "risco",
    "proveniencia",
    "fonte",
    "substitui",
)
STATUS = {"draft", "battle-tested", "imported", "superseded"}
RISCO = {"nenhum", "dados-sensiveis", "uso-dual"}
PROVENIENCIA = {"original", "importado"}
FONTE_DESCONHECIDA = "nao-identificada"
KEY_ORDER = REQUIRED_KEYS


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1].replace('\\"', '"')
    return value


def split_flow_list(inner: str) -> list[str]:
    items: list[str] = []
    buf: list[str] = []
    quote: str | None = None
    for ch in inner:
        if quote:
            buf.append(ch)
            if ch == quote:
                quote = None
            continue
        if ch in {'"', "'"}:
            quote = ch
            buf.append(ch)
            continue
        if ch == ",":
            items.append(unquote("".join(buf)))
            buf = []
            continue
        buf.append(ch)
    tail = unquote("".join(buf))
    if tail:
        items.append(tail)
    return items


def parse_scalar(raw: str):
    raw = raw.strip()
    if raw == "[]":
        return []
    if raw.startswith("[") and raw.endswith("]"):
        return split_flow_list(raw[1:-1].strip())
    return unquote(raw)


def parse_frontmatter(text: str) -> tuple[dict | None, str]:
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end < 0:
        return None, text
    block = text[4:end]
    body = text[end + 4 :]
    if body.startswith("\n"):
        body = body[1:]
    data: dict = {}
    for line in block.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"linha sem chave: {line}")
        key, raw = line.split(":", 1)
        data[key.strip()] = parse_scalar(raw)
    return data, body


def spell_files() -> list[Path]:
    found: list[Path] = []
    roots = [ROOT / "grimorio", ROOT / "ferramentas" / "integracoes" / "perplexity"]
    for base in roots:
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            rel = path.relative_to(ROOT).as_posix()
            if path.name in {"README.md", "INDEX.md"}:
                continue
            if rel == "grimorio/CATALOGO.md":
                continue
            if "/examples/" in rel:
                continue
            found.append(path)
    return found


def placeholder_names(body: str) -> list[str]:
    return sorted(set(re.findall(r"\{\{([^{}]+)\}\}", body)))


def declared_names(value) -> list[str]:
    if not isinstance(value, list):
        return []
    names = []
    for item in value:
        item = str(item).strip()
        match = re.fullmatch(r"\{\{([^{}]+)\}\}", item)
        names.append(match.group(1) if match else item)
    return sorted(names)


def check_names() -> list[str]:
    errors = []
    for dirpath, dirnames, filenames in os_walk_safe(ROOT):
        rel_dir = Path(dirpath).relative_to(ROOT)
        if ".git" in rel_dir.parts:
            continue
        for name in dirnames + filenames:
            if name != name.strip():
                errors.append(f"nome com espaço na ponta: {(rel_dir / name).as_posix()}")
    return errors


def os_walk_safe(root: Path):
    import os

    return os.walk(root)


def render_catalog(rows: list[tuple[str, dict, str]]) -> str:
    lines = [
        "# Catálogo",
        "",
        "Gerado por `python3 ferramentas/cli/check_grimorio.py --write-catalog`. Não edite à mão.",
        "Feitiço `battle-tested` ainda não existe: ninguém gravou saída real em `exemplos/responses/`.",
        "",
        "| id | status | risco | proveniência | arquivo |",
        "|---|---|---|---|---|",
    ]
    for _id, data, rel in sorted(rows, key=lambda item: item[0]):
        fonte = data.get("fonte") or ""
        prov = data["proveniencia"]
        if prov == "importado" and fonte == FONTE_DESCONHECIDA:
            prov = "importado, fonte pendente"
        lines.append(
            f"| `{_id}` | {data['status']} | {data['risco']} | {prov} | [{rel}]({rel_link(rel)}) |"
        )
    lines.append("")
    return "\n".join(lines)


def rel_link(rel: str) -> str:
    # Catálogo mora em grimorio/. Links relativos a essa pasta.
    if rel.startswith("grimorio/"):
        return rel[len("grimorio/") :]
    return "../" + rel


def check(rows_out: list | None = None) -> list[str]:
    errors = check_names()
    seen: dict[str, str] = {}
    rows: list[tuple[str, dict, str]] = []
    for path in spell_files():
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        try:
            data, body = parse_frontmatter(text)
        except ValueError as exc:
            errors.append(f"{rel}: {exc}")
            continue
        if data is None:
            errors.append(f"{rel}: sem frontmatter")
            continue
        missing = [key for key in REQUIRED_KEYS if key not in data]
        if missing:
            errors.append(f"{rel}: faltam chaves {missing}")
            continue
        spell_id = str(data["id"])
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", spell_id):
            errors.append(f"{rel}: id inválido `{spell_id}`")
        if spell_id in seen:
            errors.append(f"{rel}: id `{spell_id}` repetido em {seen[spell_id]}")
        seen[spell_id] = rel
        if data["status"] not in STATUS:
            errors.append(f"{rel}: status inválido")
        if data["risco"] not in RISCO:
            errors.append(f"{rel}: risco inválido")
        if data["proveniencia"] not in PROVENIENCIA:
            errors.append(f"{rel}: proveniencia inválida")
        imported = data["proveniencia"] == "importado"
        if imported != (data["status"] == "imported"):
            errors.append(f"{rel}: status imported e proveniencia importado têm de andar juntos")
        fonte = str(data["fonte"])
        if imported and not (fonte.startswith("http://") or fonte.startswith("https://") or fonte == FONTE_DESCONHECIDA):
            errors.append(f"{rel}: importado precisa de fonte http ou `{FONTE_DESCONHECIDA}`")
        if data["status"] == "battle-tested":
            response = ROOT / "exemplos" / "responses" / f"{spell_id}.md"
            if not response.is_file() or response.stat().st_size == 0:
                errors.append(f"{rel}: battle-tested sem exemplos/responses/{spell_id}.md")
        declared = declared_names(data["placeholders"])
        used = placeholder_names(body)
        if declared != used:
            errors.append(
                f"{rel}: placeholders divergem. declarados={declared} usados={used}"
            )
        rows.append((spell_id, data, rel))
    if rows_out is not None:
        rows_out.extend(rows)
    expected = render_catalog(rows)
    actual = CATALOG.read_text(encoding="utf-8") if CATALOG.exists() else ""
    if actual != expected:
        errors.append("grimorio/CATALOGO.md está desatualizado. Rode com --write-catalog.")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-catalog", action="store_true")
    args = parser.parse_args()
    rows: list = []
    # Gera o catálogo a partir dos arquivos mesmo se outras regras falharem,
    # mas só grava se a leitura do frontmatter tiver produzido linhas.
    errors = check(rows)
    if args.write_catalog:
        CATALOG.write_text(render_catalog(rows), encoding="utf-8")
        errors = [err for err in check() if not err.startswith("grimorio/CATALOGO.md")]
    if errors:
        for err in errors:
            print(err, file=sys.stderr)
        print(f"{len(errors)} erro(s)", file=sys.stderr)
        return 1
    print(f"ok: {len(spell_files())} feitiços")
    return 0


if __name__ == "__main__":
    sys.exit(main())
