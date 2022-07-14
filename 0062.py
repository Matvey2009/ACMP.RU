x = input()
print("BLACK") if (ord(x[0:1]) + int(x[1:2])) % 2 == 0 else print("WHITE")