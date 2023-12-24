n, m, k = list(map(int, input().split()))
arr = [[0]*(m+2) for i in range(n+2)]
for i in range(k):
	x, y = map(int, input().split())
	arr[x][y] = 10
	arr[x-1][y-1]=arr[x-1][y-1]+1#-1-1
	arr[x-1][y]=  arr[x-1][y]+1#-10
	arr[x-1][y+1]=arr[x-1][y+1]+1#-1+1
	arr[x][y-1]=  arr[x][y-1]+1#0-1
	arr[x][y+1]=  arr[x][y+1]+1#0+1
	arr[x+1][y-1]=arr[x+1][y-1]+1#+1-1
	arr[x+1][y]=  arr[x+1][y]+1#+10
	arr[x+1][y+1]=arr[x+1][y+1]+1#+1+1
for i in range(1, n+1):
	c = ""
	for j in range(1, m+1):
		if arr[i][j] >= 10:
			c += "*"
		elif arr[i][j] == 0:
			c+= "."
		else:
			c+=str(arr[i][j])
	print(c)
