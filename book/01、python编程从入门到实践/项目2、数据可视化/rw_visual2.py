"""模拟多次随机漫步"""

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 只要程序处于活动状态，就可以不断地模拟随机漫步
while True:
    #  创建一个 RandomWalk 实例，并将其包含的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input('是否创建其他的随机漫步？ （y/n） ')
    if keep_running == 'n':
        break
