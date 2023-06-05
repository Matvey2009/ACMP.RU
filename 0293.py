maxi = 0
k = 1
n = int(input())
df = list(map(float, input().split()))
nf = list(map(int, input().split()))
for i in range(n):
	if (maxi < df[i] / 100 * nf[i]):
		maxi = df[i] / 100 * nf[i]
		k = i+1
print(k)
