"""
一.约瑟夫环问题:
已知n个人（以编号1，2，3...n分别表示）
围坐在一张圆桌周围。从编号为k的人开始报数，数到m的那个人出列；
他的下一个人又从1开始报数，数到m的那个人又出列；依此规律重复下去，
直到圆桌周围的人全部出列；输出出列的顺序列表。
"""

# 初始化约瑟夫环
people = []
now_people = []
for i in range(10):
    people.append(i + 1)

now = 4 - 1  # now指定当前报数的人
while len(people):
    now = (now + 3) % len(people) - 1
    if now < 0:
        now_people.append(people[now])
        people.pop(now)
        now = 0
    else:
        now_people.append(people[now])
        people.pop(now)

print(now_people)
