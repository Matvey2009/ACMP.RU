ur = input()
p, v, t, z = ur[0], ur[2], ur[4], ur[1]
if(p == "x"):
	if(z == "+"):
		print(int(t) - int(v))
	else:
		print(int(v) + int(t))
		
if(v == "x"):
	if(z == "+"):
		print(int(t) - int(p))
	else:
		print(int(p) - int(t))
		
if(t == "x"):
	if(z == "+"):
		print(int(p) + int(v))
	else:
		print(int(p) - int(v))
