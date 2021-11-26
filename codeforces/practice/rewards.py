import math
c = map(int, input().split())
m = map(int, input().split())
n = int(input())
tc = 0
tm = 0
for i in c: tc += i
for i in m: tm += i
if math.ceil(tc/5) + math.ceil(tm/10) > n:
    print("NO")
else:
    print("YES")