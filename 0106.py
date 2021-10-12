N = int(input())
S = 0
for i in range(N):
    X = int(input())
    S += X
if N - S > S:
    print(S)
else:
    print(N - S)