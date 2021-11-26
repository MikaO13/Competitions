t = int(input())

for test in range(t):
    n = int(input())
    l = input()
    
    p = ''
    for d in l:
        if d == "S":
            p += "E"
        else:
            p += "S"

    print(p)