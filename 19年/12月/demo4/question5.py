d = int(input())
i = 2

res = []
while d >= i:
    while d % i == 0:
        res.append(str(i))
        d = d / i
    i = i + 1

# 12308760
print(' '.join(res))
