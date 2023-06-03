import math
b = 0
n = int(input())
for i in range(1, n):
	if (n % i != 0 and math.gcd(n, i) == 1):
		b += 1
print(b+1)

#n = int(input())
#result=n
#i=2
#while i*i<=n:
#	i+=1
#	if(n%i==0):
#		while(n%i==0):
#			result-=result//i
#			n=n//i
#if(n>1):
#	result-=result//n
#print(result)
