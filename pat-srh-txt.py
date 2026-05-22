t = input()
p = input()
r = [i for i in range(len(t)-len(p)+1) if t[i:i+len(p)] == p]
if r:
    for i in r:
        print(i, end=" ")
else:
    print(-1, end="")