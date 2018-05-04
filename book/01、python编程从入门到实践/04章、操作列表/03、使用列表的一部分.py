# 遍历切片
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# for player in players[:3]:
#     print(player)


# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)
print('当我们做出改变的情况的时候')
friend_foods.pop()
print(my_foods)
print(friend_foods)