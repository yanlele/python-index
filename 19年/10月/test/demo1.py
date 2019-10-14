# 猜数字

import random

random_number = random.randint(1, 100)
print('## 猜数字游戏 ##')

time = 0
while True:
    input_number = int(input('请输入数字： '))
    if input_number > random_number:
        print('猜的数字太大了')
        time += 1
    elif input_number < random_number:
        print('猜的数字太小了')
        time += 1
    elif input_number == random_number:
        print('恭喜你数字才对了，数字是: %d, 一共猜了: %d 次' % (random_number, time))
        break
