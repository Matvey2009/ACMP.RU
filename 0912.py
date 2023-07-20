n = int(input())
arr = list(map(int, input().split()))
onearr = list(set(arr))
t = 0
for i in range(len(onearr)):
	if arr.count(onearr[i])>t:
		t = int(arr.count(onearr[i]))
		s = onearr[i]
	elif arr.count(onearr[i])==t:
		s = 0
print(s)
