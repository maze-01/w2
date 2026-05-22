n=int(input())
a=[list(map(int,input().split()))for _ in range(n)]
r=[]
def f(x,y,p):
    if x==n-1 and y==n-1:
        r.append(p)
        return
    a[x][y]=0
    for dx,dy,c in ((1,0,'D'),(0,-1,'L'),(0,1,'R'),(-1,0,'U')):
        i,j=x+dx,y+dy
        if 0<=i<n and 0<=j<n and a[i][j]:
            f(i,j,p+c)
    a[x][y]=1
if a[0][0] and a[-1][-1]:
    f(0,0,'')
print(*r if r else [-1])