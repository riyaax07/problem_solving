s = "ababaab"
last_seen = {}
results = [-1] * len(s)
for i in range(len(s) - 1, -1, -1):
    ch = s[i]
    if ch in last_seen:
        distance = last_seen[ch] - i - 1
        results[i] = -1 if distance > 1 else distance
    else:
        results[i] = -1
    last_seen[ch] = i
print(*results)
