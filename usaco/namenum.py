"""
ID: Mika.di1
LANG: PYTHON3
TASK: namenum
PROG: namenum
"""

fin = open("namenum.in.txt", "r")
fout = open("namenum.out", "w")

cowid = fin.readline()
lenid = len(cowid)
acceptableNames = []

'''

2: A,B,C     5: J,K,L    8: T,U,V
          3: D,E,F     6: M,N,O    9: W,X,Y
          4: G,H,I     7: P,R,S

          '''

for pos in lenid:
    