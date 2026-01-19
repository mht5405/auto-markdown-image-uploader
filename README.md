# 自动化图床工具

## 简介

这是一个用于自动化处理 Markdown 文件中图片上传的工具。它可以自动扫描 Markdown 文件中的图片链接，上传本地图片到图床（如通过 PicList），并将原链接替换为图床链接，最终生成一个新的 Markdown 文件。

## 功能

- 自动识别 Markdown 文件中的图片语法 `![alt](path)`
- 支持相对路径和 URL 编码的路径（如 %20 空格）
- 上传图片到配置的图床
- 替换原链接为图床链接
- 生成新文件到 `upload` 文件夹中
- 支持命令行参数处理指定文件

## 安装

### 环境要求

- Python 3.6+
- PicList 工具（用于图片上传）

### 步骤

1. **克隆或下载项目文件**：
   - 将 `photo_transform.py` 和 `run.sh` 下载到同一文件夹。

2. **安装 Python 依赖**：
   ```bash
   pip install requests
   ```

3. **安装并配置 PicList**：
   - 下载并安装 [PicList](https://github.com/Kuingsmile/PicList-Core)（基于 PicGo-Core）。
   - 启动 PicList 服务：
     ```bash
     picgo-server -p 36677
     ```
   - 配置图床（如 SM.MS、GitHub 等）。

4. **设置脚本权限**：
   ```bash
   chmod +x run.sh
   ```

## 使用

### 基本用法

在终端中运行：
```bash
./run.sh /path/to/your/markdown/file.md
```

例如：
```bash
./run.sh "/Users/username/Documents/article.md"
```

脚本会：
- 处理指定的 Markdown 文件
- 上传其中的图片
- 在原文件目录创建 `upload` 文件夹
- 生成新文件 `原文件名_upload.md`

### 高级用法

直接运行 Python 脚本：
```bash
python photo_transform.py /path/to/file.md
```

如果不提供参数，使用默认文件（代码中设置的 `SOURCE_FILE`）。

## 配置

### PicList 配置

- 默认 URL：`http://127.0.0.1:36677/upload`
- 如需修改，编辑 `photo_transform.py` 中的 `PICLIST_URL`。

### 文件路径

- 图片路径应相对于 Markdown 文件所在目录。
- 支持子文件夹，如 `assets/image.png`。

## 注意事项

- **PicList 服务**：确保 PicList 服务正在运行，否则上传会失败。
- **图片路径**：图片必须存在于本地，且路径正确。相对路径会自动解析。
- **网络**：上传需要网络连接，图床配置正确。
- **备份**：处理前建议备份原文件。
- **兼容性**：仅支持 Markdown 格式文件。

## 故障排除

- **"连接 PicList 出错"**：检查 PicList 是否启动，端口是否正确。
- **"文件不存在"**：检查图片路径是否正确，可能需要 URL 解码。
- **上传失败**：检查图床配置和网络。

## 贡献

欢迎提交 Issue 和 Pull Request 来改进工具。

## 许可证

MIT License