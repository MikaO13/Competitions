"""
ID: Mika.di1
LANG: PYTHON3
TASK: palsquare
PROG: palsquare
"""

fin = open("palsquare.in", "r")
fout = open("palsquare.out", "w")

symbols = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def dtb(dec,base):
  conv = []
  if dec == 0: conv = '0'
  while dec != 0:
    conv.insert(0,symbols[dec % base])
    dec = dec // base
  return "".join(conv)

b = int(fin.readline())
#b = int(input())

for n in range(1, 300):
    reg = dtb(n, b)
    sq = dtb(n**2, b)
    if str(sq) == str(sq)[len(str(sq))::-1]:
        #print(reg, sq)
        fout.write(str(reg) + " " + str(sq) + "\n")