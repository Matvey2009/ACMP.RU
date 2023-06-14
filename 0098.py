n = int(input())
arr = list(map(int, input().split()))
p = v = l = 0
r = n-1
for i in range(n):
	#print(i, arr[i], n - i - 1, arr[n - i - 1])#
	if(arr[l] >= arr[r]):
		if (i % 2 == 0):
			p += arr[l]
			#print(arr[l], "Первый начало")
			l += 1
		else:
			v += arr[l]
			#print(arr[l], "Второй начало")
			l += 1
		#arr.pop(i)
	else:
		if (i % 2 == 0):
			p += arr[r]
			#print(arr[r], "Первый последний")
			r -= 1
		else:
			v += arr[r]
			#print(arr[r], "Второй последний")
			r -= 1
		#arr.pop(n - i - 1)
print(str(p)+":"+str(v))
