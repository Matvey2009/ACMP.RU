N = int(input())
arr = list(map(int, input().split()))
d1 = []
d2 = []
for i in arr:
	if (i % 2 == 0):
		d2.append(i)
	else:
		d1.append(i)
print(*d1)
print(*d2)
if (len(d1) > len(d2)):
	print("NO")
else:
	print("NO")
