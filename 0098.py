n = int(input())
arr = list(map(int, input().split()))
p = v = 0
for i in range(n):
	print(i, arr[i], n - i - 1, arr[n - i - 1])
	if(arr[i] >= arr[n - i - 1]):
		if (i % 2 != 0):
			p += arr[i]
		else:
			v += arr[i]
		#arr.pop(i)
	else:
		if (i % 2 != 0):
			p += arr[n - i - 1]
		else:
			v += arr[n - i - 1]
		p += arr[n - i - 1]
		#arr.pop(n - i - 1)
print(p,":",v)
