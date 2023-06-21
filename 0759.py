n, m = map(int, input().split())
arr = list(map(int, input().split()))
s = 0
arr.sort()
arr.reverse()
for i in range(n):
	if(arr[i]>0 and m > 0):
		s += arr[i]
		m -= 1
print(s)
