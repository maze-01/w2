from itertools import combinations
n,m=map(int,input().split())
edges=[tuple(map(int,input().split())) for _ in range(m)]
best=None
for r in range(1,n+1):
    for sub in combinations(range(n),r):
        c=set(sub)
        if all(u in c or v in c for u,v in edges):
            best=sub;break
    if best:break
print(*best)