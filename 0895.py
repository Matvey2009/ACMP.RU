arr = []
for i in range(3):
	arr.append(list(input()))
if (arr[0][0]=='X'and arr[0][1]=='X'and arr[0][2]=='X')or(arr[1][0]=='X'and arr[1][1]=='X'and arr[1][2]=='X')or(arr[2][0]=='X'and arr[2][1]=='X'and arr[2][2]=='X')or(arr[0][0]=='X'and arr[1][0]=='X'and arr[2][0]=='X')or(arr[0][1]=='X'and arr[1][1]=='X'and arr[2][1]=='X')or(arr[0][2]=='X'and arr[1][2]=='X'and arr[2][2]=='X')or(arr[0][0]=='X'and arr[1][1]== 'X'and arr[2][2]=='X')or(arr[0][2]=='X'and arr[1][1]=='X' and arr[2][0]=='X'):
	print('Win')
elif('.' not in arr[0] and '.' not in arr[1] and '.' not in arr[2]):
	print('Draw')
else:
	print('Lose')
