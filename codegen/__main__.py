"""CLI entry point: generate Python clients from OpenAPI schemas."""

from __future__ import annotations

import json
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

from codegen.emitter import emit_combined_file, emit_types_file
from codegen.parser import parse_spec

ROOT = Path(__file__).resolve().parent.parent


@dataclass
class ApiConfig:
    schema_path: Path
    output_dir: Path
    client_name: str
    default_base_url: str
    default_rate_limit: int
    search_groups: frozenset[str] = frozenset()
    default_search_rate_limit: int | None = None


APIS = [
    ApiConfig(
        schema_path=ROOT / "schemas" / "forum.json",
        output_dir=ROOT / "src" / "lolzteam" / "generated" / "forum",
        client_name="ForumClient",
        default_base_url="https://prod-api.lolz.live",
        default_rate_limit=300,
    ),
    ApiConfig(
        schema_path=ROOT / "schemas" / "market.json",
        output_dir=ROOT / "src" / "lolzteam" / "generated" / "market",
        client_name="MarketClient",
        default_base_url="https://prod-api.lzt.market",
        default_rate_limit=120,
        search_groups=frozenset({"category"}),
        default_search_rate_limit=20,
    ),
]


def generate_api(config: ApiConfig) -> None:
    print(f"Generating {config.client_name}...")

    try:
        raw_spec = json.loads(config.schema_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        raise RuntimeError(f"Failed to parse schema {config.schema_path}: {exc}") from exc
    result = parse_spec(raw_spec)

    if config.output_dir.exists():
        shutil.rmtree(config.output_dir)
    config.output_dir.mkdir(parents=True, exist_ok=True)

    # Write types.py
    types_content = emit_types_file(result.groups, result.component_schemas)
    (config.output_dir / "types.py").write_text(types_content, encoding="utf-8")
    print("  types.py")

    # Write __init__.py (all group classes + client classes)
    init_content = emit_combined_file(
        result.groups,
        config.client_name,
        config.default_base_url,
        config.default_rate_limit,
        search_groups=config.search_groups,
        default_search_rate_limit=config.default_search_rate_limit,
        component_schema_names=frozenset(result.component_schemas.keys()),
    )
    (config.output_dir / "__init__.py").write_text(init_content, encoding="utf-8")
    print("  __init__.py")

    total_ops = sum(len(g.methods) for g in result.groups)
    print(f"  Done: {len(result.groups)} groups, {total_ops} operations\n")


def _postprocess(dirs: list[Path]) -> None:
    """Run ruff fix + format on generated directories."""
    paths = [str(d) for d in dirs]
    subprocess.run(
        ["uv", "run", "ruff", "check", "--fix", "--quiet", *paths],
        check=False,
    )
    subprocess.run(
        ["uv", "run", "ruff", "format", "--quiet", *paths],
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
