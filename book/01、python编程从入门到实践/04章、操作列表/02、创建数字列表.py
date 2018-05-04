# for value in range(1, 5):
#     print(value)
#
#
# numbers = list(range(1,6))
# print(numbers)

# even_numbers = list(range(2,11,2))
# print(even_numbers)

# squares = []
# for value in range(1, 11):
#     squares.append(value ** 2)
# print(squares)

# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))

# squares = [value **2 for value in range(1,11)]
# print(squares)

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
