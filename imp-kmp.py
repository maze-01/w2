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
def kmp(text, pattern):
    lps = lps_array(pattern)
    j = 0
    ans = []
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            ans.append(i - len(pattern) + 1)
            j = lps[j - 1]
    if ans:
        print(*ans, end=" ")
    else:
        print("No Match", end="")
text = input()
pattern = input()
kmp(text, pattern)