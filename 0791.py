n = int(input())
arr = []
if (n > 8):
	arr.append(n-8)
if ((n % 8 != 1)):
	arr.append(n-1)
if (n % 8 != 0):
	arr.append(n+1)
if (n <= 56):
	arr.append(n+8)
print(*arr)
