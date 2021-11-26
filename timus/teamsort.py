from sys import stdin
n = int(stdin.readline()[:-1])
t = []
s = []

for i in range(n):
    x = stdin.readline()[:-1].split()
    t.append(x[0])
    s.append(int(x[1]))

for rnd in range(n-1):
    for bubble in range(n-1-rnd):
        if s[bubble] < s[bubble + 1]:
            s[bubble], s[bubble + 1] = s[bubble + 1], s[bubble]
            t[bubble], t[bubble + 1] = t[bubble + 1], t[bubble]
    

for i in range(n):
    print(t[i], s[i])

'''
8
1 2
16 3
11 2
20 3
3 5
26 4
7 1
22 4'''