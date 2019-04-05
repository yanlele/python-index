import numpy as np

# 创建一维数组
print('创建一维数组')
print(np.array([1, 2, 3]))
print()

# 创建二维数组
print('创建二维数组')
print(np.array([
    (1, 2, 3),
    (4, 5, 6)]))
print()

# 创建全部为0 的二位数组
print('创建全部为0 的二位数组')
print(np.zeros((3, 4)))
print()

# 创建一个全部为1的三维数组
print('创建一个全部为1的三维数组')
print(np.ones((2, 3, 4)))
print()

"""
创建一维等差数组
第一个参数是起始数
第二个参数是结束数
第三个参数是等差项

如果只有一个参数， 那就是从零开始
"""
print('创建一维等差数组')
print(np.arange(5))
print(np.arange(1, 10, 3))
print()

# 创建二位等差数组
print('创建二位等差数组')
print(np.arange(6).reshape(2, 3))
print()

# 创建单位矩阵（二位数组）
print('创建单位矩阵（二位数组）')
print(np.eye(3))
print()

# 创建等间隔的一维数组
print('创建等间隔的一维数组')
print(np.linspace(1, 10, num=6))
print()

# 创建随机的二维数组
print('创建随机的二维数组')
print(np.random.rand(2, 3))
print()

"""
创建二维随机整数数组（数值小于5）
后面的size 是 几维 几秩
"""
print('创建二维随机整数数组（数值小于5）')
print(np.random.randint(5, size=(2, 3)))
print()

# 根据自定义函数创建数组
print('根据自定义函数创建数组')
print(np.fromfunction(lambda i, j: i + j, (3, 3)))
print()
