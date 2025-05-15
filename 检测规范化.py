import zipfile
import os
import csv
import json
import re

folders = ['forge', 'neoforge', 'fabric']
csv_file = 'scan_result.csv'

def extract_side_raw(content: str):
    """只提取 side = "..." 的原始内容"""
    match = re.search(r'side\s*=\s*"([^"]*)"', content)
    return match.group(1) if match else ''

def extract_environment_raw(content: str):
    """只提取 environment = "..." 的原始内容"""
    try:
        data = json.loads(content)
        return data.get("environment", "")
    except Exception:
        return ''

with open(csv_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['文件夹', '标志文件存在', 'jar 文件名', 'side / environment 原文'])

    for folder in folders:
        if not os.path.isdir(folder):
            print(f"目录 {folder} 不存在，跳过。")
            continue

        jars = [f for f in os.listdir(folder) if f.endswith('.jar')]

        for jar in jars:
            jar_path = os.path.join(folder, jar)
            try:
                with zipfile.ZipFile(jar_path, 'r') as z:
                    found = '否'
                    value = ''

                    if folder == 'forge':
                        path = 'META-INF/mods.toml'
                        if path in z.namelist():
                            found = '是'
                            with z.open(path) as f_mod:
                                content = f_mod.read().decode('utf-8', errors='ignore')
                                value = extract_side_raw(content)

                    elif folder == 'neoforge':
                        path = 'META-INF/neoforge.mods.toml'
                        if path in z.namelist():
                            found = '是'
                            with z.open(path) as f_mod:
                                content = f_mod.read().decode('utf-8', errors='ignore')
                                value = extract_side_raw(content)

                    elif folder == 'fabric':
                        path = 'fabric.mod.json'
                        if path in z.namelist():
                            found = '是'
                            with z.open(path) as f_json:
                                content = f_json.read().decode('utf-8', errors='ignore')
                                value = extract_environment_raw(content)

                    writer.writerow([folder, found, jar, value])
            except zipfile.BadZipFile:
                print(f"{jar_path} 不是有效的 zip 文件，跳过。")
