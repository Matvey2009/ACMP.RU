A, B, C, T = map(int, input().split())

if T > A:
    S = A * B + (T - A) * C
else:
    S = T * B
print(S)