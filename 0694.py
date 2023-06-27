n = int(input())
arra = []
arrb = []
for i in range(n):
	a, b = map(int, input().split())
	arra.append(a)
	arrb.append(b)
a = max(arra)
b = min(arrb)
if(b >= a):
	print("YES")
else:
	print("NO")
