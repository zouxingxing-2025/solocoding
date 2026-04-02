#!/usr/bin/env python3
"""
从备份恢复文件并添加 When to Use 和 Not For 章节。
"""

import shutil
from pathlib import Path

SKILLS_DIR = Path(".trae/skills")
BACKUP_DIR = Path(".backup/skills_before_frontmatter")


def add_when_use_not_for(content: str, name: str) -> str:
    """添加 When to Use 和 Not For 章节（如果缺失）"""
    if '## When to Use This Skill' in content and '## Not For' in content:
        return content
    
    # 如果已经有 Advance 章节，在它后面添加新章节
    if '## Advance' in content:
        # 找到 Advance 章节的位置
        lines = content.splitlines(True)
        new_lines = []
        added = False
        
        for i, line in enumerate(lines):
            new_lines.append(line)
            
            if not added and line.strip().startswith('## Advance'):
                # 找到 Advance 章节的结束（下一个 ## 或文件尾）
                j = i + 1
                while j < len(lines) and not lines[j].strip().startswith('##'):
                    new_lines.append(lines[j])
                    j += 1
                
                # 在 Advance 之后插入新章节
                new_lines.append('\n')
                new_lines.append('## When to Use This Skill\n')
                new_lines.append(f'Use this skill when {name} is required, such as during phase {name[0] if name else "unknown"} tasks.\n')
                new_lines.append('\n')
                new_lines.append('## Not For\n')
                new_lines.append('- This skill does not handle other phases or unrelated tasks.\n')
                new_lines.append('\n')
                added = True
                i = j - 1
        
        if added:
            return ''.join(new_lines)
    
    # 如果找不到 Advance，在文件末尾添加
    return content + f"\n\n## When to Use This Skill\nUse this skill when {name} is required.\n\n## Not For\n- This skill does not handle other phases or unrelated tasks.\n"


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
        new_content = add_when_use_not_for(content, name)
        
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
