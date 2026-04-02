---
name: 锁定选中demo
description: 将用户选中的demo锁定为最终版本，丢弃其他未选中的demo。
allowed-tools: Write, Bash
---

# 前置条件
- `.ai/进度状态.json` 中的 `current_step` 必须为 `C9`。
- `C8` 已完成（用户已选择demo）。

## 目标
将用户选中的demo锁定为最终版本，并丢弃其他未选中的demo及其相关临时文件，避免后续混淆。

## Action
- 读取 `.ai/进度状态.json` 中的 `selected_demo` 字段。
- 将选中的demo代码从 `.ai/demos/demo_<selected>/` 复制到项目根目录（或保留在 `.ai/demos/final/`）。
- 删除其他未选中的demo目录（`.ai/demos/demo_*` 除了选中的）。
- 清理预览环境配置（如临时端口映射、docker-compose片段）。
- 记录最终选中的demo信息到 `.ai/进度状态.json` 的 `final_demo` 字段。

## Assert
- 选中的demo代码已被完整保留。
- 其他demo目录已被删除。

## Artefact
- 最终demo代码（位于项目根目录或 `.ai/demos/final/`）。
- 更新后的进度状态。

## Analysis
- 检查是否误删了依赖的共享文件（如公共库），若存在则恢复或提示。
- 记录用户选择偏好，作为成功经验存入全局经验库。

## Adjust
- 如果复制过程中出现冲突（如目标文件已存在），备份原文件后覆盖。

## Advance
- 更新 `.ai/进度状态.json`：
  ```json
  {
    "current_step": "D1",
    "steps_completed": ["...", "C9"]
  }
  ```
- 提示用户：阶段3完成，下一步进入阶段4（部署与发布），应执行 D1。

## 干预
无。
