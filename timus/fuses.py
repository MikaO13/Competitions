a = int(input())
b = int(input())

if (b - a) % 2 == 1:
    print((b - a) // 2 + 1)
else:
    if a % 2 == 1:
        print((b-a)//2 + 1)
    else:
        print((b-a)//2)