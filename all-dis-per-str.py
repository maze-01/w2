from itertools import permutations
s = input()
ans = sorted(set(''.join(p) for p in permutations(s)))
print(*ans, end="")