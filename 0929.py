N = int(input())
print(N // 6 + int(N % 6 > 0) * 7 - N % 6, N * 6)