n = int(input())
a = b = c = 1
for i in range(n):
	a = (b+c)%10 
	c, b = b, a
print(c)
