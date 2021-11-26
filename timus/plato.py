n = int(input())
d = [int(i) for i in input().split()]

d.sort()
d.reverse()

tm = 0
td = 0

for amt in d:
    td += amt

for city in range(n):
    tm += td*d[city]
    td -= d[city]
    tm += td*d[city]

print(tm)