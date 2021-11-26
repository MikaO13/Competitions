for _ in range(int(input())):
    x, y = map(int, input().split())
    if max(x, y) > 2 and min(x, y) > 1:
        print("NO")
    else:
        print("YES")