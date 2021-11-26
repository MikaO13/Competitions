n = int(input())

t = 0

for i in range(n):
    s = [i for i in input().split()]
    st = 0
    for i in s:
        if i == "1":
            st += 1
    if st >= 2:
        t += 1

print(t)