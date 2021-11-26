"""
ID: Mika.di1
LANG: PYTHON3
TASK: ride
PROG: ride
"""

fin = open('ride.in', 'r')
fout = open('ride.out', 'w')
x,y = map(str, fin.readlines())
x_total, y_total = 1, 1

for char in x:
    x_total *= ord(char) - 64
for char in y:
    y_total *= ord(char) - 64

if (x_total / -54) % 47 == (y_total / -54) % 47:
    fout.write('GO' + '\n')
else:
    fout.write('STAY' + '\n')

fout.close()
fin.close()