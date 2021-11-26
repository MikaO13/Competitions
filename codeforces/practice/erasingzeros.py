for _ in range(int(input())):
    s = input()
    t = 0
    c = 0
    l = "start"
    for char in s:
        if char == l:
            c += 1
            l = char
        elif char == '0' and l == 'start':
            l = 'start'
        else:
            if l == '0':
                t += c
            c = 1
            l = char
    print(t)