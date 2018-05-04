cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

print('-----------------------')

# 临时排序  这个东西有问题，程序会报错
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars.sorted(cars))
print(cars)