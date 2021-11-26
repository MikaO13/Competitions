n, k = map(int, input().split())
ess = k-(n+1)*2
acs = 0

for i in range(n):
    b, g = map(int, input().split())
    ess += b
    acs += g

x = ess - acs

if x >= 0:
    print(x)
else:
    print("Big Bang!")