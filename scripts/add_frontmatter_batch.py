#!/usr/bin/env python3
"""
批量添加 frontmatter 和章节到所有技能文件。
使用前请先创建 Git 备份分支（@创建备份分支）。
如果结果不满意，可以执行 @回滚到备份分支 恢复。

修复记录：
- Issue1: 移除基于内容关键词的误删逻辑，仅通过精确章节标题检测
- Issue2: 统一使用完整标题 '## When to Use This Skill' 和 '## Not For'
- Issue3: DRY_RUN 默认值改为 False（直接执行）
"""

import re
import sys
import shutil
from pathlib import Path

# 配置
SKILLS_DIR = Path(".trae/skills")
BACKUP_DIR = Path(".backup/skills_before_frontmatter")
DRY_RUN = False          # 默认直接执行（设为 True 为预览模式）


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
    """
    添加 When to Use 和 Not For 章节（如果缺失）。
    
    修复说明：
    - 使用精确的完整标题检测，避免重复添加
    - 不删除任何已有内容，仅追加缺失章节
    """
    # 精确检查完整标题
    if '## When to Use This Skill' in content and '## Not For' in content:
        return content

    # 查找插入位置（在 Advance 章节之后）
    if '## Advance' in content:
        # 找到 Advance 章节的结束位置
        lines = content.splitlines(True)
        new_lines = []
        inserted = False
        
        for i, line in enumerate(lines):
            new_lines.append(line)
            
            if not inserted and line.strip().startswith('## Advance'):
                # 找到 Advance 章节的最后一行
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
                inserted = True
                i = j - 1  # 跳过已处理的后续行
        
        if inserted:
            return ''.join(new_lines)

    # 如果找不到 Advance，则在文件末尾添加
    return content + f"\n\n## When to Use This Skill\nUse this skill when {name} is required.\n\n## Not For\n- This skill does not handle other phases or unrelated tasks.\n"


def process_file(filepath: Path):
    """处理单个文件"""
    print(f"处理: {filepath.name}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if has_frontmatter(content):
        print(f"  跳过（已有 frontmatter）")
        return

    if not DRY_RUN:
        backup_file(filepath)

    name = filepath.stem
    description = extract_description(content, filepath.name)
    frontmatter = generate_frontmatter(name, description)
    new_content = frontmatter + content
    new_content = add_when_use_not_for(new_content, name)

    if DRY_RUN:
        print(f"  [干运行] 将添加 frontmatter 和章节")
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
        print(f"\n处理完成！共处理 {len(md_files)} 个文件。")
        print("请检查修改结果，如有问题可使用 @回滚到备份分支 恢复。")


if __name__ == "__main__":
    # 默认直接执行（False），如需预览请改为 True
    DRY_RUN = False
    main()
