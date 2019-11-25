a = 4
b = a
c = a
for i in range(1, a + 1):
    print(" " * (b - 1) + "*" * (2 * i - 1))
    b -= 1
    if i == a:
        for y in range(1, a):
            print(" " * y + "*" * (2 * c - 3))
            c -= 1
