l = input()
if l == "{}": print(0)
elif len(l) == 3: print(1)
else:
    le = l[1:-1]
    let = le.split(', ')
    lett = []
    lette = 0
    for letter in let: 
        if letter not in lett:
            lett.append(letter)
            lette += 1
    print(lette)