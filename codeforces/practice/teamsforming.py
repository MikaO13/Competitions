n = int(input())
s = [int(i) for i in input().split()]
s.sort()
t = 0
for i in range(0, n, 2):
    t += s[i+1] - s[i]
print(t)