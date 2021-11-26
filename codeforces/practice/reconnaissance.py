n, d = map(int, input().split())
t = 0
s = [int(i) for i in input().split()]

for i in range(n):
    for j in range(n):
        if abs(s[i] - s[j]) <= d and i != j:
            t += 1

print(t)