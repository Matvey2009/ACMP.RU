n, m, k = map(int, input().split())
print((m // k + min(m, k - 1))*n)
