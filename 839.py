N = input()
for i in range(len(N)):
    if N[i] == '0':
        print('NO')
        N = 0
        break
if N:
    print('YES')