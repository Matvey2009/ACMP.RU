import math 
n, n2 = map(int, input().split())
a = b = 1
for i in range(n-2):
	a, b = b, a+b
p = b
a = b = 1
for i in range(n2-2):
	a, b = b, a+b
v = b
print(math.gcd(p, v))

