fin = open("lineup.txt", 'r')
fout = open('lineup.out.txt', 'w')

n = int(fin.readline())
cneed = {'Beatrice': [], 'Belinda': [], 'Bella': [], 'Bessie': [], 'Betsy': [], 'Blue': [], 'Buttercup': [], 'Sue': []}
for i in range(n):
    req = fin.readline().split()
    cneed[req[0]].append(req[5])
    cneed[req[5]].append(req[0])
ans = []
for cow in cneed:
    print(cow)
    if cow not in ans:
        if len(cneed[cow]) < 2:
            ans.append(cow)
            if len(cneed[cow]) == 1:
                ans.append(cneed[cow][0])
                if len(cneed[cneed[cow][0]]) > 1:
                    if cneed[cneed[cow][0]][0] != cow:
                        
        else:
            if cneed[cow][0] < cow:
                ans.append(cneed[cow][0])
                ans.append(cow)
                ans.append(cneed[cow][1])
            else: 
                ans.append(cneed[cow][1])
                ans.append(cow)
                ans.append(cneed[cow][0])
    print(ans)
for cow in ans:
    fout.write(cow + '\n')
fout.close()
fin.close()