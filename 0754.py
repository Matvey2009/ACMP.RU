M1, M2, M3 = map(int, input().split())
if M1 < 94 or M2 < 94 or M3 < 94 or M1 > 727 or M2 > 727 or M3 > 727:
    print('Error')
else:
    if M1 >= M2 and M1 >= M3:
        print(M1)
    elif M2 >= M1 and M2 >= M3:
        print(M2)
    else:
        print(M3)