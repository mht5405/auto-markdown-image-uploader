import re
import os
import requests
import json
import urllib.parse
import sys

# 配置参数
# SOURCE_FILE = '/Users/liuhuahui/Nutstore Files/md_ducument/01.日志/01.bloggers/2026/202601/20260118_obsidian 邪修用法.md'  # 待处理的文件
SOURCE_FILE = ''
PICLIST_URL = 'http://127.0.0.1:36677/upload' # PicList 默认服务地址

def upload_to_piclist(file_path):
    """调用 PicList API 上传图片"""
    try:
        # PicList 接受的格式，具体参考官方文档
        res = requests.post(PICLIST_URL, json={"list": [file_path]})
        data = res.json()
        if data.get('success'):
            return data['result'][0] # 返回图床链接
        else:
            print(f"上传失败: {file_path}, 原因: {data}")
    except Exception as e:
        print(f"连接 PicList 出错: {e}")
    return None

def process_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 匹配 Markdown 图片语法: ![alt](path)
    # 这个正则会捕获路径部分
    img_reg = r'!\[.*?\]\((.*?)\)'
    img_paths = re.findall(img_reg, content)

    # 记录替换映射
    replace_map = {}
    
    # 获取当前 MD 文件的绝对路径，用于定位本地图片
    md_dir = os.path.dirname(os.path.abspath(file_path))

    for path in img_paths:
        # 排除已经是 http 开头的网络图片
        if path.startswith('http'):
            continue
        
        # 转换为本地绝对路径 (处理 Typora 的相对路径)
        abs_path = os.path.normpath(os.path.join(md_dir, urllib.parse.unquote(path)))
        
        if os.path.exists(abs_path):
            print(f"正在上传: {path}...")
            web_url = upload_to_piclist(abs_path)
            if web_url:
                replace_map[path] = web_url
                print(f"成功: {web_url}")
        else:
            print(f"跳过: 文件不存在 {abs_path}")

    # 替换内容
    new_content = content
    for local_path, web_url in replace_map.items():
        new_content = new_content.replace(local_path, web_url)

    # 生成新文件
    md_dir = os.path.dirname(file_path)
    upload_dir = os.path.join(md_dir, 'upload')
    os.makedirs(upload_dir, exist_ok=True)
    base_name = os.path.basename(file_path).replace('.md', '')
    new_file_name = os.path.join(upload_dir, base_name + '_upload.md')
    with open(new_file_name, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"\n处理完成！发布稿已生成: {new_file_name}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_to_process = sys.argv[1]
    else:
        file_to_process = SOURCE_FILE
    process_md(file_to_process)
