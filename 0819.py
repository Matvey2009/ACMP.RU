A, B, C = map(int, input().split())
O = A * B * C
S = (A * B + B * C + C * A) * 2
print(S, O)