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
  - 部署到目标服务器（如通过 SSH 或云服务）
- 将配置文件写入项目根目录下的相应路径（如 `.github/workflows/deploy.yml`）。

## Assert
- 配置文件语法正确（可引用现有模板）。
- 包含必要的环境变量和密钥占位符（如 `${{ secrets.DEPLOY_KEY }}`）。

## Artefact
- CI/CD 配置文件。

## Analysis
- 检查部署步骤是否与 `deployment.yaml` 中的配置一致。
- 若使用 Docker，确保已生成 `Dockerfile`。

## Adjust
- 如果用户未指定 CI/CD 平台，使用 GitHub Actions 作为默认。
- 若部署需要特定密钥，提示用户在仓库设置中添加。

## Advance
- 更新 `.ai/进度状态.json`：
  ```json
  {
    "current_step": "B11",
    "steps_completed": ["...", "B10"]
  }
  ```
- 提示用户：下一步应执行 B11。

## 干预
无。
