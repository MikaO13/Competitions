n = int(input())
s = input()
let = {'z':0, 'e':0, 'r':0, 'o':0, 'n':0}
for c in s: let[c] += 1
n1 = min(let['o'], let['n'], let['e'])
n0 = min(let['z'], let['e'] - n1, let['r'], let['o']-n1)

print(('1 ' * n1 + '0 ' * n0)[:-1])