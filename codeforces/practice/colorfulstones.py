s = input()
t = input()
p = 0
for i in range(len(t)):
    if s[p] == t[i]:
        p += 1
print(p + 1)