t = input()
p = input()
r = [str(i) for i in range(len(t) - len(p) + 1) if t[i:i + len(p)] == p]
print(" ".join(r) if r else "No Match")