str1 = 'i have an apple'
str2 = 'i have a strawberry'

str_upper1 = str1.upper()
str_upper2 = str2.upper()

res = []
for x in str_upper1:
    if x in str_upper2:
        if not x.isspace():
            res.append(x)

res = list(set(res))
res.sort()
print('in both:')
print(' '.join(res))

res2 = []
for x in str_upper1:
    if x not in str_upper2:
        res2.append(x)

res2 = list(set(res2))
res2.sort()
print('in string 1 not in string 2:')
print(' '.join(res2))

res3 = []
char26 = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
for x in char26:
    if x not in str_upper1:
        if x not in str_upper2:
            res3.append(x)

print(' '.join(res3))
