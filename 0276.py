n, m = map(int, input().split())
k = n // m
t = n % m
arr = []
for i in range(m-t):
	arr.append(k)
for i in range(m-k):
	arr.append(t)
arr.sort()
print(*arr)
