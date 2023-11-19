n = int(input())
arr = [int(input()) for i in range(n)]
arr.sort()

if n < 3:
	print(sum(arr))
else:
	l, r = n-3, n-1
	s = t = arr[r-1]+arr[r]
	while l >= 0:
		while arr[l]+arr[l+1]<arr[r]:
			t-=arr[r]
			r-=1
		t+=arr[l]
		l-=1
		s = max(s, t)
	print(s)
