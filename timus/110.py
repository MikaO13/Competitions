import math
n = int(input())
s = ""
for i in range(n):
    p = int(input())
    if math.sqrt(8*p - 7)%1 == 0.0:
        s += "1 "
    else:
        s += "0 "
print(s[:-1])