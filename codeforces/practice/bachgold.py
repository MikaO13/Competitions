n = int(input())

if n%2==0:
    print(n//2)
    for i in range(n//2):
        if i == n//2 - 1:
            print(2)
        else:
            print(2, end = " ")
else:
    print(n//2)
    for i in range(n//2):
        if i == n//2 - 1:
            print(3)
        else:
            print(2, end = " ")