n = int(input())
arr = list()

q = list()#Очередь
d = list()#Длина путей Пути
for i in range(n):
	arr.append(list(map(int, input().split())))
	d.append(10000)
c, f = map(int, input().split())
f -= 1
c -= 1
d[c] = 0
q.append(c)

while len(q) > 0:
	t = q[0]#Номер проверяемой вершины
	q.pop(0)#Убираем из очереди
	for i in range(n):
		if arr[t][i] > 0 and d[i] > d[t]+1:
			q.append(i)
			d[i] = d[t]+1#Добовляем расстояние(Не единица, а расстояние просто тут расстояние всегда 1)
			
if d[f] < 10000:
	print(d[f])
else:
	print(-1)

