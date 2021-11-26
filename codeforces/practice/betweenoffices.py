n = int(input())
s = input()
ts, tf = 0, 0
l = "N"

for i in range(n):
    if s[i] != l:
        if l == "F":
            ts += 1
        elif l == "S":
            tf += 1
    l = s[i]
if tf > ts:
    print("YES")
else:
    print("NO")