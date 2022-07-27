n = int(input())
arr = list(map(int, input().split()))
m = int(input())
h = []
for l in range(m):
	s = []
	i, j = map(int, input().split())
	for k in range(i, j+1):
		s.append(arr[k-1])
	h.append(s)
for i in h:
	print(*i)
