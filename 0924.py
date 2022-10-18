arr = []
g = "Yes"
for i in range(4):
	arr.append(list(input()))
for i in range(3):
	for j in range(3):
		if (arr[i][j] == arr[i+1][j] == arr[i][j+1] == arr[i+1][j+1]):
			g = "No"
			break
print(g)
