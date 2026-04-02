---
name: 配置SSL证书
description: 为域名配置 SSL 证书（如 Let's Encrypt），启用 HTTPS。
allowed-tools: Bash, Network, Write
---

# 前置条件
- `.ai/进度状态.json` 中的 `current_step` 必须为 `D9`。
- `D8` 已完成（反向代理已配置）。

## 目标
为域名配置 SSL 证书（如 Let's Encrypt），启用 HTTPS。

## Action
- 读取 `.ai/config/deployment.yaml` 中的域名和邮箱。
- 使用 Certbot 自动申请证书：
  - 安装 Certbot（如果未安装）：`apt-get install certbot python3-certbot-nginx`
  - 运行：`certbot --nginx -d your-domain.com --non-interactive --agree-tos -m your-email`
- 若自动申请失败，提供手动申请指南。
- 配置证书自动续期（`cron` 或 systemd timer）。
- 验证 HTTPS 是否生效（`curl -I https://your-domain.com`）。

## Assert
- 证书申请成功，Nginx 配置已更新。
- HTTPS 访问正常，无证书错误。

## Artefact
- 证书文件（系统目录）。
- 更新后的 Nginx 配置。
- 部署日志（`.ai/logs/ssl_setup.log`）。

## Analysis
- 检查域名 DNS 解析是否已指向服务器。
- 若证书申请失败，分析原因（DNS 未解析、端口 80 不可访问）。

## Adjust
- 如果用户已有证书，可手动上传并配置。
- 若用户不需要 HTTPS，可跳过此步骤。

## Advance
- 更新 `.ai/进度状态.json`：
  ```json
  {
    "current_step": "D10",
    "steps_completed": ["...", "D9"]
  }
  ```
- 提示用户：下一步应执行 D10。

## 干预
需用户提供域名和邮箱。


## When to Use This Skill
Use this skill when D9_配置SSL证书 is required, such as during phase D tasks.

## Not For
- This skill does not handle other phases or unrelated tasks.
