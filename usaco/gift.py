"""
ID: Mika.di1
LANG: PYTHON3
TASK: gift1
PROG: gift1
"""

fin = open("gift1.in", 'r')
fout = open('gift1.out', 'w')

friends = {}
numfriends = int(fin.readline())

lines = fin.readlines()

numline = -1
for line in lines:
    numline += 1
    if numline <= numfriends:
        friends[line[:-1]] = 0
    else:
        break

currline = numfriends

while currline < len(lines):
    gifter = lines[currline][:-1]
    amt, numppl = map(int, lines[currline + 1].split())
    #print("{} is giving {} people ${}".format(gifter, str(numppl), str(amt)))
    if numppl == 0 or amt == 0:
        pass
    else:
        friends[gifter] = friends[gifter] - amt + (amt % numppl)
        for personLine in range(currline + 2, currline + numppl + 2):
            friends[lines[personLine][:-1]] += amt // numppl
    currline += numppl + 2

for friend in friends:
    fout.write('{} {}\n'.format(friend, str(friends[friend])))

fout.close()
fin.close()