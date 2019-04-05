import numpy as np

# 生成一位示例数组
a = np.array([10, 20, 30, 40, 50])
b = np.arange(1, 6)
print('生成一位示例数组')
print(a)
print(b)
print()

# 一维数组加法运算
print('一维数组加法运算')
print(a + b)
print()

# 一维数组减法运算
print('一维数组减法运算')
print(a - b)
print()

# 以为数组乘法运算
print('以为数组乘法运算')
print(a * b)
print()

# 以为数组除法运算
print('以为数组除法运算')
print(a / b)
print()

# 生成二位数组
print('生成二位数组')
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print('A', A)
print('B', B)
print()

# 矩阵加法运算
print('矩阵加法运算')
print(A + B)
print()

# 矩阵减法运算
print('矩阵减法运算')
print(A - B)
print()

# 矩阵元素之间乘法运算
print('矩阵元素之间乘法运算')
print(A * B)
print()

# 矩阵乘法运算（注意与上题的区别）
print('矩阵乘法运算（注意与上题的区别）')
print(np.dot(A, B))
print()
print('如果使用 np.mat 将二维数组准确定义为矩阵，就可以直接使用 * 完成矩阵乘法计算')
print(np.mat(A) * np.mat(B))
print()

# 数乘矩阵
print('数乘矩阵')
print(2 * A)
print()

# 矩阵的转置
print('矩阵的转置')
print(A.T)
print()

# 矩阵求逆
print('矩阵求逆')
print(np.linalg.inv(A))
print()


