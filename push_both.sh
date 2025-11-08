#!/usr/bin/env bash
set -euo pipefail

# 双远程提交并推送脚本：同时推送到 GitHub(origin) 与 Gitee(gitee)
# 使用方法：
#   ./push_both.sh "feat: 更新 p29/p13 生成与比较"
# 若未传入消息，将使用带时间戳的默认提交信息。

cd "$(dirname "$0")"

MSG=${1:-"chore: 双远程同步 $(date '+%Y-%m-%d %H:%M:%S')"}

# 确保在 Git 仓库中
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "错误：当前目录不是 Git 仓库。请先执行 git init。"
  exit 1
fi

# 解析或创建当前分支
BRANCH=$(git symbolic-ref --quiet --short HEAD || echo main)
if ! git rev-parse --verify "$BRANCH" >/dev/null 2>&1; then
  git checkout -B "$BRANCH"
fi

# 暂存并提交（若有更改）
git add -A
if git diff --cached --quiet; then
  echo "没有需要提交的更改。"
else
  git commit -m "$MSG"
fi

# 校验远程 origin（GitHub）
if ! git remote get-url origin >/dev/null 2>&1; then
  echo "错误：未配置远程 origin（GitHub）。请先执行："
  echo "  git remote add origin <github仓库地址>"
  exit 1
fi

# 校验远程 gitee（Gitee）
if ! git remote get-url gitee >/dev/null 2>&1; then
  echo "错误：未配置远程 gitee（Gitee）。请先执行："
  echo "  git remote add gitee <gitee仓库地址>"
  exit 1
fi

# 推送到 GitHub（origin）
echo "推送到 GitHub（origin/${BRANCH}）..."
git push origin "$BRANCH"

# 推送到 Gitee（gitee）
echo "推送到 Gitee（gitee/${BRANCH}）..."
git push gitee "$BRANCH"

echo "双远程推送完成。"