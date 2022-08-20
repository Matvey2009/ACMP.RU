n, i, j = map(int, input().split())
print(min(abs(i-j)-1,n-abs(i-j)-1))
