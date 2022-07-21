n = int(input())
temp = 0
j =-1
for i in range(n):
	v, s = map(int, input().split())
	if (s == 1 and v > temp):
		temp = v
		j = i
print(j+1)
