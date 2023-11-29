n, d = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = 0
left, right = 0, n-1
while left <= right:
	if left == right:
		res+=1
		break
	if arr[left] + arr[right] <= d:
		left+=1
	right-=1
	res+=1
print(res)
