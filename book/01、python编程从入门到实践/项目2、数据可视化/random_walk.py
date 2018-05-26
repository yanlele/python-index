from random import choice

class RandomWalk():
    """ 一个生成随机漫步数据的类 """
    def __init__(self, num_point=5000):
        """初始化随机漫步的属性"""
        self.num_point = num_point

        # 所有随机漫步都开始于（0，0）
        self.x_value = [0]
        self.y_value = [0]

