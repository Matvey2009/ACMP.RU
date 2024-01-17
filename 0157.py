f = [0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 20922789888000]
c = input()
r = f[len(c)]
for i in set(c):
	r//=f[c.count(i)]
print(r)

#import itertools
#x = list(input())
#permutations = list(itertools.permutations(x))
#print(len(list(set(permutations))))

#x = input()
#arr = []
#for i in range(len(x)):
#	t = x[i]
#	for j in range(i+1, len(x)):
#		t+=x[j]
#		print(t)o
#		arr.append(t)
#le = len(x)-1
#for i in range(len(x)):
#	t = x[i]
#	while le != 0:
#		t+=x[-le]
#		print(t)
#		arr.append(t)
#		le-=1
#arr = list(set(arr))
#print(len(arr)+factlen(x))


#print(fact(len(list(x)))//fact(len(list(x)) - len(list(set(x)))+1))
