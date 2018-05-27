"""调整尺寸以适合屏幕"""

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 只要程序处于活动状态，就可以不断地模拟随机漫步
while True:
    #  创建一个 RandomWalk 实例，并将其包含的点都绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()

    #  设置绘图窗口的尺寸
    # 函数 figure() 用于指定图表的宽度、高度、分辨率和背景色。你需要给形参 figsize 指定一个元组，向 matplotlib 指出绘图窗口的尺寸，单位为英寸。
    # Python 假定屏幕分辨率为 80 像素 / 英寸，如果上述代码指定的图表尺寸不合适，可根据需要调整其中的数字。如果你知道自己的系统的分辨率，可使用形参 dpi 向 figure() 传递该分辨率，以有效地利用可用的屏幕空间，
    # 比如：plt.figure(dpi=128, figsize=(10, 6))
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))

    # 但绘制很多点时，黑色轮廓可能会粘连在一起。要删除数据点的轮廓，可在调用 scatter() 时传递实参 edgecolor='none'
    # 可传递参数 c ，并将其设置为一个元组，其中包含三个 0~1 之间的小数值，它们分别表示红色、绿色和蓝色分量。
    # 我们将参数 c 设置成了一个 y  值列表，并使用参数 cmap 告诉 pyplot 使用哪个颜色映射。这些代码将 y  值较小的点显示为浅蓝色，并将 y  值较大的点显示为深蓝色
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    plt.show()

    keep_running = input('是否创建其他的随机漫步？ （y/n） ')
    if keep_running == 'n':
        break
