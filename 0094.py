N, M, K = map(int, input().split())
if(N >= M):
	print(1)
elif(N <= K):
	print("NO")
else:
	print((M-N-1)//(N-K)+2)
