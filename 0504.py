K = int(input())
n1, n2, n3 = 'G', 'C', 'V'
for i in range(K % 3):
    n1, n2, n3 = n3, n1, n2
print(n1 + n2 + n3)