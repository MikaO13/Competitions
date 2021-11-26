n, k = map(int, input().split())

bb = [int(i) for i in input().split()]

tk = 0
tl = 0

for b in bb:
    if b > k:
        tl += b-k
        tk += k
    else:
        tk += b

print(tl, n*k-tk)