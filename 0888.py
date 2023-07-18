n = int(input())
arr = list(map(int, input().split()))
t = s = 0
for i in range(n):
	if arr[i]:
		s += 3+t
		t += 1
	elif t-3>0:
		t-=3
	else:
		t=0
print(s)
