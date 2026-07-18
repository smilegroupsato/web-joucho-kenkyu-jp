#!/usr/bin/env python3
"""Build the SGOS Site Tree JSON consumed by SGOS Console."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urljoin


class MetadataParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._in_title = False
        self._in_h1 = False
        self._title_parts: list[str] = []
        self._h1_parts: list[str] = []
        self._h1_complete = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        lowered = tag.lower()
        if lowered == "title":
            self._in_title = True
        elif lowered == "h1" and not self._h1_complete:
            self._in_h1 = True

    def handle_endtag(self, tag: str) -> None:
        lowered = tag.lower()
        if lowered == "title":
            self._in_title = False
        elif lowered == "h1" and self._in_h1:
            self._in_h1 = False
            self._h1_complete = True

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self._title_parts.append(data)
        if self._in_h1:
            self._h1_parts.append(data)

    def values(self) -> tuple[str, str | None]:
        title = " ".join("".join(self._title_parts).split())
        heading = " ".join("".join(self._h1_parts).split()) or None
        return title, heading


def read_title(path: Path) -> str:
    parser = MetadataParser()
    parser.feed(path.read_text(encoding="utf-8"))
    title, heading = parser.values()
    if heading:
        return heading
    if not title:
        raise ValueError(f"No <title> or <h1> found: {path}")
    for delimiter in ("｜", "|"):
        if delimiter in title:
            return title.split(delimiter, 1)[0].strip()
    return title


def page_url(relative_path: Path, site_url: str) -> str:
    posix = relative_path.as_posix()
    if posix == "index.html":
        return site_url
    if relative_path.name == "index.html":
        return urljoin(site_url, relative_path.parent.as_posix().rstrip("/") + "/")
    return urljoin(site_url, posix)


def source_revision() -> str:
    from_env = os.getenv("GITHUB_SHA") or os.getenv("SGOS_SOURCE_REVISION")
    if from_env:
        return from_env
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def load_config(path: Path) -> dict[str, Any]:
    config = json.loads(path.read_text(encoding="utf-8"))
    required = ("schema_version", "site_id", "site_title", "site_url", "source_dir")
    missing = [key for key in required if not config.get(key)]
    if missing:
        raise ValueError(f"Missing required config keys: {', '.join(missing)}")
    if not str(config["site_url"]).endswith("/"):
        raise ValueError("site_url must end with '/'")
    return config


def is_excluded(relative_path: Path, excluded: set[str]) -> bool:
    relative_posix = relative_path.as_posix()
    return relative_posix in excluded or any(
        relative_posix.startswith(item.rstrip("/") + "/") for item in excluded
    )


def page_node(html_path: Path, source_dir: Path, site_url: str) -> dict[str, Any]:
    relative = html_path.relative_to(source_dir)
    return {
        "kind": "page",
        "title": read_title(html_path),
        "url": page_url(relative, site_url),
        "path": relative.as_posix(),
        "children": [],
    }


def directory_node(
    directory: Path,
    source_dir: Path,
    site_url: str,
    excluded: set[str],
    *,
    kind: str,
    title_override: str | None = None,
) -> dict[str, Any] | None:
    relative_dir = directory.relative_to(source_dir)
    index_path = directory / "index.html"
    usable_index = index_path.is_file() and not is_excluded(
        index_path.relative_to(source_dir), excluded
    )

    direct_pages = [
        page_node(path, source_dir, site_url)
        for path in sorted(directory.glob("*.html"))
        if path.name != "index.html"
        and not is_excluded(path.relative_to(source_dir), excluded)
    ]

    nested_nodes: list[dict[str, Any]] = []
    for child_dir in sorted(path for path in directory.iterdir() if path.is_dir()):
        if is_excluded(child_dir.relative_to(source_dir), excluded):
            continue
        child_node = directory_node(
            child_dir,
            source_dir,
            site_url,
            excluded,
            kind="group",
        )
        if child_node is not None:
            nested_nodes.append(child_node)

    if not usable_index and not direct_pages and not nested_nodes and title_override is None:
        return None

    title = (
        title_override
        or (read_title(index_path) if usable_index else relative_dir.name)
    )
    url = page_url(index_path.relative_to(source_dir), site_url) if usable_index else None
    return {
        "kind": kind,
        "slug": relative_dir.name,
        "title": title,
        "url": url,
        "available": bool(usable_index or direct_pages or nested_nodes),
        "children": direct_pages + nested_nodes,
    }


def build_tree(config: dict[str, Any], repository_root: Path) -> dict[str, Any]:
    source_dir = repository_root / str(config["source_dir"])
    if not source_dir.is_dir():
        raise FileNotFoundError(f"Source directory not found: {source_dir}")

    excluded = {
        Path(item).as_posix().lstrip("/")
        for item in config.get("exclude_paths", [])
    }
    section_config = config.get("sections", [])
    configured_slugs = [str(item["slug"]) for item in section_config]
    section_by_slug = {str(item["slug"]): item for item in section_config}
    site_url = str(config["site_url"])

    tree: list[dict[str, Any]] = []

    root_index = source_dir / "index.html"
    if root_index.is_file() and not is_excluded(Path("index.html"), excluded):
        tree.append(page_node(root_index, source_dir, site_url))

    for path in sorted(source_dir.glob("*.html")):
        if path.name == "index.html" or is_excluded(path.relative_to(source_dir), excluded):
            continue
        tree.append(page_node(path, source_dir, site_url))

    discovered_slugs = sorted(
        path.name
        for path in source_dir.iterdir()
        if path.is_dir()
        and path.name not in configured_slugs
        and not is_excluded(path.relative_to(source_dir), excluded)
    )
    ordered_slugs = configured_slugs + discovered_slugs

    for slug in ordered_slugs:
        directory = source_dir / slug
        section_spec = section_by_slug.get(slug, {})
        if directory.is_dir():
            node = directory_node(
                directory,
                source_dir,
                site_url,
                excluded,
                kind="section",
                title_override=section_spec.get("title"),
            )
        else:
            node = {
                "kind": "section",
                "slug": slug,
                "title": str(section_spec.get("title") or slug),
                "url": section_spec.get("url"),
                "available": False,
                "children": [],
            }
        if node is not None:
            tree.append(node)

    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    return {
        "schema_version": str(config["schema_version"]),
        "site_id": str(config["site_id"]),
        "site_title": str(config["site_title"]),
        "site_url": site_url,
        "generated_at": generated_at,
        "source_revision": source_revision(),
        "counts": {
            "sections": sum(1 for item in tree if item["kind"] == "section"),
            "pages": count_nodes(tree, "page"),
            "groups": count_nodes(tree, "group"),
        },
        "tree": tree,
    }


def count_nodes(nodes: list[dict[str, Any]], kind: str) -> int:
    total = 0
    for node in nodes:
        if node.get("kind") == kind:
            total += 1
        total += count_nodes(node.get("children", []), kind)
    return total


def validate_output(data: dict[str, Any]) -> None:
    if data.get("schema_version") != "1.0":
        raise ValueError("Unsupported schema_version")
    if not isinstance(data.get("tree"), list):
        raise ValueError("tree must be a list")

    seen_urls: set[str] = set()

    def validate_nodes(nodes: list[dict[str, Any]]) -> None:
        for node in nodes:
            if node.get("kind") not in {"page", "section", "group"}:
                raise ValueError(f"Invalid node kind: {node.get('kind')}")
            if not node.get("title"):
                raise ValueError("Every node must have a title")
            url = node.get("url")
            if node["kind"] == "page" and not url:
                raise ValueError(f"Page has no URL: {node}")
            if url:
                if url in seen_urls:
                    raise ValueError(f"Duplicate node URL: {url}")
                seen_urls.add(url)
            children = node.get("children", [])
            if not isinstance(children, list):
                raise ValueError("children must be a list")
            validate_nodes(children)

    validate_nodes(data["tree"])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        default="sgos-site-tree.config.json",
        help="Path to the site-tree config, relative to repository root.",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output path. Defaults to <source_dir>/sgos-site-tree.json.",
    )
    args = parser.parse_args()

    repository_root = Path.cwd()
    config = load_config(repository_root / args.config)
    data = build_tree(config, repository_root)
    validate_output(data)

    output_path = (
        repository_root / args.output
        if args.output
        else repository_root / str(config["source_dir"]) / "sgos-site-tree.json"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"Wrote {output_path} "
        f"({data['counts']['sections']} sections, "
        f"{data['counts']['groups']} groups, "
        f"{data['counts']['pages']} pages)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
