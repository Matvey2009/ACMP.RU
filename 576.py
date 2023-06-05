import math
b = 0
n = int(input())
for i in range(1, n):
	if (math.gcd(n, i) == 1):
		b += 1
print(b)
