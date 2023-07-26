n = input()
arr=[] 	
arrr=[]
for i in n:
	arr.append(i)
	arrr.append(i)

if "0" in arr:
	print("No")
else:
	arr.sort()
	arrr.sort()
	arrr.reverse()
	r = ''.join(arr)
	e = ''.join(arrr)
	t1 = t2 = 0 
	for i in range(2, int(int(e)**0.5)+1):
		if(int(e)%i == 0):
			t2+=1
			break
	for i in range(2, int(int(r)**0.5)+1):
		if(int(r)%i == 0):
			t1+=1
			break
	if t1== 0 and t2==0:
		print("Yes")
	else:
		print("No")

