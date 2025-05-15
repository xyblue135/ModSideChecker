import os
import csv
import shutil
import re

def sanitize_filename(name):
    # 替换 *
    name = name.replace('*', '客户端服务端都需要')
    # 替换其余非法字符
    return re.sub(r'[<>:"/\\|?]', '_', name)

csv_file = 'scan_result.csv'
output_base = '过滤'

with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    headers = next(reader)  # 跳过表头

    for row in reader:
        folder, _, jar_name, side_env = row
        side_env = side_env.strip()

        if not side_env:
            side_env = '未识别'

        safe_side_env = sanitize_filename(side_env)

        source_path = os.path.join(folder, jar_name)
        if not os.path.exists(source_path):
            print(f"未找到文件：{source_path}，跳过。")
            continue

        # 构建目标目录
        target_dir = os.path.join(output_base, folder, safe_side_env)
        os.makedirs(target_dir, exist_ok=True)

        shutil.copy2(source_path, os.path.join(target_dir, jar_name))