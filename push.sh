#!/usr/bin/env bash
set -euo pipefail

# 提交并推送当前仓库到远程 origin
# 用法示例：
#   ./push.sh "feat: 更新 p31 渠道口径与预览生成"
# 若未传入参数，将使用带时间戳的默认提交说明。

cd "$(dirname "$0")"

MSG=${1:-"chore: sync $(date '+%Y-%m-%d %H:%M:%S')"}

# 确保是 Git 仓库
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "未检测到 Git 仓库，正在初始化..."
  git init
fi

# 选择当前分支（若无法解析则使用 main 并创建）
BRANCH=$(git symbolic-ref --quiet --short HEAD || echo main)
if ! git rev-parse --verify "$BRANCH" >/dev/null 2>&1; then
  git checkout -B "$BRANCH"
fi

# 暂存并提交
git add -A
if git diff --cached --quiet; then
  echo "没有需要提交的更改。"
else
  git commit -m "$MSG"
fi

# 校验远程
if ! git remote get-url origin >/dev/null 2>&1; then
  echo "未配置远程 origin。请先执行："
  echo "  git remote add origin <your-repo-url>"
  exit 1
fi

# 推送
git push -u origin "$BRANCH"
echo "已推送到 origin/$BRANCH"