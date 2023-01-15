x, y = map(int, input().split())
if (x <= 1 and y <= 1):
	print(0)
else:
	if(x==y):
		print(2)
	else:
		print(1)

