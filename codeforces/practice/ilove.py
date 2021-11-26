n = int(input())
s = [int(i) for i in input().split()]
t = 0
mi = s[0]
ma = s[0]

for i in s:
    if i > ma:
        t += 1
        ma = i
    elif i < mi:
        t += 1
        mi = i

print(t)