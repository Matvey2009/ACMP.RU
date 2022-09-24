n = int(input())
arr = ['A', 'B', 'C', 'E', 'H', 'K', 'M', 'O', 'P', 'T', 'X', 'Y']
arrn = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
for i in range(n):
	s = input()
	if (len(s) == 6 and s[0] in arr and s[4] in arr and s[5] in arr and s[1] in arrn and s[2] in arrn and s[3] in arrn):
		print('Yes')
	else:
		print('No')
