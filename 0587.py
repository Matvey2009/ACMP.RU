n, m = map(int, input().split())
text = input()
arr = set()
for i in range(n-m+1):
	arr.add(text[i:i+m])
print(len(arr))
