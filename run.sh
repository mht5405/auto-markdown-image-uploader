#!/bin/bash

# 脚本用于运行 Markdown 图片上传工具
# 用法: ./run.sh /path/to/your/markdown/file.md

if [ $# -eq 0 ]; then
    echo "用法: $0 <Markdown文件路径>"
    echo "例如: $0 /Users/your/path/article.md"
    exit 1
fi

FILE_PATH="$1"

# 检查文件是否存在
if [ ! -f "$FILE_PATH" ]; then
    echo "错误: 文件 '$FILE_PATH' 不存在"
    exit 1
fi

# 检查文件扩展名
if [[ "$FILE_PATH" != *.md ]]; then
    echo "错误: 文件必须是 .md 格式"
    exit 1
fi

# 运行脚本
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "正在处理文件: $FILE_PATH"
"/Users/liuhuahui/Nutstore Files/md_ducument/01.日志/01.bloggers/00.自动化图床/.venv/bin/python" photo_transform.py "$FILE_PATH"

echo "处理完成！"