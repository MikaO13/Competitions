n, k = map(int, input().split())
row = list(range(1, n+1))
pos = {num: [num - 1] for num in range(1, n+1)} 
swaps = []
for i in range(k):
    swaps.append(list(map(int, input().split())))
for repeat in range(100):
    for swap in swaps:
        row[swap[0]-1], row[swap[1]-1] = row[swap[1]-1], row[swap[0]-1]
        if swap[1]-1 not in pos[row[swap[1]-1]]: # note this will actually be 1 since we swapped
            pos[row[swap[1]-1]].append(swap[1]-1)
        if swap[0]-1 not in pos[row[swap[0]-1]]: 
            pos[row[swap[0]-1]].append(swap[0]-1)
for i in pos:
    print(len(pos[i]))