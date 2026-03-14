"""CLI entry point: generate Python clients from OpenAPI schemas."""

from __future__ import annotations

import json
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

from codegen.emitter import emit_group_file, emit_index_file, emit_types_file
from codegen.parser import parse_spec
from codegen.utils.naming import group_to_file_name

ROOT = Path(__file__).resolve().parent.parent


@dataclass
class ApiConfig:
    schema_path: Path
    output_dir: Path
    client_name: str
    default_base_url: str
    default_rate_limit: int


APIS = [
    ApiConfig(
        schema_path=ROOT / "schemas" / "forum.json",
        output_dir=ROOT / "src" / "lolzteam" / "generated" / "forum",
        client_name="ForumClient",
        default_base_url="https://api.lolz.live",
        default_rate_limit=300,
    ),
    ApiConfig(
        schema_path=ROOT / "schemas" / "market.json",
        output_dir=ROOT / "src" / "lolzteam" / "generated" / "market",
        client_name="MarketClient",
        default_base_url="https://api.lzt.market",
        default_rate_limit=120,
    ),
]


def generate_api(config: ApiConfig) -> None:
    print(f"Generating {config.client_name}...")

    raw_spec = json.loads(config.schema_path.read_text(encoding="utf-8"))
    result = parse_spec(raw_spec)

    if config.output_dir.exists():
        shutil.rmtree(config.output_dir)
    config.output_dir.mkdir(parents=True, exist_ok=True)

    # Write types.py
    types_content = emit_types_file(result.groups, result.component_schemas)
    (config.output_dir / "types.py").write_text(types_content, encoding="utf-8")
    print("  types.py")

    # Write group files
    for group in result.groups:
        file_name = group_to_file_name(group.group_name)
        content = emit_group_file(group)
        (config.output_dir / f"{file_name}.py").write_text(content, encoding="utf-8")
        print(f"  {file_name}.py")

    # Write __init__.py
    index_content = emit_index_file(
        result.groups,
        config.client_name,
        config.default_base_url,
        config.default_rate_limit,
    )
    (config.output_dir / "__init__.py").write_text(index_content, encoding="utf-8")
    print("  __init__.py")

    total_ops = sum(len(g.methods) for g in result.groups)
    print(f"  Done: {len(result.groups)} groups, {total_ops} operations\n")


def _postprocess(dirs: list[Path]) -> None:
    """Run ruff fix + format on generated directories."""
    paths = [str(d) for d in dirs]
    subprocess.run(
        ["ruff", "check", "--fix", "--quiet", *paths],
        check=False,
    )
    subprocess.run(
        ["ruff", "format", "--quiet", *paths],
        check=False,
    )


def main() -> None:
    generated_dirs: list[Path] = []
    for api in APIS:
        if not api.schema_path.exists():
            print(f"Schema not found: {api.schema_path}, skipping.")
            continue
        generate_api(api)
        generated_dirs.append(api.output_dir)

    if generated_dirs:
        _postprocess(generated_dirs)


if __name__ == "__main__":
    main()
