n, w, d, p = map(int, input().split())
if (w*n*(n-1)//2-p)>0:
	print((w*n*(n-1)//2-p)//d)
else:
	print(n)
