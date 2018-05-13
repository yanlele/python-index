# 类的创建
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        print(self.name.title() + ' rolled over!')
