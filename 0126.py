n = int(input())
arr = list()
for i in range(n):
	arr.append(list(map(int, input().split())))
m = 999999
for i in range(n):
	for j in range(i+1, n):
		for k in range(j+1, n):	
			m = min(m, arr[i][j]+ arr[j][k] + arr[k][i])
print(m)
