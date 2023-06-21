n, m = map(int, input().split())
arr = []
for i in range(m):
	arr.append(n//m)
if (n % m == 0):
	print(*arr)
else:
	for i in range(n%m):
		arr[-i-1] += 1
	print(*arr)
