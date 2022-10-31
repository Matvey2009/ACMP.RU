n, m = map(int, input().split())
if (n == 0 and m != 0):
	print("Impossible")
elif (m == 0):
	print(n, n)
else:
	print(max(m, n), n + m - 1)
