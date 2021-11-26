n = int(input())

tp = 2

for i in range(n):
    p = input()
    tp += 1
    if p[-4:] == "+one":
        tp += 1

if tp == 13:
    tp += 1

print(tp*100)