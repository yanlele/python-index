import numpy as np

# 一维数组索引
a = np.array([1, 2, 3, 4, 5])
print('一维数组索引')
print(a[0])
print(a[-1])
print()

"""
一维数组切片
从开始坐标开始， 到结束坐标之前
"""
print('一维数组切片')
print(a[0:2])
print(a[0:-1])
print()

# 二维数组索引
a = np.array([
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)])
print('二维数组索引')
print(a)
print(a[0])
print(a[-1])
print()

# 二维数组切片
print('二维数组切片')
print(a)
print('取第一行')
print(a[:1, :])
print('取第一二行')
print(a[:2, :])
print('取二三行')
print(a[1:3, :])
print('取第一列')
print(a[:, 1:2])
print(a[:, 1])
print()
