arr = [71, 93, 2, 39, 59, 41, 78, 59, 21, 78]

n = len(arr)
for i in range(n):
    for j in range(0, n - i - 1):

        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)
