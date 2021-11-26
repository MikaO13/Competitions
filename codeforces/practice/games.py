n = int(input())
h = []
g = []
t = 0

for i in range(n):
    a, b = map(str, input().split())
    h.append(a)
    g.append(b)

for i in range(n):
    c = h[i]
    for j in range(n):
        if i != j:
            if g[j] == h[i]:
                t += 1
print(t)