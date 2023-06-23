k = int(input())
s = 0
for i in range(k+1):
	t = int(str(i)[::-1])
	if(i + t == k):
		s += 1
print(s)
