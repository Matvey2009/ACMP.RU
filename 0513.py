import math
n = int(input())
s=0
for i in range(2, n+1):
	s+=math.factorial(n)//(math.factorial(n-i)*math.factorial(i))
print(s)

