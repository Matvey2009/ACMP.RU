n = int(input())
polka = []
final = []
for i in range(n):
	arr = list(map(int, input().split()))
	if arr[0] == 1:
		polka.insert(0, arr[1])
	elif arr[0] == 2:
		polka.append(arr[1])
	elif arr[0] == 3:
		final.append(polka[0])
		polka.pop(0)
	elif arr[0] == 4:
		final.append(polka[len(polka)-1])
		polka.pop(len(polka)-1)
print(*final)

