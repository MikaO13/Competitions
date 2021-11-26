n = int(input())

ss = []

t = 0

for i in range(n):
    s = input()
    if s in ss:
        t += 1
    else:
        ss.append(s)

print(t)