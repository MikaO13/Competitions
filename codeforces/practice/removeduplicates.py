n = int(input())
a = [int(i) for i in input().split()]
a.reverse()
d = []
for i in a:
    if i not in d: d.append(i)
d.reverse()

print(len(d))
for i in d:
    print(i, end = " ")