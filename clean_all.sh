#!/bin/sh
# 目的：在项目根目录下清空所有 logs、output、tmp 目录中的内容（保留目录本身）
#
# 说明：
# - 默认仅在 /Users/jinghai/coder/gen_ppt 根路径及其子目录中执行。
# - 清空这三类目录内的所有文件与子目录（含隐藏文件），不删除目录本身。
# - 为避免误删，脚本包含路径安全限制：仅允许对项目根目录及其子目录执行。
# - 兼容 macOS 的 /bin/sh（POSIX）环境，无需额外依赖。
#
# 使用：
#   1) 直接在项目根路径执行：
#      sh ./clean_all.sh
#   2) 指定根路径（必须是项目根或其子路径）：
#      sh ./clean_all.sh /Users/jinghai/coder/gen_ppt
#
# 注意：
# - 脚本仅处理名为 "logs"、"output"、"tmp" 的目录。
# - 跳过 .git 目录下的内容。
# - 若未找到任何目标目录，会提示信息并正常退出。

set -eu

DEFAULT_ROOT="/Users/jinghai/coder/gen_ppt"
ROOT="${1:-$DEFAULT_ROOT}"

# 安全防护：仅允许清理项目根路径或其子路径
case "$ROOT" in
  "$DEFAULT_ROOT"|"$DEFAULT_ROOT"/*) ;;
  *)
    echo "安全限制：仅允许清理路径 $DEFAULT_ROOT 及其子目录"
    echo "传入的路径为：$ROOT"
    exit 1
    ;;
esac

if [ ! -d "$ROOT" ]; then
  echo "路径不存在：$ROOT"
  exit 1
fi

echo "开始清空项目所有 logs、output、tmp 内容，根路径：$ROOT"

# 统计将要处理的目标目录数量（兼容 BSD find）并跳过 .git
dirs_count=$(find "$ROOT" -type d \( -name logs -o -name output -o -name tmp \) -not -path "*/.git/*" | wc -l | tr -d ' ')

if [ "$dirs_count" -eq 0 ]; then
  echo "未找到任何 logs、output 或 tmp 目录，无需清理。"
  exit 0
fi

# 清理每一个匹配的目录内容（包含隐藏项，跳过 .git）
find "$ROOT" -type d \( -name logs -o -name output -o -name tmp \) -not -path "*/.git/*" | while IFS= read -r dir; do
  # 统计清空前的条目数量（不递归，仅当前目录）
  if [ -d "${dir}" ]; then
    count=$(ls -A "${dir}" 2>/dev/null | wc -l | tr -d ' ')
  else
    count=0
  fi

  # 执行清空：普通与隐藏文件/目录。对于不存在的 glob 静默处理。
  rm -rf "${dir}"/* "${dir}"/.[!.]* "${dir}"/..?* 2>/dev/null || true

  echo "清空：${dir}（移除 ${count} 项）"
done

echo "已完成：清空 $dirs_count 个目录。"
echo "完成。"