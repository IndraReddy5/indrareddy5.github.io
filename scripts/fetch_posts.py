#!/usr/bin/env python3
"""Fetch blog posts from Hashnode and generate Hugo content files."""

import json
import os
import re
import sys
from urllib import request as urllib_request

HASHNODE_HOST = os.environ.get("HASHNODE_HOST", "indrareddy.hashnode.dev")
CONTENT_DIR = os.path.join(os.path.dirname(__file__), "..", "content", "blog")


def fetch_posts(host):
    gql = {
        "query": """
        {
          publication(host: "%s") {
            posts(first: 50) {
              edges {
                node {
                  title
                  brief
                  slug
                  publishedAt
                  readTimeInMinutes
                  tags { name }
                  coverImage { url }
                  content { html }
                }
              }
            }
          }
        }
        """ % host
    }
    data = json.dumps(gql).encode()
    req = urllib_request.Request(
        "https://gql.hashnode.com",
        data=data,
        headers={"Content-Type": "application/json"},
    )
    with urllib_request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read())
    if "errors" in result:
        print("GraphQL errors:", result["errors"], file=sys.stderr)
        sys.exit(1)
    return result["data"]["publication"]["posts"]["edges"]


def yaml_str(value):
    """Wrap a string value safely for YAML frontmatter."""
    escaped = str(value).replace('"', '\\"')
    return f'"{escaped}"'


def write_post(post):
    slug = post["slug"]
    title = post["title"]
    date = post["publishedAt"]
    brief = post.get("brief") or ""
    tags = [t["name"] for t in (post.get("tags") or [])]
    read_time = post.get("readTimeInMinutes") or 5
    cover = (post.get("coverImage") or {}).get("url") or ""
    html_content = post["content"]["html"]

    tags_yaml = "\n".join(f'  - {yaml_str(t)}' for t in tags) if tags else ""
    tags_block = f"tags:\n{tags_yaml}\n" if tags_yaml else ""

    hashnode_url = f"https://{HASHNODE_HOST}/{slug}"

    frontmatter = (
        f"---\n"
        f"title: {yaml_str(title)}\n"
        f"date: {date}\n"
        f"description: {yaml_str(brief)}\n"
        f"{tags_block}"
        f"readingTime: {read_time}\n"
        f"coverImage: {yaml_str(cover)}\n"
        f"hashnodeUrl: {yaml_str(hashnode_url)}\n"
        f"---\n\n"
    )

    filepath = os.path.join(CONTENT_DIR, f"{slug}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(frontmatter + html_content + "\n")
    return filepath


def main():
    os.makedirs(CONTENT_DIR, exist_ok=True)

    # Remove previously generated post files (keep _index.md)
    for fname in os.listdir(CONTENT_DIR):
        if fname.endswith(".md") and fname != "_index.md":
            os.remove(os.path.join(CONTENT_DIR, fname))

    print(f"Fetching posts from {HASHNODE_HOST}…")
    edges = fetch_posts(HASHNODE_HOST)

    for edge in edges:
        path = write_post(edge["node"])
        print(f"  wrote {os.path.basename(path)}")

    print(f"Done — {len(edges)} post(s) generated.")


if __name__ == "__main__":
    main()
