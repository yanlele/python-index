import numpy as np

# 生成一位示例数组
a = np.array([10, 20, 30, 40, 50])
b = np.arange(1, 6)
print('生成一位示例数组')
print(a)
print(b)
print()

# 生成二位数组
print('生成二位数组')
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print('A', A)
print('B', B)
print()

# 三角函数
print('三角函数')
print(np.sin(a))
print()

# 以自然对数函数为底数的指数函数
print('以自然对数函数为底数的指数函数')
print(np.exp(a))
print()

# 数组的方根的运算（开平方）
print('数组的方根的运算（开平方）')
print(np.sqrt(a))
print()

# 数组的方根的运算（立方）
print('数组的方根的运算（立方）')
print(np.power(a, 3))
print()
