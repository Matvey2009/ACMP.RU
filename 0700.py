n, v, k = map(int, input().split())
t = s = 0
for i in range(n):
	if (v >= 1):
		s += v
		v -= k
	else:
		print("NO", s)
		t = 1
		break
if (t == 0):
	print("YES", s)
