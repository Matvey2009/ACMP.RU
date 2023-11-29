c, k = map(int, input().split())
maxi = mini = ""
t = c
d = 1
for i in range(k):
	maxi += str(min(9, t))
	t -= 9
	if t <= 0:
		 t = 0
t=c-1
for i in range(k-1):
	mini += str(min(9, t))
	t -= 9
	if t <= 0:
		t = 0
for i in mini:
	d += int(i)
mini = str(c-d+1) + mini[::-1]
print(maxi, mini)

