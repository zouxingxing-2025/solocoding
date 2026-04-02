#!/bin/bash
# 清理脚本 - 删除项目中的临时文件、缓存、日志等
# 用法: ./scripts/cleanup.sh

set -e

echo "开始清理项目临时文件..."

# 删除 .ai 目录下的临时子目录
rm -rf .ai/tmp/
rm -rf .ai/cache/
rm -rf .ai/reports/
rm -rf .ai/backup/
rm -rf .ai/logs/

# 删除经验库待整理目录（保留已分类）
rm -rf .ai/经验库/待整理/

# 删除 demo 临时目录
rm -rf .ai/demos/

# 删除项目根目录下的临时文件
rm -f *.tmp *.bak *.log

# 删除测试覆盖率报告
rm -rf htmlcov/ .coverage coverage.xml

# 删除 Python 缓存
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -type f -name "*.pyc" -delete

# 删除 Node.js 缓存
rm -rf node_modules/.cache/

# 删除沙箱临时文件（如果存在）
rm -rf /tmp/sandbox-* 2>/dev/null || true

echo "清理完成。"
