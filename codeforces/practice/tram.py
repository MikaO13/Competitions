n = int(input())

m = 0
c = 0

for i in range(n):
    a, b = map(int, input().split())
    c -= a
    c += b
    if c > m:
        m = c

print(m)