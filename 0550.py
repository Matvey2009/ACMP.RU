n = int(input())
if (n % 400 == 0) or (n % 4 == 0 and n % 100 != 0):
    print('12/09/' + f'{n:04}')
else:
    print('13/09/' + f'{n:04}')