import math
l, c, n = map(int, input().split())

tl = 0
cl = 0

for w in range(n):
    word = input()
    cwl = len(word)
    if cl + cwl > c:
        tl += 1
        cl = cwl + 1
    else:
        cl += cwl + 1

print(math.ceil((tl + 1) / l))