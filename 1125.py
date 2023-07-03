n = int(input())
arr = []
for i in range(1, n):
	if(i**2>n):
		break
	else:
		arr.append(i**2)
print(*arr)
