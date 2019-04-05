import numpy as np

# 生成示例数组
a = np.array((
    [1, 4, 3],
    [6, 2, 9],
    [4, 7, 2]))
print('生成示例数组')
print(a)
print()

# 返回每列最大值
print('返回每列最大值')
print(np.max(a, axis=0))
print()

# 返回每行最大值
print('返回每行最大值')
print(np.max(a, axis=1))
print()

# 返回每行最下值
print('返回每行最下值')
print(np.min(a, axis=1))
print()

# 返回每列最大值索引
print('返回每列最大值索引')
print(np.argmax(a, axis=0))
print()

# 返回每行最小值索引
print('返回每行最小值索引')
print(np.argmin(a, axis=1))
print()







