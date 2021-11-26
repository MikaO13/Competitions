s = input()
t = input()
p = "YES"
if len(s) == len(t):
    for i in range(len(s)):
        if s[i] != t[len(s)-i-1]:
            p = "NO"
            break
else:
    p = "NO"
print(p)