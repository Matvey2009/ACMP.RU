n = int(input())
arr = []
s = 0
for i in range(n):
	arr.append(list(map(int, input().split())))
	for j in range(n):
		if (arr[i][j] == 1):
			s += 1
print(s//2)
