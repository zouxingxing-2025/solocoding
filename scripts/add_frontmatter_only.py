#!/usr/bin/env python3
"""
仅添加 YAML frontmatter，不修改已有章节。
假设文件已经包含 When to Use 和 Not For 章节。
"""

import re
import sys
import shutil
from pathlib import Path

SKILLS_DIR = Path(".trae/skills")
BACKUP_DIR = Path(".backup/skills_frontmatter_only")
DRY_RUN = False


def has_frontmatter(content: str) -> bool:
    return content.strip().startswith('---')


def extract_description(content: str, filename: str) -> str:
    match = re.search(r'#+\s*目标\s*\n(.*?)(?=\n#+\s|\Z)', content, re.DOTALL)
    if match:
        desc = match.group(1).strip().split('\n')[0].strip()
        if len(desc) > 200:
            desc = desc[:197] + '...'
        return desc
    name = filename.replace('.md', '').replace('_', ' ')
    return f"执行 {name} 步骤，完成项目流程中的特定任务。"


def generate_frontmatter(name: str, description: str) -> str:
    return f"""---
name: {name}
description: {description}
allowed-tools: Bash, Read, Write
---

"""


def process_file(filepath: Path):
    print(f"处理: {filepath.name}")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if has_frontmatter(content):
        print(f"  跳过（已有 frontmatter）")
        return
    
    if not DRY_RUN:
        # 备份
        backup_path = BACKUP_DIR / filepath.name
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(filepath, backup_path)
        print(f"  已备份")
    
    name = filepath.stem
    description = extract_description(content, filepath.name)
    frontmatter = generate_frontmatter(name, description)
    new_content = frontmatter + content
    
    if DRY_RUN:
        print(f"  [干运行] 将添加 frontmatter")
        return
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"  已更新")


def main():
    if not SKILLS_DIR.exists():
        print(f"错误: {SKILLS_DIR} 目录不存在")
        sys.exit(1)
    
    if not DRY_RUN:
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        print(f"备份目录: {BACKUP_DIR}")
    
    md_files = list(SKILLS_DIR.glob("*.md"))
    print(f"找到 {len(md_files)} 个技能文件")
    
    for md_file in md_files:
        process_file(md_file)
    
    if DRY_RUN:
        print("\n干运行完成。若要实际执行，请将 DRY_RUN 设置为 False。")
    else:
        print("\n处理完成！请检查结果，如有问题可使用 Git 回滚。")


if __name__ == "__main__":
    DRY_RUN = True
    main()
