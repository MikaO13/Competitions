for _ in range(int(input())):
    n = int(input())
    angle = 360/n
    if 90 % angle == 0 or n%2 == 0: print("YES")
    else: print("NO")