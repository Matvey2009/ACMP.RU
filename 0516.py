n = input()
arr=[] 	
arrr=[]
for i in n:
	arr.append(i)
	arrr.append(i)
if "0" in arr:
	print("No", 1)
else:
	arr.sort()
	arrr.sort()
	arrr.reverse()
	r = ''.join(arr)
	e = ''.join(arrr)
	t1 = t2 = 0 
	for i in range(2, int(e)):
		if(int(e)%i == 0):
			t2+=1
			break
	for i in range(2, int(r)):
		if(int(r)%i == 0):
			t1+=1
			break
	if t1== 0 and t2==0:
		print("Yes")
	else:
		print("No")

