---
name: 生成多demo
description: 基于当前代码生成2-3个不同实现方式的候选demo，供用户试用和选择。
allowed-tools: Read, Write, Bash
---

# 前置条件
- `.ai/进度状态.json` 中的 `current_step` 必须为 `C6`。
- `C5` 已完成（审查通过或用户确认忽略问题）。

## 目标
基于当前已生成并审查通过的代码，创建2-3个不同实现方式的候选demo（例如使用不同的UI库、图表库或API设计），供用户试用和选择。

## Action
- 读取当前模块的代码、数据模型和需求文档。
- 确定可变的实现点（如UI组件库、图表库、数据缓存策略、分页方式等）。
- 生成2-3个变体：
  - Demo A：使用默认配置（按当前设计）。
  - Demo B：替换UI库（如从Ant Design换为Material-UI）或图表库。
  - Demo C：优化性能实现（如添加缓存、分页）。
- 每个demo独立构建，生成独立的预览目录（`.ai/demos/demo_A/`, `.ai/demos/demo_B/`等）。
- 为每个demo生成简单的启动脚本和说明。

## Assert
- 至少生成2个候选demo。
- 每个demo都能独立运行（基本功能可用）。

## Artefact
- 各demo的代码目录（`.ai/demos/demo_*/`）。
- demo列表文件（`.ai/demos/demo_list.json`），包含名称、路径、特点说明。

## Analysis
- 比较各demo的差异点，列出优缺点供用户参考。
- 如果某个demo构建失败，自动回退到默认配置。

## Adjust
- 若生成多个demo导致磁盘空间不足，提示用户清理或限制数量。
- 若用户只需要一个demo，可跳过此步骤（设置 `max_demos: 1`）。

## Advance
- 更新 `.ai/进度状态.json`：
  ```json
  {
    "current_step": "C7",
    "steps_completed": ["...", "C6"]
  }
  ```
- 提示用户：下一步应执行 C7。

## 干预
无。


## When to Use This Skill
Use this skill when C6_生成多demo is required, such as during phase C tasks.

## Not For
- This skill does not handle other phases or unrelated tasks.
