n = int(input())
a = b = 1
for i in range(1200000000):
	a, b = b, (a+b)
	if(n == b):
		print(1)
		print(i+3)
		break
	elif(n < b):
		print(0)
		break
