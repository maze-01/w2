n,m=map(int,input().split())
g=[list(map(int,input().split()))for _ in range(n)]
c=[0]*n
def f(v=0):
    if v==n:return 1
    for x in range(1,m+1):
        for i in range(n):
            if g[v][i] and c[i]==x:break
        else:
            c[v]=x
            if f(v+1):return 1
            c[v]=0
f()
print(*c,end=" ")