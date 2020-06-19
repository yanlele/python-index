import time

n = int(input("请输入要求累加到的数："))

start = time.process_time()
sum = 0
for i in range(n + 1):  # 实际遍历到n
    sum += i
print(sum)
end = time.process_time()
print(end - start)
