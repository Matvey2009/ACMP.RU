n = int(input())
s = 0
for i in bin(n):
	if (i == "1"):
		s += 1
print(s)
