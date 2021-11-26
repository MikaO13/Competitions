n, c = map(int, input().split())
a = [int(i) for i in input().split()]
t = 1
for i in range(1, n):
    if a[i] - a[i-1] > c:
        t = 1
    else:
        t += 1
print(t)