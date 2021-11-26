n, k = map(int, input().split())
s = [int(i) for i in input().split()]
ki = s[k - 1]
t = 0
for i in s:
    if (i > 0 and i >= s[k-1]):
        t += 1
print(t)