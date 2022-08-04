n, m, y, x = map(int, input().split())
if (y % 2 != 0):
	print((m*(y-1)-1+x))
else:
	print((m*(y-1)+(m-x)))
print()
