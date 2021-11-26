n, m = map(int, input().split())
c = []
for i in range(n):
    lst = [int(i) for i in input().split()]

    for i in range(1, len(lst)):
        if lst[i] not in c: c.append(lst[i])

t = []
f = True
for i in range(1, n+2):
    if i not in c:
        f = False

if f: print("YES")
else: print("NO")

