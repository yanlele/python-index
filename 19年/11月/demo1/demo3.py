a = 4
b = a
c = a
print(" " * (a - 1) + "*")
for i in range(2, a + 1):
    print(" " * (b - 2) + "*" + " " * (2 * i - 3) + "*")
    b -= 1
    if i == a:
        for y in range(2, a):
            print(" " * (y - 1) + "*" + " " * (2 * c - 5) + "*")
            c -= 1
        print(" " * (a - 1) + "*")
