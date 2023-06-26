arr = list(map(int, input().split()))
chet = []
nche = []
for i in range(len(arr)):
	if(i%2!=0):
		chet.append(arr[i])
	else:
		nche.append(arr[i])
print(max(chet) + min(nche))
