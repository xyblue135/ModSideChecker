import zipfile
import os
import csv

folders = ['forge', 'neoforge', 'fabric']
csv_file = 'scan_result.csv'

with open(csv_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # 写表头
    writer.writerow(['文件夹', '包含 neoforge.mods.toml', 'jar 文件名'])

    for folder in folders:
        if not os.path.isdir(folder):
            print(f"目录 {folder} 不存在，跳过。")
            continue

        jars = [f for f in os.listdir(folder) if f.endswith('.jar')]

        for jar in jars:
            jar_path = os.path.join(folder, jar)
            try:
                with zipfile.ZipFile(jar_path, 'r') as z:
                    if 'META-INF/neoforge.mods.toml' in z.namelist():
                        writer.writerow([folder, '是', jar])
                    else:
                        writer.writerow([folder, '否', jar])
            except zipfile.BadZipFile:
                print(f"{jar_path} 不是有效的zip文件，跳过。")