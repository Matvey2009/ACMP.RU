n, m = map(int, input().split())
temp = 999999
arr = []
for i in range(n):
	a = input()
	arr = list(map(int, input().split()))
	if (sum(arr) < temp):
		s = a
		temp = sum(arr)
print(s)
