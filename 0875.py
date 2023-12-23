n, m, k  = map(int, input().split())
arr = []
for i in range(n):
	c = input()
	for j in range(m):
		if c[j] == "*":
			arr.append([i, j])
for _ in range(k):
	mtx = [[0]*m for i in range(n)]
	for i in arr:
		mtx[i[0]][i[1]]+=10
		mtx[(i[0]-1+n)%n][(i[1]-1+m)%m]+=1
		mtx[(i[0]-1+n)%n][i[1]]+=1
		mtx[(i[0]-1+n)%n][(i[1]+1+m)%m]+=1
		mtx[i[0]][(i[1]-1+m)%m]+=1
		mtx[i[0]][(i[1]+1+m)%m]+=1
		mtx[(i[0]+1+n)%n][(i[1]-1+m)%m]+=1
		mtx[(i[0]+1+n)%n][i[1]]+=1
		mtx[(i[0]+1+n)%n][(i[1]+1+m)%m]+=1
	arr = []
	for i in range(n):
		for j in range(m):
			if mtx[i][j] == 3 or (mtx[i][j] > 11 and mtx[i][j] < 14):
				arr.append([i, j])
mtx = [['.']*m for i in range(n)]
for i in arr:
	mtx[i[0]][i[1]]='*'
for i in range(n):
	print(''.join(mtx[i]))

'''
n, m, k  = map(int, input().split())
arr = []
for i in range(n):
	arr.append(list(input()))
for _ in range(k):
	tmp = [['.']*m for i in range(n)]
	for i in range(n):
		for j in range(m):
			t = 0
			if arr[(i-1+n)%n][(j-1+m)%m] == "*":
				t+=1
			if arr[(i-1+n)%n][j] == "*":
				t+=1
			if arr[(i-1+n)%n][(j+1+m)%m] == "*":
				t+=1
			if arr[i][(j-1+m)%m] == "*":
				t+=1
			if arr[i][(j+1)%m] == "*":
				t+=1
			if arr[(i+1+n)%n][(j-1+m)%m] == "*":
				t+=1
			if arr[(i+1+n)%n][j] == "*":
				t+=1
			if arr[(i+1+n)%n][(j+1+m)%m] == "*":
				t+=1
			if (arr[i][j] == "*" and t > 1 and t < 4) or (not arr[i][j] == "*" and t == 3):
				tmp[i][j] = "*"
			else:
				tmp[i][j] = "."
	arr = tmp
for i in range(n):
	print(''.join(arr[i]))
'''
