n, c, f = map(int, input().split())
arr = list()
d = list()
for i in range(n):
	arr.append(list(map(int, input().split())))
	d.append(10000)
c, f = c-1, f-1
d[c] = 0
q = [c]
while len(q) > 0:
	for i in range(n):
		if arr[q[0]][i] > 0 and d[i] > d[q[0]] + arr[q[0]][i]:
			q.append(i)
			d[i] = d[q[0]] + arr[q[0]][i]
	q.pop(0)
if d[f] < 10000:
	print(d[f])
else:
	print(-1)
