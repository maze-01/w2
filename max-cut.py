n=int(input())
a,b,c=map(int,input().split())
d=[-1]*(n+1)
d[0]=0
for i in range(n+1):
    if d[i]<0:continue
    for j in (a,b,c):
        if i+j<=n:
            d[i+j]=max(d[i+j],d[i]+1)
print(max(0,d[n]))