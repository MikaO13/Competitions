n, k, l = map(int, input().split())
indexs = [int(i) for i in input().split()]
# max h-index is n - can stop once the n papers are good
totalcites = k*l
tofix = [i for i in indexs if i < n]
goodnum = len(indexs) - len(tofix)
goodindex = goodnum
for i in range(k):
    for j in range(min(l, len(tofix))):
        c = j
        while tofix[c] > goodindex:
            c += 1
        tofix[c] += 1
        if tofix[c] == good + 1: good += 1
print(tofix)