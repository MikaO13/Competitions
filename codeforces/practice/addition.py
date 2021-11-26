s = [int(i) for i in input().split("+")]

for rnd in range(len(s)-1):
    for bubble in range(len(s)-1-rnd):
        if s[bubble] > s[bubble + 1]:
            s[bubble], s[bubble + 1] = s[bubble + 1], s[bubble]

for i in range(0, len(s)):
    if i == len(s)-1:
        print(s[i])
    else:
        print(s[i], end = "+")