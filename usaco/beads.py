"""
ID: Mika.di1
LANG: PYTHON3
TASK: beads
PROG: beads
"""

fin = open("beads.in", 'r')
fout = open("beads.out", "w")

def countBeads(necklace):
    total = 0
    color = ''
    for beadNum in range(len(necklace)):
        if color == '':
            if necklace[beadNum] != 'w':
                color = necklace[beadNum]
            total += 1
        else:
            if necklace[beadNum] == color or necklace[beadNum] == "w":
                total += 1
            else:
                return total
    return total

numBeads, beads = map(str, fin.readlines())
bestCount = 0
used = []

beads = beads[:-1]

for splitPlace in range(int(numBeads)):
    total = 0
    necklace = beads[splitPlace:] + beads[:splitPlace]
    if necklace == necklace[::-1]:
        total += countBeads(necklace)
    else:
        total += countBeads(necklace) + countBeads(necklace[::-1])

    if total > bestCount:
        bestCount = total
        bestNecklace = necklace
    

fout.write(str(bestCount) + '\n')
fout.close()
fin.close()