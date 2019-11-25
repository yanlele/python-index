A = [30, 64, 72, 49, 30, 50, 72, 30, 16, 62]

for i in range(len(A)):

    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]

print(A)
