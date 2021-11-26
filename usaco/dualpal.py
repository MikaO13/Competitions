"""
ID: Mika.di1
LANG: PYTHON3
TASK: dualpal
PROG: dualpal
"""

fin = open("dualpal.in", "r")
fout = open("dualpal.out", "w")

symbols = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def dtb(dec,base):
  conv = []
  if dec == 0: conv = '0'
  while dec != 0:
    conv.insert(0,symbols[dec % base])
    dec = dec // base
  return "".join(conv)

def isP(n):
    return str(n) == str(n)[len(str(n))::-1]

n, s = map(int, fin.readline().split())
#n, s = map(int, input().split())

i = 0

while i < n:
    s += 1
    c = 0
    if isP(s): c += 1
    for b in range(2, 10):
        if isP(dtb(s, b)): c += 1
        if c >= 2: 
            #print(s)
            fout.write(str(s) + '\n')
            i += 1
            break
    