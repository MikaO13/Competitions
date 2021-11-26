import random
nt = [int(i) for i in input().split()]
signs = ['x', '/', '-', '+']

for i in range(len(nt)):
    n = []
    for j in range(nt[i]):
        a = ""
        for k in range(4):
            num = random.randint(1, 10)
            a += str(num) + random.choice(signs)
            n.append(num)
        print(a[:-1])
    n.sort()
    for i in n:
        print(i, end = ", ")
    print()