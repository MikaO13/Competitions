"""
ID: Mika.di1
LANG: PYTHON3
TASK: friday
PROG: friday
"""

fin = open("friday.in", 'r')
fout = open("friday.out", "w")
weekday = 1 #sat --> fri
days = [0, 0, 0, 0, 0, 0, 0]

def calcmonth(numdays):
    global weekday
    weekday += 13 # go to the thirtheenth
    days[weekday % 7] += 1
    weekday += numdays - 13
    

for year in range(int(fin.readline())): #starts at 0, goes to N || remember to add 1900 to all years for leap year calc
    for month in range(1, 13):
        if month == 4 or month == 9 or month == 11 or month == 6:
            calcmonth(30)
        elif month == 2:
            if ((year + 1900) % 100 == 0 and (year + 1900) % 400 == 0) or ((year + 1900) % 100 != 0 and (year + 1900) % 4 == 0):
                calcmonth(29)
                print(year + 1900)
            else:
                calcmonth(28)
        else:
            calcmonth(31)

fout.write(str(days[0]) + " " + str(days[1]) + " " + str(days[2]) + " " + str(days[3]) + " " + str(days[4]) + " " + str(days[5]) + " " + str(days[6]) + '\n')

fout.close()
fin.close()