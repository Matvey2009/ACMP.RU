k1, l1, m1 = map(int, input().split())
k2, l2, m2 = map(int, input().split())
k = min((k1 - (k1*l1//100)), (k2 - (k2*l2//100)))
print((k1-k) * m1 + (k2-k) * m2)






# ~ k1, l1, m1 = map(int, input().split())
# ~ k2, l2, m2 = map(int, input().split())
# ~ s = (k1//100*l1*m1) + (k2//100*l2*m2)
# ~ if(k1 > k2):
	# ~ s += (k1 - k2) * m1
# ~ elif (k1 < k2):
# ~ s += (k2 - k1) * m2
# ~ print(s)
