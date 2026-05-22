m,n=map(int,input().split())
g=[list(map(int,input().split())) for _ in range(m)]
sx,sy=map(int,input().split())
dx,dy=map(int,input().split())
v=[[0]*n for _ in range(m)]
ans=-1
def dfs(x,y,d):
    global ans
    if (x,y)==(dx,dy):
        ans=max(ans,d)
        return
    v[x][y]=1
    for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx,ny=x+a,y+b
        if 0<=nx<m and 0<=ny<n and g[nx][ny] and not v[nx][ny]:
            dfs(nx,ny,d+1)
    v[x][y]=0
if g[sx][sy] and g[dx][dy]:
    dfs(sx,sy,0)
print(ans,end="")