import os
names = os.listdir('G:\\Model\\Live2D\\白草净华\\02 模型文件\\__other__\\胡桃x纳西妲\\sounds')
name = []
for i in names:
    i0 = i.strip('.wav')
    name.append(i0)
output = []
for i in name:
    otp = f'''\n        {{
          "File": "motions/touch.motion3.json",
          "Sound": "sounds/{i}.wav",
          "SoundVolume": 0.919,
          "Text": "{i}",
          "FadeIn": 1000,
          "FadeOut": 1000
---分界线---
          "TimeLimit": {{
            "Hour": 12,
            "Minute": 0,
            "Sustain": 180
          }}
---分界线---
        }},'''

    with open("test.txt", "a") as f:
        f.write(otp)  # 自带文件关闭功能，不需要再写f.close()
