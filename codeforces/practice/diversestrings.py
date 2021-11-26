for _ in range(int(input())):
    s = input()
    l = []
    ml = False
    for char in s:
        if char in l:
            ml = True
            break
        else:
            l.append(char)
    l.sort()
    a = True
    for i in range(1, len(l)):
        if abs(ord(l[i]) - ord(l[i-1])) != 1:
            a = False
            break

    if a == False or ml == True:
        print("No")
    else:
        print("Yes")