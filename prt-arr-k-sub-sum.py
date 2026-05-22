n=int(input())
a=list(map(int,input().split()))
k=int(input())
s=sum(a)
if s%k:
    print(0,end="")
else:
    t=s//k
    u=[0]*n
    def f(st,c,cnt):
        if cnt==k-1:
            return 1
        if c==t:
            return f(0,0,cnt+1)
        for i in range(st,n):
            if not u[i] and c+a[i]<=t:
                u[i]=1
                if f(i+1,c+a[i],cnt):
                    return 1
                u[i]=0
        return 0
    print(f(0,0,0),end="")