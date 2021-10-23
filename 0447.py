N = int(input())
S = 1
for i in range(1, N+1):
    S = S * i

while True:
    if S % 10 == 0:
        S = S // 10
    else:
        print(S % 10)
        break
