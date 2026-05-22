n=int(input())
d=input().strip()
k=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
res=[]
def f(i,s):
    if i==len(d):
        res.append(s);return
    for c in k[ord(d[i])-48]:
        f(i+1,s+c)
if d:
    f(0,"")
    res.sort()
    print(*res,end=" ")