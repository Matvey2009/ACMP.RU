n = int(input())
arr = list()
d = list()#Длина путей Пути
for i in range(n):
	arr.append(list(map(int, input().split())))
	d.append(10000)
c, f = map(int, input().split())
f, c = f-1,c-1
d[c] = 0
q = [c]
while len(q) > 0:
	for i in range(n):
		if arr[q[0]][i] > 0 and d[i] > d[q[0]]+1:
			q.append(i)
			d[i] = d[q[0]]+1#Добовляем расстояние(Не единица, а расстояние просто тут расстояние всегда 1)
	q.pop(0)#Убираем из очереди
if d[f] < 10000:
	print(d[f])
else:
	print(-1)
