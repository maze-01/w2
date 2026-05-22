k,n=map(int,input().split())
d=[0]*(k+1)
m=0
while d[k]<n:
    m+=1
    for i in range(k,0,-1):
        d[i]+=d[i-1]+1
print(m)