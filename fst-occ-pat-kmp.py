def lps(p):
    l=[0]*len(p)
    j=0
    for i in range(1,len(p)):
        while j and p[i]!=p[j]:
            j=l[j-1]
        if p[i]==p[j]:
            j+=1
            l[i]=j
    return l
s=input()
p=input()
l=lps(p)
j=0
for i in range(len(s)):
    while j and s[i]!=p[j]:
        j=l[j-1]
    if s[i]==p[j]:
        j+=1
    if j==len(p):
        print(i-j+1,end="")
        break
else:
    print(-1,end="")