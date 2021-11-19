HS, MS = map(int, input().split(':'))
HF, MF = map(int, input().split())
print(str(((HS + HF) + (MS + MF) // 60) % 24).zfill(2) + ':' + str((MS + MF) % 60).zfill(2))