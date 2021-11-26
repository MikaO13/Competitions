for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    o = []
    counter = 0
    for i in a:
        if i == 1: counter += 1
        else:
            if counter >= 1: o.append(counter)
            counter = 0
    if counter >= 1: o.append(counter)

    print(o)