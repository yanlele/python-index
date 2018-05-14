# 类的创建
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        print(self.name.title() + ' rolled over!')


my_dog = Dog('hillie', 6)
print('my dog name is ' + my_dog.name.title() + ' .')
print('my dog age is ' + str(my_dog.age)+ 'yours lod')
my_dog.sit()
my_dog.roll_over()


