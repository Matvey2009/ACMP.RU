n, k = map(int, input().split())
bi, c, m = str(), 0, 1 
while n > 0:
	bi, n = bi+str(n%k), n//k
for i in bi[::-1]:
	c, m = c+int(i), m*int(i)
print(m-c)
