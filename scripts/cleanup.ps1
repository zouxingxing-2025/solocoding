# 清理脚本 - 删除项目中的临时文件、缓存、日志等
# 用法: .\scripts\cleanup.ps1

Write-Host "开始清理项目临时文件..." -ForegroundColor Cyan

# 删除 .ai 目录下的临时子目录
Remove-Item -Path ".ai/tmp/" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path ".ai/cache/" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path ".ai/reports/" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path ".ai/backup/" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path ".ai/logs/" -Recurse -Force -ErrorAction SilentlyContinue

# 删除经验库待整理目录
Remove-Item -Path ".ai/经验库/待整理/" -Recurse -Force -ErrorAction SilentlyContinue

# 删除 demo 临时目录
Remove-Item -Path ".ai/demos/" -Recurse -Force -ErrorAction SilentlyContinue

# 删除项目根目录下的临时文件
Remove-Item -Path "*.tmp" -Force -ErrorAction SilentlyContinue
Remove-Item -Path "*.bak" -Force -ErrorAction SilentlyContinue
Remove-Item -Path "*.log" -Force -ErrorAction SilentlyContinue

# 删除测试覆盖率报告
Remove-Item -Path "htmlcov" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path ".coverage" -Force -ErrorAction SilentlyContinue
Remove-Item -Path "coverage.xml" -Force -ErrorAction SilentlyContinue

# 删除 Python 缓存
Get-ChildItem -Path . -Directory -Name "__pycache__" -Recurse | ForEach-Object { Remove-Item -Path $_ -Recurse -Force -ErrorAction SilentlyContinue }
Get-ChildItem -Path . -File -Name "*.pyc" -Recurse | ForEach-Object { Remove-Item -Path $_ -Force -ErrorAction SilentlyContinue }

# 删除 Node.js 缓存
Remove-Item -Path "node_modules/.cache/" -Recurse -Force -ErrorAction SilentlyContinue

Write-Host "清理完成。" -ForegroundColor Green
