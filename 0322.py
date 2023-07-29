n = input()
a, b = 1, 2
k = ''
for i in range(len(n)):
	if len(n)<a:
		break
	k+=n[a-1]
	a, b = b, (a+b)
print(k)
