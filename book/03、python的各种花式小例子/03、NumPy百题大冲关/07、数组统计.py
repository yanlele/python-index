import numpy as np

# 生成示例数组
a = np.array((
    [1, 4, 3],
    [6, 2, 9],
    [4, 7, 2]))
print('生成示例数组')
print(a)
print()

# 统计数组各列的中位数
print('统计数组各列的中位数')
print(np.median(a, axis=0))
print()

# 统计数组各行的算术平均值
print('统计数组各行的算术平均值')
print(np.mean(a, axis=1))
print()

# 统计数组各列的加权平均值
print('统计数组各列的加权平均值')
print(np.average(a, axis=0))
print()

# 统计数组各行的方差
print('统计数组各行的方差')
print(np.var(a, axis=1))
print()

# 统计数组各列的标准偏差
print('统计数组各列的标准偏差')
print(np.std(a, axis=0))
print()



