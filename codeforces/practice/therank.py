n = int(input())
s = []
ts = 0
for i in range(n):
    g = [int(i) for i in input().split()]
    if i == 0: ts = g[0]+g[1]+g[2]+g[3]
    s.append(g[0]+g[1]+g[2]+g[3])
s.sort()
s.reverse()
for i in range(n):
    if s[i] == ts:
        print(i + 1)
        break

