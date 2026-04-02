#!/usr/bin/env python3
"""
批量添加 frontmatter 到所有技能文件。
使用前请先创建 Git 备份分支（@创建备份分支）。
如果结果不满意，可以执行 @回滚到备份分支 恢复。
"""

import re
import sys
import shutil
from pathlib import Path
from datetime import datetime

# 配置
SKILLS_DIR = Path(".trae/skills")
BACKUP_DIR = Path(".backup/skills_before_frontmatter")
DRY_RUN = False  # 设为 True 可先预览，不实际写入


def backup_file(filepath: Path):
    """备份原文件"""
    backup_path = BACKUP_DIR / filepath.name
    backup_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(filepath, backup_path)
    print(f"  已备份: {filepath.name}")


def has_frontmatter(content: str) -> bool:
    """检查是否已有 frontmatter"""
    return content.strip().startswith('---')


def extract_description(content: str, filename: str) -> str:
    """从 '## 目标' 或 '# 目标' 提取描述"""
    match = re.search(r'#+\s*目标\s*\n(.*?)(?=\n#+\s|\Z)', content, re.DOTALL)
    if match:
        desc = match.group(1).strip().split('\n')[0].strip()
        if len(desc) > 200:
            desc = desc[:197] + '...'
        return desc
    # 后备：从文件名生成
    name = filename.replace('.md', '').replace('_', ' ')
    return f"执行 {name} 步骤，完成项目流程中的特定任务。"


def generate_frontmatter(name: str, description: str) -> str:
    """生成 YAML frontmatter"""
    return f"""---
name: {name}
description: {description}
allowed-tools: Bash, Read, Write
---

"""


def add_when_use_not_for(content: str, name: str) -> str:
    """添加 When to Use 和 Not For 章节（如果缺失）"""
    if '## When to Use' in content and '## Not For' in content:
        return content
    
    # 首先检查是否有多余的重复内容（如果有，先清理）
    # 查找最后一个 Advance 章节之后的内容，看看是否已经有重复添加的内容
    if '## Advance' in content:
        # 找到 Advance 章节之后的位置
        lines = content.splitlines(True)
        new_lines = []
        advance_found = False
        added_new_sections = False
        
        for i, line in enumerate(lines):
            # 如果已经添加了新章节，且遇到了旧的重复内容，跳过旧内容
            if added_new_sections and (line.strip().startswith('## Advance') or '提示用户：' in line or '更新 .ai/进度状态.json' in line):
                continue
                
            new_lines.append(line)
            
            if line.strip().startswith('## Advance'):
                advance_found = True
                # 找到 Advance 章节的结束（下一个 ## 或文件尾）
                j = i + 1
                while j < len(lines) and not lines[j].strip().startswith('##'):
                    new_lines.append(lines[j])
                    j += 1
                
                # 插入新章节
                new_lines.append('\n')
                new_lines.append('## When to Use This Skill\n')
                new_lines.append(f'Use this skill when {name} is required, such as during phase {name[0] if name else "unknown"} tasks.\n')
                new_lines.append('\n')
                new_lines.append('## Not For\n')
                new_lines.append('- This skill does not handle other phases or unrelated tasks.\n')
                new_lines.append('\n')
                added_new_sections = True
                i = j - 1  # 跳过已处理的 Advance 后续行
        
        if added_new_sections:
            return ''.join(new_lines)
    
    # 如果找不到 Advance，则在文件末尾添加
    return content + f"\n\n## When to Use This Skill\nUse this skill when {name} is required.\n\n## Not For\n- This skill does not handle other phases or unrelated tasks.\n"


def process_file(filepath: Path):
    """处理单个文件"""
    print(f"处理: {filepath.name}")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    new_content = content
    
    # 检查是否需要添加 When to Use 和 Not For
    if '## When to Use' not in content or '## Not For' not in content:
        name = filepath.stem
        new_content = add_when_use_not_for(new_content, name)
        modified = True
        print(f"  将添加 When to Use 和 Not For 章节")
    
    # 检查是否需要添加 frontmatter
    if not has_frontmatter(content):
        name = filepath.stem
        description = extract_description(content, filepath.name)
        frontmatter = generate_frontmatter(name, description)
        new_content = frontmatter + new_content
        modified = True
        print(f"  将添加 frontmatter")
    
    if not modified:
        print(f"  跳过（无需修改）")
        return
    
    if not DRY_RUN:
        backup_file(filepath)
    
    if DRY_RUN:
        print(f"  [干运行] 将更新文件")
        return
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"  已更新: {filepath.name}")


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
        print("\n干运行完成。若要实际执行，请将脚本中的 DRY_RUN 设置为 False。")
        print("执行前请先运行 @创建备份分支 创建 Git 备份。")
    else:
        print(f"\n处理完成！")
        print("请检查修改结果，如有问题可使用 @回滚到备份分支 恢复。")


if __name__ == "__main__":
    # 默认干运行模式，确认无误后改为 False
    DRY_RUN = False
    main()
