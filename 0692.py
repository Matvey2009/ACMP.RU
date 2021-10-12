N = int(input())
T = 1
R = 'NO'
while N >= T:
    if N == T:
        R = 'YES'
        break
    T *= 2
print(R)