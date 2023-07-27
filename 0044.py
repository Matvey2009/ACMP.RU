n = input()
s = 0
k = n + "     "
for i in range(len(n)):
	if str(k[i:i+5]) == '>>-->' or k[i:i+5] == '<--<<':
		s += 1
print(s)
