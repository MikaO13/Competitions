n = int(input())
w = input()
if n < 26:
    print("NO")
else:
    t = []
    for char in w:
        if char.lower() not in t:
            t.append(char.lower())
    if len(t) == 26:
        print("YES")
    else:
        print("NO")