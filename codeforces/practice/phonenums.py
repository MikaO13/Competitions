for _ in range(int(input())):
    n = int(input())
    s = input()
    eight = n
    for i in range(n):
        if s[i] == "8":
            eight = i
            break
    if n - eight >= 11: print("YES")
    else: print("NO")