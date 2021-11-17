N = int(input())
temp = 0
for i in input().split():
    temp += 1
    if int(i) <= 437:
        print('Crash', temp)
        N = 0
        break
if N:
    print('No crash')