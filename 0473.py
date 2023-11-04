n = int(input())
a = b = 1
for i in range(n):
    a, b = b, (a+b)
print(a**2)
