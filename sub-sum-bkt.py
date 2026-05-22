n,t=map(int,input().split())
a=list(map(int,input().split()))
ans=0
def f(i,s,c):
    global ans
    if s==t:
        print("["+" ".join(map(str,c))+"]")
        ans=1
        return
    if i==n or s>t: return
    f(i+1,s+a[i],c+[a[i]])
    f(i+1,s,c)
f(0,0,[])
if not ans: print("No subset found")