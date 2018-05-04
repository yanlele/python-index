import math
# 切片
arr = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
print('前三个元素为： ', arr[:3])
print('中间三个元素为： ', arr[math.floor(len(arr)/2)-1:math.ceil(len(arr)/2)+1])
print('最后三个元素为： ', arr[-3:])

# 你的比萨和我的比萨
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('好吃的品种')
friend_foods.append('一般的味道')
for item in my_foods:
    print('我的实物有：', item)
for item in friend_foods:
    print('朋友的食物有： ', item)