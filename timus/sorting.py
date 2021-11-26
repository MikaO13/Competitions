n = int(input())

h = [['Slytherin:'], ['Hufflepuff:'], ['Gryffindor:'], ['Ravenclaw:']]

for i in range(n):
    p = input()
    ph = input()
    if ph[0] == "S":
        h[0].append(p)
    elif ph[0] == "H":
        h[1].append(p)
    elif ph[0] == 'G':
        h[2].append(p)
    else:
        h[3].append(p)

for house in h:
    for s in house:
        print(s)
    print("")

