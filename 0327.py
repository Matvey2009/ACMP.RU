k = int(input())
def test(s):
	l = str(s // 1000)
	l = sum(map(int, l))
	r = str(s % 1000)
	r = sum(map(int, r))
	return l == r

for i in range(k):
	s = int(input())
	if test(s+1) or test(s-1):
		print("Yes")
	else:
		print("No")

