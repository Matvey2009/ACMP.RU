n = int(input())
arr = list(map(int, input().split()))
s = 0
for i in range(n):
	s = max(arr[i] + arr[(i+1)%n] + arr[(i-1)%n] , s)
print(s)
