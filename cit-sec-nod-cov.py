from itertools import combinations
n,m,k = map(int,input().split())
edges = [tuple(map(lambda x:int(x)-1,input().split())) for _ in range(m)] 
found=False
for r in range(k+1):
    for sub in combinations(range(n),r):
        c=set(sub)
        if all(u in c or v in c for u,v in edges):
            print("Yes")
            print(*[x+1 for x in sorted(c)], end=" ")
            found=True
            break
    if found: break
if not found:
    print("No")