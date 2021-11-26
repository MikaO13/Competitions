overall = 0
lp = 0
slp = 0
mp = 0
pes = [[], [], []]

tv1 = int(input())
pe = [int(i) for i in input().split()] 
pes[0] = pe
tv2 = int(input())
pe = [int(i) for i in input().split()] 
pes[1] = pe
tv3 = int(input())
pe = [int(i) for i in input().split()] 
pes[2] = pe

if tv1 <= tv2 and tv1 <= tv3:
    if tv2 <= tv3:
        slp = 1
        mp = 2
    else:
        slp = 2
        mp = 1
    lp = 0
elif tv2 <= tv1 and tv2 <= tv3:
    if tv1 <= tv3:
        slp = 0
        mp = 2
    else:
        slp = 2
        mp = 0
    lp = 1
else:
    if tv1 <= tv2:
        slp = 0
        mp = 1
    else:
        slp = 1
        mp = 0
    lp = 2

def bin_Search(arr, val):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if val < arr[mid]:
            high = mid - 1
        elif val > arr[mid]:
            low = mid + 1
        else:
            return True
    else:
           return False

for e in pes[lp]:
    if bin_Search(pes[slp], e):
        if bin_Search(pes[mp], e):
            overall += 1

print(overall)