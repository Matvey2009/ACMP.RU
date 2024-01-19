n, m = map(int, input().split())
t = list(map(int, input().split()))
res = -1
t.pop(0)
q = []
arr = [[False for i in range(m)] for i in range(n)]
for i in range(0, len(t), 2):
	q.append([t[i]-1, t[i+1]-1])
	arr[t[i]-1][t[i+1]-1] = True
while len(q) > 0:
	res+=1
	t = []
	for i in q:
		if i[0] > 0 and not arr[i[0]-1][i[1]]:#в
			arr[i[0]-1][i[1]] = True
			t.append([i[0]-1, i[1]])
		if i[1] > 0 and not arr[i[0]][i[1]-1]:#л
			arr[i[0]][i[1]-1] = True
			t.append([i[0], i[1]-1])
			
		if i[1] < m-1 and not arr[i[0]][i[1]+1]:#п
			arr[i[0]][i[1]+1] = True
			t.append([i[0], i[1]+1])
		
		if i[0] < n-1 and not arr[i[0]+1][i[1]]:#н
			arr[i[0]+1][i[1]] = True
			t.append([i[0]+1, i[1]])
			
	q = t
print(res)
"""
5 5
2 1 1 5 5
"""
