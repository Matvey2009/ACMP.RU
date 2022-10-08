n = int(input())
a = list(map(int, input().split()))
k = int(input())
s = sum(a)
for i in a:
	if(i > k):
		s -= i - k
print(s)
