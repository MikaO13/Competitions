n, q = map(int, input().split())
s = input()
ans = []

for i in range(q):
    exclude = list(map(int, input().split())) # all of these will be +1
    segs = [s[0:exclude[0]-1], s[exclude[1]:n+1]]
    c = 0
    for seg in segs:
        uc = {}
        fp = {} # first pos of each color
        for leg in seg:
            if leg not in uc:
                uc[leg] = 1
                fp[leg] = s.index(leg)
                c += 1
            else: uc[leg] += 1
        #print(uc, fp)
        for f in range(len(seg)):
            if uc[seg[f]] > 1:
                good = True
                for j in range(f, len(seg)):
                    if seg[j] > seg[f]: # darker color
                        continue
                    elif seg[j] == seg[f]:
                        continue
                    elif seg[j] < seg[f]:
                        good = False
                        break
                if good == False:
                    c += 1
    ans.append(c)
for i in ans:
    print(i) 