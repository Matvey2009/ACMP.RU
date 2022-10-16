n, m = map(int, input().split())
arr = []
s = 0
for i in range(n):
	arr.append(input())
input()
for i in range(n):
	g = input()
	for j in range(m):
		if arr[i][j] == g[j]:
			s += 1
print(s)
