for _ in range(int(input())):
    a, b = map(int, input().split())
    if min(a, b)*2 < max(a, b): print(max(a, b)**2)
    else: print((min(a, b)*2)**2)