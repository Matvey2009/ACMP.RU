m, n, i, j, c = map(int, input().split())
if (not m & 1) or (not n & 1):
	print("equal")
elif ((i + j) & 1 and c == 1) or (not(i + j) & 1 and c == 0):
	print("black")
else:
	print("white")
