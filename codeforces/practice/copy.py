for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    s = []
    for i in a:
        if i not in s:
            s.append(i)
    print(len(s))