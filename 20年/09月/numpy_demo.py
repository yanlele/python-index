import numpy as np  # 引入numpy库
import datetime


def add(n):
    a = []
    b = []
    c = []
    for i in range(n):
        a.append(i ** 2)
        b.append(i + 3)
        c.append(a[i] + b[i])
    return c


def np_add(n):
    a = np.arange(n) ** 2
    b = np.arange(n) + 3
    c = a + b


N = 1000000

starttime = datetime.datetime.now()
add(N)
endtime = datetime.datetime.now()
seconds = (endtime - starttime).microseconds
print("add(N) - 消耗时间： ", seconds)


starttime = datetime.datetime.now()
np_add(N)
endtime = datetime.datetime.now()
seconds = (endtime - starttime).microseconds
print("np_add(N) - 消耗时间： ", seconds)

