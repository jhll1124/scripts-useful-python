import requests
import os

os.makedirs('./Download', exist_ok=True)

path = "C:\\Users\\Administration\\Downloads\\0054177f-9e85-403b-be46-7bc7062783c1_normal.m3u8"
i = 0


def get():
    url = 'https://dtliving-sh.dingtalk.com/live_hp/' + line.strip('\n')
    print(url)
    data = requests.get(url).content
    with open(f'Download\\{i}.ts', mode='wb') as f:
        f.write(data)


for line in open(path, encoding='utf-8'):
    if line.startswith('#'):
        pass
    else:
        get()
        i += 1

# 这是闪记
# https://dtliving-sh.dingtalk.com/live_hp/
# 这是分享的直播
# https://dtliving-sz.dingtalk.com/live_hp/
# 使用时只需要更改m3u8文件路径
