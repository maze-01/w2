from itertools import permutations
n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
ans = float('inf')
for p in permutations(range(1, n)):
    cost = 0; prev = 0; ok = True
    for v in p:
        if g[prev][v] == 0:
            ok = False;break
        cost += g[prev][v]
        prev = v
    if ok and g[prev][0]:
        cost += g[prev][0]
        ans = min(ans, cost)
print(ans, end="")