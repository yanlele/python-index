x = 7
y = 1
i = 1
while i <= x:
    j = 1
    k = 1
    while k <= x - i:
        print(' ' * y, end='')
        k += 1
    while j <= i:
        print('*', end=' ' * (2 * y - 1))
        j += 1
    print('\n')
    i += 2
while i <= 2 * x - 1:
    a = x + 1
    b = 2 * x - 1
    while a <= i:
        print(' ' * y, end='')
        a += 1
    while b >= i:
        print('*', end=' ' * (2 * y - 1))
        b -= 1
    print('\n')
    i += 2
