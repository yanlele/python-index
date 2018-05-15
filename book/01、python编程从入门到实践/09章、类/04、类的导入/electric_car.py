from single_car import Car

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
