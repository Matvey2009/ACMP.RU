a, b = map(int, input().split())
for i in range(a, b+1):
	if str(i*i)[-len(str(i)):] == str(i):
		print(i)
