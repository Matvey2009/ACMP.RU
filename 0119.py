arr = []
n = int(input())
for i in range(n):
	tarr = []
	tarr = list(map(int, input().split()))
	at = tarr[2] + tarr[1]*60 + tarr[0]*60*60
	arr.append(at)
arr.sort()
for i in range(n):
	print(arr[i]//3600, arr[i]//60%60, arr[i]%60)
