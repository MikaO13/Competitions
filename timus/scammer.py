n = int(input())

names = {}

for i in range(n):
    name = input()
    if name in names:
        names[name] += 1
    else:
        names[name] = 1

for name in names:
    if names[name] > 1:
        print(name)