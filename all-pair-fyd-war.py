n=int(input())
INF=10**9; g=[]
for i in range(n):
    r=list(map(int,input().split()))
    for j in range(n):
        if r[j]==-1 and i!=j:
            r[j]=INF
    g.append(r)
for k in range(n):
    for i in range(n):
        for j in range(n):
            if g[i][k]+g[k][j]<g[i][j]:
                g[i][j]=g[i][k]+g[k][j]
for i in range(n):
    for j in range(n):
        print(g[i][j] if g[i][j]!=INF else "INF",end=" ")
    print()