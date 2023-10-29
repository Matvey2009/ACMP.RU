n = input()
k = -1
for i in range(1, len(n)+1):
	k += 2**(i-1)
print(k)
