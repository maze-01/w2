g=[list(map(int,input().split())) for _ in range(9)]
def ok(r,c,x):
    for i in range(9):
        if g[r][i]==x or g[i][c]==x: return 0
    r-=r%3; c-=c%3
    for i in range(3):
        for j in range(3):
            if g[r+i][c+j]==x: return 0
    return 1
def f():
    for i in range(9):
        for j in range(9):
            if g[i][j]==0:
                for x in range(1,10):
                    if ok(i,j,x):
                        g[i][j]=x
                        if f(): return 1
                        g[i][j]=0
                return 0
    return 1
f()
for r in g: print(*r)