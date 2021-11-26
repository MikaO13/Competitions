n, k = map(int, input().split())
a = [int(i) for i in input().split()]
t = 0

for i in range(n):
    if a[i] <= k: 
        t += 1
        a[i] = k + 1
    else: break

for i in range(n-1, -1, -1):
    if a[i] <= k: t += 1
    else: break

print(t)