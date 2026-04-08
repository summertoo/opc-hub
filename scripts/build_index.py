#!/usr/bin/env python3
"""手动构建 directory/index.yaml"""

import os
import yaml
from datetime import datetime

MEMBERS_DIR = os.path.join(os.path.dirname(__file__), "../directory/members")
INDEX_FILE = os.path.join(os.path.dirname(__file__), "../directory/index.yaml")

FRONTMATTER_FIELDS = ["handle", "name", "title", "skills", "industries",
                      "location", "available", "looking_for", "contact", "established"]

def parse_frontmatter(filepath):
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    if not content.startswith("---"):
        return None
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None
    data = yaml.safe_load(parts[1])
    data["file"] = "members/" + os.path.basename(filepath)
    return {k: data[k] for k in FRONTMATTER_FIELDS + ["file"] if k in data}

def build():
    members = []
    for fname in sorted(os.listdir(MEMBERS_DIR)):
        if fname.endswith(".md") and fname != "example.md":
            m = parse_frontmatter(os.path.join(MEMBERS_DIR, fname))
            if m:
                members.append(m)

    index = {
        "meta": {
            "total": len(members),
            "last_built": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "version": "1.0"
        },
        "members": members
    }

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write("# OPC Hub 目录索引\n")
        f.write("# 此文件由 scripts/build_index.py 手动构建，请勿直接编辑\n\n")
        yaml.dump(index, f, allow_unicode=True, sort_keys=False)

    print(f"✅ 索引构建完成，共 {len(members)} 位成员")

if __name__ == "__main__":
    build()
