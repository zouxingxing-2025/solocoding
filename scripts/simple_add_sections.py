#!/usr/bin/env python3
"""
从备份恢复文件并添加 When to Use 和 Not For 章节（简单版本）。
"""

import shutil
from pathlib import Path

SKILLS_DIR = Path(".trae/skills")
BACKUP_DIR = Path(".backup/skills_before_frontmatter")


def add_sections_simple(content: str, name: str) -> str:
    """简单版本：只在文件末尾添加章节（如果不存在）"""
    if '## When to Use This Skill' in content and '## Not For' in content:
        return content
    
    # 简单直接在文件末尾添加
    return content + f"\n\n## When to Use This Skill\nUse this skill when {name} is required, such as during phase {name[0] if name else 'unknown'} tasks.\n\n## Not For\n- This skill does not handle other phases or unrelated tasks.\n"


def main():
    # 从备份恢复文件
    print("从备份恢复文件...")
    for backup_file in BACKUP_DIR.glob("*.md"):
        dest_file = SKILLS_DIR / backup_file.name
        shutil.copy2(backup_file, dest_file)
        print(f"  已恢复: {backup_file.name}")
    
    print("\n添加 When to Use 和 Not For 章节...")
    count = 0
    
    for md_file in SKILLS_DIR.glob("*.md"):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        name = md_file.stem
        new_content = add_sections_simple(content, name)
        
        if new_content != content:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  已更新: {md_file.name}")
            count += 1
        else:
            print(f"  跳过（已有章节）: {md_file.name}")
    
    print(f"\n处理完成！共更新 {count} 个文件。")


if __name__ == "__main__":
    main()
