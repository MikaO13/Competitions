"""
ID: Mika.di1
LANG: PYTHON3
TASK: milk2
PROG: milk2
"""

fin = open("milk2.in.txt", "r")
fout = open("milk2.out", "w")

numfarmers = fin.readline()
farmers = fin.readlines()

earliestActiveTime = int(farmers[0].split()[0])
latestActiveTime = int(farmers[0].split()[0])

longestIdle = 0
longestActive = 0

print(farmers)

for farmer in range(int(numfarmers)):
    farmerStart, farmerEnd = map(int, farmers[farmer].split())
    
    if farmerStart > latestActiveTime:
        if farmerEnd - farmerStart > longestActive:
            longestActive = farmerEnd - farmerStart
        if farmerStart - latestActiveTime > longestIdle:
            longestIdle = farmerStart - latestActiveTime
        latestActiveTime = farmerEnd
        earliestActiveTime = farmerStart
    else:
        if farmerEnd < latestActiveTime:
            pass
        else:
            latestActiveTime = farmerEnd
            if latestActiveTime - earliestActiveTime > longestActive:
                longestActive = latestActiveTime - earliestActiveTime

fout.write(str(longestActive) + ' ' + str(longestIdle) + '\n')