n = int(input())
p = n // 5
t = 0
if (n%5 == 1):#1
	p -= 1
	t += 2
if (n%5 == 2):#2
	p -= 2
	t += 4
if (n%5 == 3):#3
	t += 1
if (n%5 == 4):#4
	p -= 1
	t += 3
print(p, t)
