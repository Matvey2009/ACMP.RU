nk = dk = 0
n = list(input())
for i in range(len(n)):
	if (i % 2 == 0):
		dk += int(n[i])
	else:
		nk += int(n[i])
if (abs(nk - dk) % 11 == 0):
	print("YES")
else:
	print("NO")
