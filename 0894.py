s1, r1 = map(float, input().split())
s2 = 3.14159265 * r1 * r1 - s1
r2 = (s2/3.14159265)**0.5
print(round(r2, 3))
