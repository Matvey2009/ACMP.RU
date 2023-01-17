k=0
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
n = int(input())
for i in range(n):
	x3, y3 = map(int, input().split())
	sl = (abs(y1-y3)**2+abs(x1-x3)**2)**0.5
	cl =((abs(y2-y3)**2+abs(x2-x3)**2)**0.5)/2
	if (sl <= cl):
		print(i+1)
		k = 1
		break
if k != 1:		
	print("NO")
 
