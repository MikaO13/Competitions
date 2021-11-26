for _ in range(int(input())):
    s = input()
    z, o = 0, 0
    eso, eeo = 0, 0
    esz, eez = 0, 0
    
    for i in range(len(s)):
        if s[i] == '0': z += 1
        else: o += 1

    for i in range(0, len(s) - 1):
        if s[i] == '1': eso += 1
        else: break
    for i in range(len(s)-1, -1, -1):
        if s[i] == '1': eeo += 1
        else: break
    
    for i in range(0, len(s) - 1):
        if s[i] == '0': esz += 1
        else: break
    for i in range(len(s)-1, -1, -1):
        if s[i] == '0': eez += 1
        else: break

    print(min(z-max(esz, eez), o-max(eso, eeo)))