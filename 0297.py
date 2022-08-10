n = input()
s = 0
for i in n:
	if (i == "0" or i == "6" or i == "9"):
		s += 1
	if (i == "8"):
		s += 2
print(s)
