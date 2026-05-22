n=int(input())
e=int(input())
INF=10**9
g=[[INF]*n for _ in range(n)]
for i in range(n): g[i][i]=0
for _ in range(e):
    s,d,w=map(int,input().split())
    g[s-1][d-1]=w
for k in range(n):
    for i in range(n):
        for j in range(n):
            if g[i][k]+g[k][j]<g[i][j]:
                g[i][j]=g[i][k]+g[k][j]
for i in range(n):
    print(*(x if x<INF else "INF" for x in g[i]),end=" ")
    print()