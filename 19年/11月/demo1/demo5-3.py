import re

input_arr = input("")
match_arr = re.match(r'^([\[])(.*)([\]])', input_arr)

arr = [int(n) for n in match_arr.group(2).split(",")]

n = len(arr)
for i in range(n):
    for j in range(0, n - i - 1):

        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)
