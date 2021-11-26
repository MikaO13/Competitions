n = int(input())
c = [int(i) for i in input().split()]
t = 0
ma = 0
for i in c:
    if i > ma: ma = i

for i in c:
    t += ma - i
print(t)