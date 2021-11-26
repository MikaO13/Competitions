n = int(input())
s = [i for i in input().split()]
c = []
m = []
p = []
for i in range(n):
    if s[i] == "1": c.append(i + 1)
    elif s[i] == "2": m.append(i + 1)
    elif s[i] == "3": p.append(i + 1)

b = len(c)
for i in [c, m, p]:
    if len(i) < b:
        b = len(i)

print(b)

for i in range(b):
    print(c[i], m[i], p[i])