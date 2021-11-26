fin = open("gymnastics.in", 'r')
k, n = map(int, fin.readline().split())
s = []
for line in range(k):
    s.append(fin.readline().split())
fin.close()
c = 0
for cow1 in range(1, n+1):
    for cow2 in range(cow1+1, n+1):
        good = True
        if s[0].index(str(cow1)) > s[0].index(str(cow2)):
            greater = str(cow1)
            lesser = str(cow2)
        else: 
            greater = str(cow2)
            lesser = str(cow1)
        for session in range(k):
            if s[session].index(greater) < s[session].index(lesser):
                good = False
                break
        if good: 
            c += 1
fout = open('gymnastics.out', 'w')
fout.write(str(c))