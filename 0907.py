W, H, R = map(int, input().split())
R *= 2
if R <= W and R <= H:
    print('YES')
else:
    print('NO')