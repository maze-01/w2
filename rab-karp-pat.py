def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    base = 256
    mod = 10**9 + 7
    h = pow(base, m - 1, mod)
    p_hash = t_hash = 0
    for i in range(m):
        p_hash = (p_hash * base + ord(pattern[i])) % mod
        t_hash = (t_hash * base + ord(text[i])) % mod
    ans = []
    for i in range(n - m + 1):
        if p_hash == t_hash and text[i:i + m] == pattern:
            ans.append(str(i))
        if i < n - m:
            t_hash = (
                (t_hash - ord(text[i]) * h) * base
                + ord(text[i + m])
            ) % mod
    print(" ".join(ans) if ans else "No Match")
text = input()
pattern = input()
rabin_karp(text, pattern)