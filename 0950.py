n = input()
arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
k = 0
m = ''
for i in n:
	if i == "0":
		k += 1
	else:
		m += arr[k]
		k = 0			
print(m)
