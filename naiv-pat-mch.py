text = input()
pattern = input()
ans = []
for i in range(len(text) - len(pattern) + 1):
    if text[i:i + len(pattern)] == pattern:
        ans.append(str(i))
if ans:
    print(*ans, end=" ")
else:
    print("No Match")