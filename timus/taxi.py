a, b, c, d = map(int, input().split())
f = 10000000000
po = a - b
do = c + d

while True:
    if f < po + b:
        break
    else:
        po += b
        f = po
    if f > do - d:
        break
    else:
        do -= d
        f = do

print(f)