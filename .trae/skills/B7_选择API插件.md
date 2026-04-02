---
name: 选择API插件
description: 为每个功能模块选择或生成合适的 API 插件。
allowed-tools: Read, Write
---

# 前置条件
- `.ai/进度状态.json` 中的 `current_step` 必须为 `B7`。
- `B6` 已完成。

## 目标
为每个功能模块选择或生成合适的 API 插件（如标准 CRUD、统计接口、导出等）。

## Action
- 读取 `.ai/config/modules.yaml` 和 `data-model.json`。
- 对于每个模块，根据其功能类型（列表展示、表单提交、报表统计等）匹配 API 插件：
  - 列表/详情 → 标准 CRUD 插件（自动生成基于数据模型的 REST API）
  - 统计图表 → 聚合查询插件（支持 group by、sum、count）
  - 导出 → 导出插件（CSV/Excel）
  - 自定义功能 → 提示用户提供 API 规范或选择通用插件
- 生成插件配置（如实体名称、字段映射、权限等），存入 `.ai/config/plugins.yaml` 的 `api_plugins` 部分。

## Assert
- 每个模块至少绑定一个 API 插件。
- 插件配置中的实体和字段在 `data-model.json` 中存在。

## Artefact
- 更新后的 `.ai/config/plugins.yaml`。

## Analysis
- 检查插件是否与已有模块冲突（如重复路由）。
- 若存在多种插件候选，按推荐度排序（优先使用经过验证的插件）。

## Adjust
- 如果某个模块没有合适的插件，标记为"需自定义开发"，并生成 API 骨架供用户填充。

## Advance
- 更新 `.ai/进度状态.json`：
  ```json
  {
    "current_step": "B8",
    "steps_completed": ["...", "B7"]
  }
  ```
- 提示用户：下一步应执行 B8。

## 干预
无。
