"""表示一个骰子的类-模拟掷一个骰子"""

from random import randint

class Die():
    def __init__(self, num_sides=6):
        """骰子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """" 返回一个位于 1 和骰子面数之间的随机值 """
        return randint(1,self.num_sides)

