n, m = map(int, input().split())
mini = 9999999999
for i in range(n):
	s = input()
	mini = min(mini, s.count('.'))
print(mini)
