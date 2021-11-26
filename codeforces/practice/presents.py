n = int(input())
p = [int(i) - 1 for i in input().split()]
g = [0 for i in range(n)]

for i in range(n):
    g[p[i]] = i

for i in range(n):
    if i == n - 1:
        print(g[i] + 1)
    else:
        print(g[i] + 1, end = " ")