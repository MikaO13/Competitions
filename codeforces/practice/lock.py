n = int(input())
s = input()
c = input()
t = 0
for i in range(n):
    x = max(int(s[i]), int(c[i]))
    y = min(int(s[i]), int(c[i]))
    if x-y <=5:
        t += x-y
    else:
        t += 10 - x + y
print(t)