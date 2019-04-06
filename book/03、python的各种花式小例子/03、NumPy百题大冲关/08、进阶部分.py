import numpy as np

# 51. 创建一个 5x5 的二维数组，其中边界值为1，其余值为0
print('51. 创建一个 5x5 的二维数组，其中边界值为1，其余值为0')
Z = np.ones((5, 5))
Z[1:-1, 1:-1] = 0
print(Z)
print()

# 52. 使用数字 0 将一个全为 1 的 5x5 二维数组包围
print('52. 使用数字 0 将一个全为 1 的 5x5 二维数组包围')
Z = np.ones((5, 5))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
print(Z)
print()

# 53. 创建一个 5x5 的二维数组，并设置值 1, 2, 3, 4 落在其对角线下方
print('53. 创建一个 5x5 的二维数组，并设置值 1, 2, 3, 4 落在其对角线下方')
Z = np.diag(1 + np.arange(4), k=-1)
print(Z)
print()

print('创建一个 5x5 的二维数组，并设置值 1, 2, 3, 4 落在其对角线线')
Z = np.diag(1 + np.arange(4))
print(Z)
print()

# 54. 创建一个 10x10 的二维数组，并使得 1 和 0 沿对角线间隔放置
print('54. 创建一个 10x10 的二维数组，并使得 1 和 0 沿对角线间隔放置')
Z = np.zeros((10, 10), dtype=int)
Z[1::2, ::2] = 1
Z[::2, 1::2] = 1
print(Z)
print()

# 55. 创建一个 0-10 的一维数组，并将 (1, 9] 之间的数全部反转成负数
print('55. 创建一个 0-10 的一维数组，并将 (1, 9] 之间的数全部反转成负数')
Z = np.arange(11)
Z[(1 < Z) & (Z <= 9)] *= -1
print(Z)
print()

# 56. 找出两个一维数组中相同的元素
print('56. 找出两个一维数组中相同的元素')
Z1 = np.random.randint(0, 10, 10)
Z2 = np.random.randint(0, 10, 10)
print('Z1: ', Z1)
print('Z2: ', Z2)
print(np.intersect1d(Z1, Z2))
print()

# 使用 NumPy 打印昨天、今天、明天的日期
print('使用 NumPy 打印昨天、今天、明天的日期')
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
today = np.datetime64('today', 'D')
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print("yesterday: ", yesterday)
print("today: ", today)
print("tomorrow: ", tomorrow)
print()

# 58. 使用五种不同的方法去提取一个随机数组的整数部分
print('58. 使用五种不同的方法去提取一个随机数组的整数部分')
Z = np.random.uniform(0, 10, 10)
print("原始值: ", Z)

print("方法 1: ", Z - Z % 1)
print("方法 2: ", np.floor(Z))
print("方法 3: ", np.ceil(Z) - 1)
print("方法 4: ", Z.astype(int))
print("方法 5: ", np.trunc(Z))
print()

# 59. 创建一个 5x5 的矩阵，其中每行的数值范围从 1 到 5
print('59. 创建一个 5x5 的矩阵，其中每行的数值范围从 1 到 5')
Z = np.zeros((5, 5))
Z += np.arange(1, 6)
print(Z)
print()

# 60. 创建一个长度为 5 的等间隔一维数组，其值域范围从 0 到 1，但是不包括 0 和 1
print('60. 创建一个长度为 5 的等间隔一维数组，其值域范围从 0 到 1，但是不包括 0 和 1')
Z = np.linspace(0, 1, 6, endpoint=False)[1:]
print(Z)
print()

# 61. 创建一个长度为10的随机一维数组，并将其按升序排序
Z = np.random.random(10)
Z.sort()
print(Z)
print()

print()
