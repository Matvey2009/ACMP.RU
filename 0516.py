n = input()
k = n[::-1]
t1 = t2 = 0 
for i in range(1, int(n)):
	if(int(n)%i == 0):
		t1+=1
for i in range(1, int(k)):
	if(int(k)%i == 0):
		t2+=1
		
if(t1>=0 or t2>=0):
	print("No")
else:
	print("Yes")

