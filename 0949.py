n, na1, na2 = map(int, input().split())
s1 = na1
s2 = na2
for i in range(n-1):
	temp = s1
	s1 = s2 - s1
	s2 = temp
print(s1, s2)
