---
name: 生成CI_CD配置文件
description: 根据技术栈生成 CI/CD 配置文件（如 GitHub Actions、GitLab CI）。
allowed-tools: Read, Write
---

# 前置条件
- `.ai/进度状态.json` 中的 `current_step` 必须为 `B10`。
- `B9.1` 已完成。

## 目标
根据项目技术栈和部署需求，生成 CI/CD 配置文件（如 `.github/workflows/deploy.yml`、`.gitlab-ci.yml`）。

## Action
- 读取 `AGENTS.md` 第2章（技术栈）和第8章（部署配置）。
- 选择 CI/CD 平台（默认 GitHub Actions，用户可指定）。
- 生成配置文件，包含以下阶段：
  - 代码检出
  - 依赖安装
  - 代码检查（Lint、格式）
  - 测试运行（单元测试、集成测试）
  - 构建制品（Docker 镜像或压缩包）
  - 部署到目标