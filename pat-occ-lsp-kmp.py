def lps_array(p):
    lps = [0] * len(p)
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = lps[j - 1]

        if p[i] == p[j]:
            j += 1
            lps[i] = j
    return lps
def kmp(s, p):
    lps = lps_array(p)
    j = cnt = 0
    ans = []
    for ch in s:
        while j > 0 and ch != p[j]:
            j = lps[j - 1]
        if ch == p[j]:
            j += 1
        if j == len(p):
            cnt += 1
            ans.append(lps[-1])
            j = lps[j - 1]
    if cnt:
        print(cnt)
        print(*ans)
    else:
        print("No Occurrences")
s = input().strip()
p = input().strip()
kmp(s, p)