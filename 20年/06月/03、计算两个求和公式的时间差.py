import time

n = int(input("请输入要求累加到的数："))

start1 = time.process_time()
sum1 = 0
for i in range(n + 1):  # 实际遍历到n
    sum1 += i
print('sum 普通求和结果', sum1)

end1 = time.process_time()

time1 = end1 - start1

start2 = time.process_time()

print('n * (n + 1) / 2 结果： ', n * (n + 1) / 2)

end2 = time.process_time()
time2 = end2 - start2

print('时间差绝对值： ', abs(time1 - time2))
