arr = list(map(int, input()))
n = maxn = minn = 1
for i in range(len(arr)):
	if arr[i] == 1:
		n += 1
	else:
		n -= 1
	minn = min(n, minn)
	maxn = max(n, maxn)
print(maxn-minn+1)
