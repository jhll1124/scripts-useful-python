# coding = 'utf-8'

import urllib.request
import os


path = 'C:\\Users\\Administrator\\Desktop\\1.txt'
for line in open(path, encoding='utf-8'):
    try:
        urllib.request.urlopen(line)
        print(line)
        # 以下打开
        os.system(f'"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" {line}')
        # 以下保存
        # os.makedirs('./Download', exist_ok=True)
        # response = requests.get(line)
        # filename = None
        # # Check if the response has Content-Disposition header
        # if "Content-Disposition" in response.headers:
        #     header = response.headers["Content-Disposition"]
        #     # Extract the filename from the header
        #     filename = header.split("=")[1].strip("\"")
        # # If filename is not found, use the URL basename as filename
        # if not filename:
        #     filename = os.path.basename(line)
        #
        # with open(f'Download\\{filename}', 'wb') as f:
        #     f.write(data)
    except:
        continue
