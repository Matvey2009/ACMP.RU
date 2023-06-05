n, s = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
kol = 0
for i in range(n):
	if (s < arr[i]):
		break
	else:
		kol += 1
		s -= arr[i]
print(kol)
