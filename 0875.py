n, m, k  = map(int, input().split())
arr = list()
for i in range(n):
	arr.append(list(input()))
for _ in range(k):
	le = [""]*n
	print(le)
	print()
	for i in range(n):
		le[i].append([]*m)
	for i in range(n):
		for j in range(m):
			#n, m = n-1, n-1
			t = 0
			if arr[i*n%n-1][j*n%n-1] == "*":#-1 -1
				t+=1
			if arr[i*n%n][j*n%n-1] == "*":#0 -1
				t+=1
			if arr[i*n%n+1][j*n%n-1] == "*":#+1 -1
				t+=1
			if arr[i*n%n-1][j*n%n] == "*":#-1 0
				t+=1
			if arr[i*n%n+1][j*n%n] == "*":#+1 0
				t+=1
			if arr[i*n%n-1][j*n%n+1] == "*":#-1 +1
				t+=1
			if arr[i*n%n][j*n%n+1] == "*":#0 +1
				t+=1
			if arr[i*n%n+1][j*n%n+1] == "*":#+1 +1
				t+=1
			if (t == 3) or (t > 1 and t < 4 and arr[i][j] == "*"):
				le[i][j] == "*"
			else:
				le[i][j] == "."
	arr = le.copy()
for i in range(n):
	print(*le[i])
		
