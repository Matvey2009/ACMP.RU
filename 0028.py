x1, y1, x2, y2 = map(int, input().split())
xa, ya = map(int, input().split())
if (x1 == x2):
	xb = x1-(xa-x1)
	yb = ya
else:
	xb = xa
	yb = y1-(ya-y1)
print(xb, yb)

