n, k = list(map(int, input().split()))
s = input()
arr = [0]*128
r=-1
v = 0
for l in range(n):
	while r+1<n and arr[ord(s[r+1])]<k:
		r+=1
		arr[ord(s[r])]+=1
	v+=r+1-l
	arr[ord(s[l])]-=1
print(v)
