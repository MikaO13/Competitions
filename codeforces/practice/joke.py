g = input()
h = input()
l = input()
tp = "YES"
# don't forget to account for no letters

if len(g) + len(h) != len(l):
    print("NO")
else:
    letters = {}
    for i in g:
        if i in letters: 
            letters[i] += 1
        else:
            letters[i] = 1
    for i in h:
        if i in letters: 
            letters[i] += 1
        else:
            letters[i] = 1
            
    letters2 = {}
    for i in l:
        if i in letters2: 
            letters2[i] += 1
        else:
            letters2[i] = 1
    
    for char in letters:
        if letters[char] != letters2[char]:
            tp = "NO"
            break

    print(tp)