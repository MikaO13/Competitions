r = 0
c = 0
for row in range(5):
    line = [i for i in input().split()]
    for item in range(0, 5):
        if line[item] == "1":
            r = row + 1
            c = item + 1
            break
print(abs(r - 3) + abs(c - 3))