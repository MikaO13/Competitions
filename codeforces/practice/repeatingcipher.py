n = int(input())
s = input()
t = ""
ls = 0
ts = 0
for c in s:
    if ts == 0:
        t += c
        ts = ls + 1
        ls += 1
    else:
        ts -= 1
print(t)