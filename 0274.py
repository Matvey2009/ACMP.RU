n = int(input())
for i in range(n):
	a, b = input().split()
	aarr = []
	barr = []
	for j in a:
		aarr.append(j)
	for j in b:
		barr.append(j)
	aarr.sort()
	barr.sort()
	a = "".join(set(aarr))
	b = "".join(set(barr))
	if a == b:
		print("YES")
	else:
		print("NO")
	
