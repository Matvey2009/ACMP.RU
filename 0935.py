x1, y1, x2, y2 = map(int, input().split())
if((x1 + y1) % 2 == 0):
	c1 = 1
else:
	c1 = 0
if((x2 + y2) % 2 == 0):
	c2 = 1
else:
	c2 = 0
if (c1 == c2):
	print('YES')
else:
	print('NO')
