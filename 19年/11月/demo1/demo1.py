n = 1
sum = 1
while n <= 9:
    i = 1
    while i <= n:
        sum = i * n
        print('%d * %d = %d' % (i, n, sum), end='  ')
        i = i + 1
    print('')
    n = n + 1
