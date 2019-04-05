import numpy as np

# 生成一个随机的二维数组
a = np.random.random((3, 2))
print('生成一个随机的二维数组')
print(a)
print()

# 查看数组形状
print('查看数组形状')
print(a.shape)
print()

# 更改数组形状（不改变原始数组）
print('更改数组形状（不改变原始数组）')
print(a.reshape(2, 3))
print(a)
print()

# 更改数组形状（改变原始数组）
print('更改数组形状（改变原始数组）')
# 这个地方没有输出
a.resize(2, 3)
print(a)
print()

# 展平数组
print('展平数组')
print(a.ravel())
print(a)
print()

# 垂直拼合数组
print('垂直拼合数组')
a = np.random.randint(10, size=(3, 3))
b = np.random.randint(10, size=(3, 3))
print(a)
print(b)
print('合并')
print(np.vstack((a, b)))
print()

# 水平拼合数组
print('水平拼合数组')
print(np.hstack((a, b)))
print()

# 沿横轴分割数组
print('沿横轴分割数组')
print(np.hsplit(a, 3))
print()

# 沿纵轴分割数组
print('沿纵轴分割数组')
print(np.vsplit(a, 3))
print()


