A1, A2, A3 = map(int, input().split())
if A1 + A2 == A3 or A2 + A3 == A1 or A3 + A1 == A2:
    print('YES')
else:
    print('NO')
