"""
一.约瑟夫环问题:
已知n个人（以编号1，2，3...n分别表示）
围坐在一张圆桌周围。从编号为k的人开始报数，数到m的那个人出列；
他的下一个人又从1开始报数，数到m的那个人又出列；依此规律重复下去，
直到圆桌周围的人全部出列；输出出列的顺序列表。
"""

n = int(input("请输入总人数："))
m = int(input("请输入出局号："))
k = int(input("请输入开始位置："))

# 初始化约瑟夫环
people = []
for i in range(n):
    people.append(i + 1)

print("需要处理的约瑟夫环为：\n", people)
now = k - 1  # now指定当前报数的人
while len(people):
    now = (now + m) % len(people) - 1
    if now < 0:
        print("编号为 %d 的人出局" % people[now])
        people.pop(now)
        now = 0
    else:
        print("编号为 %d 的人出局" % people[now])
        people.pop(now)
