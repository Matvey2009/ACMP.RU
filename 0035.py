k = int(input())
arr = []
for i in range(k):
    n, m = map(int, input().split())
    arr.append(19 * m + (n + 239)*(n + 366) // 2)
for d in arr:
    print(d)