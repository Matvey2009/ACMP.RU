K1 = 0
K2 = 0
for i in range(4):
    A, B = input().split()
    K1 += int(A)
    K2 += int(B)

if K1 > K2:
    print(1)
if K1 < K2:
    print(2)
if K1 == K2:
    print('DRAW')