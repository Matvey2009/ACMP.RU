ch, m = map(int, input().split())
a1, b1, a2, b2, a3, b3 = map(int, input().split())
k1, k2, k3 = b1/a1, b2/a2, b3/a3

if(max(k1, k2, k3) == k1 and a1 < m):
	ch -= b1
	m -= a1
elif(max(k1, k2, k3) == k2 and a2 < m):
	ch -= b1
	m -= a1
elif(max(k1, k2, k3) == k3 and a3 < m):
	ch -= b1
	m -= a1
