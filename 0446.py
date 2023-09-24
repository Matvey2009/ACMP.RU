n, m = map(int, input().split())
rek = voz = ""
for i in range(n):
	rek += input()
for i in range(n):
	voz += input()
voz = "".join(voz.split())
for i in range(n*m):
	if rek[i] == "." or voz[i] == "7":
		continue
	elif rek[i] == "R" and int(voz[i]) <= 3:
		print("NO")
		exit()
	elif rek[i] == "G" and int(voz[i])%2!=0 and int(voz[i])!=4 and int(voz[i])!=0:
		print("NO")
		exit()
	elif rek[i] == "B" and int(voz[i])%2==0 and int(voz[i])!=0:
		print("NO")
		exit()
print("YES")
