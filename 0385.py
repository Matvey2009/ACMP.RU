n = int(input())
arr = []
res = []
for i in range(n):
	arr.append(list(map(int, input().split())))
for i in range(n):
	for j in range(n):
		if arr[i] != arr[j]:
			res.append((abs(arr[i][0]-arr[j][0])**2 + abs(arr[i][1]-arr[j][1])**2)**0.5)
res = list(set(res))
res.sort()
print(len(res))
for i in res:
	print(i)
