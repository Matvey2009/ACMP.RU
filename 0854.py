tr, tk = map(int, input().split())
mode = input()

if mode == "freeze":
    S = min(tr, tk)
elif mode == "heat":
    S = max(tr, tk)
elif mode == "auto":
    S = tk
else:
    S = tr

print(S)