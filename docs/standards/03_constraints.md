---
title: 约束与规则
---

## 11. 约束与规则（固定）
- 架构：边界先行、容器分离、三层架构
- 代码规范：
  - 通用：camelCase, 2空格缩进, 中文注释
  - 语言特定：
    - Python: 变量/函数使用小写+下划线（snake_case），类使用大驼峰（PascalCase）
    - JavaScript/TypeScript: 变量/函数使用小驼峰（camelCase），类使用大驼峰（PascalCase）
    - 常量：使用大写+下划线（UPPER_SNAKE_CASE）
    - 文件名：Python 用下划线，JS 用小驼峰或连字符（保持项目一致）
- 禁止：直接操作 DOM、绕过 API 访问数据库
- 变更记录：每次变更后运行 `./scripts/cleanup.sh` 并更新 `CHANGELOG.md`
- **文档-代码一致性检查**：每次代码变更后，AI 必须检查并更新对应的需求文档和技术方案。若用户手动修改代码，应通过自然语言指令要求 AI 同步文档。
- 记忆库维护：每次重大决策后，AI 必须更新 `memory-bank/决策记录.md`。