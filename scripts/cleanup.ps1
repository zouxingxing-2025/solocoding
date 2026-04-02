# Cleanup script - Delete temporary files, cache, logs, etc.
# Usage: .\scripts\cleanup.ps1

Write-Host "Starting cleanup of temporary files..." -ForegroundColor Cyan

# Delete temporary subdirectories under .ai
Remove-Item -Path ".ai/tmp/" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path ".ai/cache/" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path ".ai/reports/" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path ".ai/backup/" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path ".ai/logs/" -Recurse -Force -ErrorAction SilentlyContinue

# Delete experience pending directory
Remove-Item -Path ".ai/experience-pending/" -Recurse -Force -ErrorAction SilentlyContinue

# Delete demo temporary directory
Remove-Item -Path ".ai/demos/" -Recurse -Force -ErrorAction SilentlyContinue

# Delete temporary files in root directory
Remove-Item -Path "*.tmp" -Force -ErrorAction SilentlyContinue
Remove-Item -Path "*.bak" -Force -ErrorAction SilentlyContinue
Remove-Item -Path "*.log" -Force -ErrorAction SilentlyContinue

# Delete test coverage reports
Remove-Item -Path "htmlcov" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path ".coverage" -Force -ErrorAction SilentlyContinue
Remove-Item -Path "coverage.xml" -Force -ErrorAction SilentlyContinue

# Delete Python cache
Get-ChildItem -Path . -Directory -Name "__pycache__" -Recurse | ForEach-Object { Remove-Item -Path $_ -Recurse -Force -ErrorAction SilentlyContinue }
Get-ChildItem -Path . -File -Name "*.pyc" -Recurse | ForEach-Object { Remove-Item -Path $_ -Force -ErrorAction SilentlyContinue }

# Delete Node.js cache
Remove-Item -Path "node_modules/.cache/" -Recurse -Force -ErrorAction SilentlyContinue

Write-Host "Cleanup completed." -ForegroundColor Green