n = input()
count = 0
temp = 0

for i in n:
	if i == "0":
		temp += 1
		count = max(count, temp)
	else:
		temp = 0
print(count)
	
