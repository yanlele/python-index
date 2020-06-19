import time

n = int(input("请输入要求累加到的数："))

start = time.process_time()

print(n * (n + 1) / 2)

end = time.process_time()
print(end - start)
