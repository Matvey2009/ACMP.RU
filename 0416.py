n = input()
arr = ["a", "b", "c", "d", "e", "f", "g", "h"]
c = int(n[1])
pos = arr.index(str(n[0]))
if pos-2>=0 and c-1>=1:
	print(arr[pos-2]+str(c-1))
if pos-2>=0 and c+1<=8:
	print(arr[pos-2]+str(c+1))
if pos-1>=0 and c-2>=1:
	print(arr[pos-1]+str(c-2))
if pos-1>=0 and c+2<=8:
	print(arr[pos-1]+str(c+2))
if pos+1<=7 and c-2>=1:
	print(arr[pos+1]+str(c-2))
if pos+1<=7 and c+2<=8:
	print(arr[pos+1]+str(c+2))
if pos+2<=7 and c-1>=1:
	print(arr[pos+2]+str(c-1))
if pos+2<=7 and c+1<=8:
	print(arr[pos+2]+str(c+1))
