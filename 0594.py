arra = []
arrb = []
a = input()
b = input()
if (len(a) != len(b)):
	print("NO")
else:
	for i in a.lower():
		arra.append(i)
	for i in b.lower():
		arrb.append(i)
	arra.sort()
	arrb.sort()
	if(arra == arrb):
		print("YES")
	else:
		print("NO")
