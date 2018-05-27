"""给随机漫步点着色"""

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 只要程序处于活动状态，就可以不断地模拟随机漫步
while True:
    #  创建一个 RandomWalk 实例，并将其包含的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    # 但绘制很多点时，黑色轮廓可能会粘连在一起。要删除数据点的轮廓，可在调用 scatter() 时传递实参 edgecolor='none'
    # 可传递参数 c ，并将其设置为一个元组，其中包含三个 0~1 之间的小数值，它们分别表示红色、绿色和蓝色分量。
    # 我们将参数 c 设置成了一个 y  值列表，并使用参数 cmap 告诉 pyplot 使用哪个颜色映射。这些代码将 y  值较小的点显示为浅蓝色，并将 y  值较大的点显示为深蓝色
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    plt.show()

    keep_running = input('是否创建其他的随机漫步？ （y/n） ')
    if keep_running == 'n':
        break
