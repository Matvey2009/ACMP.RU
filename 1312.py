k = input()
i = t = 0
n = -1
while t != n:
	i += 1
	t = 2**i
	print(k[-len(str(t)):len(k)], t, i)
	if (int(k[-len(str(t)):len(k)]) == t):
		print(i)
		break
