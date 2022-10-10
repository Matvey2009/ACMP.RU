n, m, d, k = map(int, input().split())
a = n * d * k 
u = m * d * k
p = n * m * d * d
print(a + u - p)
