n, c = map(int, input().split())
c+=-1
arr = list()
for i in range(n):
	arr.append(list(map(int, input().split())))
p = 0
f = [c]
q = [c]
while len(q) > 0:
	for i in range(n):
		if arr[q[0]][i] and i not in f:
			p-=-1
			q.append(i)
			f.append(i)
	q.pop(0)
print(p) 
