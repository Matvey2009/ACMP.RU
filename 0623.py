n = int(input())
a = b = 1
for i in range(n%60-1):
	a, b = b, (a+b)%10
print(b)
