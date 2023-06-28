arra = []
arrb = []
a, b = input().split()
if (len(a) != len(b)):
	print("No")
else:
	for i in a.lower():
		arra.append(i)
	for i in b.lower():
		arrb.append(i)
	arra.sort()
	arrb.sort()
	if(arra == arrb):
		print("Yes")
	else:
		print("No")

