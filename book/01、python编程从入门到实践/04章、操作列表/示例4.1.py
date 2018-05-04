for value in range(1, 21):
    print(value)

numList = list(range(1, 1000001))
print(min(numList))
print(max(numList))
print(sum(numList))

odd_numbers = []
for value in range(1, 20, 2):
    odd_numbers.append(value)
print(odd_numbers)

remaining3 = []
for value in range(3, 31, 3):
    remaining3.append(value)
print(remaining3)

cube = []
for value in range(1, 11):
    cube.append(value ** 3)
print(cube)

analysis = [value ** 3 for value in range(1, 11)]
print(analysis)
