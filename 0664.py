k, m, n = map(int, input().split())
s = 0
while n > 0:
	n -= k
	s += m*2
print(max((2 , (n * 2 + k - 1) / k) * m))
