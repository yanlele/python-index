class Test():
    def __init__(self):
        print('init')

    def get_name(self):
        print('我要用到name')
        self.name()

    def name(self):
        print('我的名字是123')
