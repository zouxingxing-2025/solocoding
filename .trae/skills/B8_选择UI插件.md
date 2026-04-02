---
name: 选择UI插件
description: 为每个功能模块选择或生成合适的 UI 插件，并统一界面风格。
allowed-tools: Read, Write
---

# 前置条件
- `.ai/进度状态.json` 中的 `current_step` 必须为 `B8`。
- `B7` 已完成。

## 目标
为每个功能模块选择或生成合适的 UI 插件（如表格、表单、图表、KPI卡片等），并统一界面风格。

## Action
- 读取 `.ai/config/modules.yaml` 和 `data-model.json`，以及已选定的 API 插件配置。
- 对于每个模块，根据其展示类型匹配 UI 插件：
  - 列表/表格 → 数据表格插件（支持分页、排序、筛选）
  - 表单/输入 → 表单生成器插件（基于字段类型自动生成输入控件）
  - 统计图表 → 图表插件（如折线图、柱状图、饼图）
  - KPI 卡片 → 指标卡片插件
  - 详情页 → 详情展示插件
- 生成 UI 插件配置（如列定义、图表类型、表单字段映射），存入 `.ai/config/plugins.yaml` 的 `ui_plugins` 部分。
- 确保所有模块的 UI 插件使用统一的设计系统（如 Ant Design、Element Plus）。

## Assert
- 每个模块至少绑定一个 UI 插件。
- 插件配置中的字段在 `data-model.json` 中存在。

## Artefact
- 更新后的 `.ai/config/plugins.yaml`。

## Analysis
- 检查插件是否与已有页面布局冲突。
- 若存在多种插件候选，按推荐度排序（优先使用轻量级、已验证的插件）。

## Adjust
- 如果某个模块没有合适的 UI 插件，标记为"需自定义开发"，并生成基础 HTML 骨架。

## Advance
- 更新 `.ai/进度状态.json`：
  ```json
  {
    "current_step": "B9",
    "steps_completed": ["...", "B8"]
  }
  ```
- 提示用户：下一步应执行 B9。

## 干预
无。
