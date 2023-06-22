arr = list(input())
arr.sort()
maxistr = ""
maxi = arr
maxi.reverse()
for i in range(len(arr)):
	maxistr += maxi[i]
arr.reverse()
if(arr[0] == "0"):
	arr[0], arr[1] = arr[1], arr[0]
if(arr[0] == "0"):
	arr[0], arr[2] = arr[2], arr[0]
if(arr[0] == "0"):
	arr[0], arr[3] = arr[3], arr[0]
if(arr[0] == "0"):
	arr[0], arr[4] = arr[4], arr[0]
if(arr[0] == "0"):
	arr[0], arr[5] = arr[5], arr[0]
if(arr[0] == "0"):
	arr[0], arr[6] = arr[6], arr[0]
if(arr[0] == "0"):
	arr[0], arr[7] = arr[7], arr[0]
if(arr[0] == "0"):
	arr[0], arr[8] = arr[8], arr[0]
print(*arr, " ", *maxistr, sep='')
