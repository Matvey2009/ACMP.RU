a = int(input())
b = str(bin(a))
c = 0
for i in b[2:len(b)]:
    c += int(i)
print(a+c)
input()