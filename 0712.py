w, h, n, = map(int, input().split())
w, h = min(w, h), max(w, h)
mini, maxi = w, h
while True:
	maxi += maxi
	while mini < maxi-(h-w):
		mini += mini
	print(maxi, mini)
	break
