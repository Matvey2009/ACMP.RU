n = int(input())
arr = list(map(int, input().split()))
s = temp = 0
for i in range(n):
	if arr[i] > 0:
		temp += 1
		s = max(s, temp)
	else:
		temp = 0
print(s)
