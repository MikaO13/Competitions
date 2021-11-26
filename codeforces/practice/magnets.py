n = int(input())
prev = ""
t = 0
for i in range(n):
    m = input()
    if m[0] != prev:
        prev = m[0]
        t += 1
print(t)