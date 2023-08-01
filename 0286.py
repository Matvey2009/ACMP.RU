from decimal import Decimal
a = Decimal(input())
b = Decimal(input())
if a < b:
	print("<")
elif a > b:
	print(">")
else:
	print("=")
