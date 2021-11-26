from sys import stdin
n = sys.stdin.readline()
t = {}
o = []

for i in range(n):
    x = sys.stdin.readline().split()
    t[x[0]] = int(x[1])

for rnd in range(n-1):
    for bubble in range(n-1-rnd):
        print(s)
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