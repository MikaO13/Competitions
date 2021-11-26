n = int(input())
a = [int(i) for i in input().split()]
ma = 0
mi = a[0]
for i in a:
    ma = max(ma, i)
    mi = min(mi, i)
print(ma - mi - n + 1)