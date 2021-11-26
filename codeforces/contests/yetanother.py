n = int(input())
a = [int(i) for i in input().split()]

sm = 0
maxscore = 0
mx = 0

for i in range(n):
    sm += a[i]
    mx = max(a[i], mx)
    maxscore = max(maxscore, sm-mx)
    if sm<0:
        sm = 0
        mx = 0

sm = 0
mx = 0

for i in range(n):
    sm += a[i]
    mx = max(a[i], mx)
    maxscore = max(maxscore, sm-mx)
    if sm-mx<0:
        sm = 0
        mx = 0

print(maxscore)