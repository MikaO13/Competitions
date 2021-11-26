#s = input()
#s = "mrsoygbpsrprs irdlllldrrrrdlllldrrrr naadp daaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaa algv fbv ar t"
s = "mrsoygbpsrprs irdlllldrrrrdlllldrrrraaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaagjmtw naaaa dlgv fbv ar t"

#grid, lights, marbles, password, pie, pyramid, scale, tournament
correct = [False]*8

#variables
g = ""
l = [False]*9
ld = [' ', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
ws = s.split()
p = ""
v, c = 0, 0
t = ""
w = ""


#checking loop
for char in s:
    #lights
    for i in range(9):
        if char in ld[i]:
            l[i] = not l[i]
            break
    #scale
    if char in 'aeiou': v += 1
    else: 
        if char != " ": c += 1
    if char in 'rps': t += char
    if char in 'roygbp': p += char
    if char in 'rdul': g += char
    if char != " ": w += char

#grid
if g[0:24] == 'rrrrdlllldrrrrdlllldrrrr': correct[0] = True

#lights
correct[1] = True
for i in l:
    if i == False:
        correct[1] = False
        break

#marbles
if ws[0][0] == "m" and ws[1][0] == "i" and ws[2][0] == 'n' and ws[3][0] == 'd':
    correct[2] = True

#password
if w[-9:] == 'lgvfbvart': correct[3] = True

#pie
if p[0:6] == 'roygbp': correct[4] = True

#pyramid
if len(ws) >= 5: 
    if len(ws[-1]) < len(ws[-2])  and len(ws[-2]) < len(ws[-3]) and len(ws[-3]) < len(ws[-4]) and len(ws[-4]) < len(ws[-5]): correct[5] = True

#scale
if v == c: correct[6] = True
print(v, c)
    
#tournament
if t[0:8] == 'rspsrprs': correct[7] = True

print("\ngrid, lights, marbles, password, pie, pyramid, scale, tournament")
print(correct)

#lights graphic
for i in range(3):
    for j in range(3):
        if l[i*3+j] == True: print('x', end = " ")
        else: print('o', end = " ")
    print('')