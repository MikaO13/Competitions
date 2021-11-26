import random
ph = []
pb = [[], [], [], []]

while True:
    o = input("would you like to draw or play? >> ")
    if o == "draw":
        for i in range(4):
            n = int(input("how many tiles would you like to draw? (remember you will see this once for each bag; enter for current bag) >> "))
            for j in range(n):
                t = random.choice(pb[i])
                print(t)
                alert(t)
                pb[i].remove(t)
                ph.append(t)
    elif o == "play":
        print("your hand: ", ph)
        alert('your hand: (click enter to continue)')
        alert(ph)
        ri = [r for r in input("enter tiles >> ").split()]
        for i in ri:
            ph.remove(i) 
    elif o == "quit":
        break
    
    v = input('what would you like to view? >> ')
    if v == 'hand':
        print(ph)
        alert(ph)
    elif v == 'bags':
        print(pb)
        alert(pb)