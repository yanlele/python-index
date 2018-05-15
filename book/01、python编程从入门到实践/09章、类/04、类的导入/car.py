""" 一个可用于表示汽车的类 """


class Car():
    """ 一次模拟汽车的简单尝试 """

    def __init__(self, make, model, year):
        """ 初始化描述汽车的属性 """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ 返回整洁的描述性名称 """
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """ 打印一条消息，指出汽车的里程 """
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        拒绝将里程表往回拨
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """ 将里程表读数增加指定的量 """
        self.odometer_reading += miles


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print('这辆车还有：' + str(self.battery_size) + ' 千瓦/时的电量')

    def get_range(self):
        """打印出电瓶续航信息"""
        if self.battery_size == 70:
            range = 240
        if self.battery_size == 85:
            range = 270
        message = '车辆的续航里程为： ' + str(range) + '千米'
        print(message)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
