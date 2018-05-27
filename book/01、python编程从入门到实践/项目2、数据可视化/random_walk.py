from random import choice


class RandomWalk():
    """ 一个生成随机漫步数据的类 """

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有随机漫步都开始于（0，0）
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        #  不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            #  决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1, -1])  # 我们使用 choice([1, -1]) 给 x_direction 选择一个值，结果要么是表示向右走的 1 ，要么是表示向左走的 -1
            x_distance = choice([0, 1, 2, 3, 4])  # choice([0, 1, 2, 3, 4]) 随机地选择一个 0~4 之间的整数，告诉 Python  沿指定的方向走多远（ x_distance ）
            x_step = x_direction * x_distance   # 我们将移动方向乘以移动距离，以确定沿 x  和 y  轴移动的距离。如果 x_step 为正，将向右移动，为负将向左移动，而为零将垂直移动

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance   # 如果 y_step 为正，就意味着向上移动，为负意味着向下移动，而为零意味着水平移动。

            # 拒绝原地漫步
            if x_step == 0 and y_step == 0:     # 如果 x_step 和 y_step 都为零，则意味着原地踏步，我们拒绝这样的情况，接着执行下一次循环
                continue

            # 计算下一个点的x和y
            next_x = self.x_values[-1] + x_step  # 为获取漫步中下一个点的 x  值，我们将 x_step 与 x_values 中的最后一个值相加
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
