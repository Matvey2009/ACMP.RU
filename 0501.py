n = int(input())
arr = list()
c=0
for i in range(n):
	arr.append(list(map(int, input().split())))
x1, y1, x2, y2 = map(int, input().split())
x1, x2 = min(x1, x2), max(x1, x2)
y1, y2 = min(y1, y2), max(y1, y2)
for i in range(len(arr)):
	arr[i][0], arr[i][2] = min(arr[i][0], arr[i][2]), max(arr[i][0], arr[i][2])
	arr[i][1], arr[i][3] = min(arr[i][1], arr[i][3]), max(arr[i][1], arr[i][3])
	px1 = max(x1, arr[i][0])
	py1 = max(y1, arr[i][1])
	px2 = min(x2, arr[i][2])
	py2 = min(y2, arr[i][3])
	c+=max((px2-px1), 0)*max((0, py2-py1))
print(c)
