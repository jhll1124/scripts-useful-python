import cv2
import numpy as np
from alive_progress import alive_bar
from copy import deepcopy
import os

# 读取文件
print("路径不要包含中文")
print("白色背景下显示的图像路径：")
path1 = input(">>>")
print("黑色背景下显示的图像路径：")
path2 = input(">>>")
# path1 = "1.jpg"
# path2 = "2.jpg"
img1 = cv2.imread(path1, 0)
img2 = cv2.imread(path2, 0)

"""
算法推导过程
m = (1 - alpha) * 255 + alpha * x
  = 255 - 255alpha + alpha * x
n = (1 - alpha) * 0 + alpha * x
  = alpha * x

m = 255 - 255alpha + n
255alpha = - m + n + 255
alpha = (n - m) / 255 + 1
x = n / alpha
"""

lost = 0


def f(gray1, gray2):
    # 处理一个像素点
    global lost
    gray1 = int(gray1)
    gray2 = int(gray2)
    alpha = (gray2 - gray1) / 255 + 1
    if alpha > 1:
        alpha = 1
        x = (gray1 + gray2) / 2
        lost += 1
    elif alpha == 0:
        x = 128
    else:
        x = round(gray2 / alpha)
    alpha = round(alpha * 255)
    pixel = np.array([x, x, x, alpha], dtype=np.uint8)
    return pixel


# 创建处理后图像的矩阵
a = max([len(img1), len(img2)])
b = max([len(img1[0]), len(img2[0])])
img3 = np.zeros((a, b, 4))

with alive_bar(a * b, force_tty=True) as bar:
    for i in range(a):
        for j in range(b):
            # 分别处理每个像素点
            try:
                g1 = img1[i][j]
            except IndexError:
                g1 = 255
            try:
                g2 = img2[i][j]
            except IndexError:
                g2 = 0
            g3 = deepcopy(f(g1, g2))
            img3[i][j] = g3
            bar()

# 报告和保存结果
print("处理完成，共损失了", lost, "个像素点。图片信息完整度", (1 - lost / (a * b)) * 100, "%")
cv2.imwrite("done.png", img3)
print("已保存到done.png")
os.system("pause")
