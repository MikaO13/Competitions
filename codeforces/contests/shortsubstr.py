for _ in range(int(input())):
    b = input()
    a = b[0]
    for i in range(1, len(b), 2):
        a += b[i]
    print(a)