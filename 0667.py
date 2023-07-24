import math
n, m, k = map(int, input().split())
if n/(m/2)<k:
	print(math.ceil((n+m)/k))
else:
	print(0)
