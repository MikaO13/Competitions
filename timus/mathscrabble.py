import random
ph = []
pb = [['x', 'x', 'x', 'x', 'x', '/', '/', '/', '/', '/'], ['+', '+', '+', '+', '+', '-', '-', '-', '-', '-'], ['2', '2', '2', '5', '5', '5'], ['1', '1', '1', '3', '3', '3', '4', '4', '4', '6', '6', '6', '7', '7', '7', '8', '8', '8', '9', '9', '9']]
th = []
tb = [['x', 'x', 'x', 'x', 'x', '+', '+', '+', '+', '+'], ['/', '/', '/', '/', '/', '-', '-', '-', '-', '-'], ['1', '1', '1', '2', '2', '2', '3', '3', '3', '4', '4', '4'], ['5', '5', '5', '6', '6', '6', '7', '7', '7', '8', '8', '8', '9', '9', '9']]

while True:
    p = input("who is player? ")
    o = input("would you like to draw or play? ")
    if p == "t":
        if o == "d":
            for i in range(4):
                n = int(input("how many tiles would you like to draw? "))
                for j in range(n):
                    t = random.choice(tb[i])
                    print(t)
                    tb[i].remove(t)
                    th.append(t)
        elif o == "p":
            print("trip's hand: ", th)
            ri = [r for r in input("enter tiles >> ").split()]
            for i in ri:
                th.remove(i) 
    elif p == "p":
        if o == "d":
            for i in range(4):
                n = int(input("how many tiles would you like to draw? "))
                for j in range(n):
                    t = random.choice(pb[i])
                    print(t)
                    pb[i].remove(t)
                    ph.append(t)
        elif o == "p":
            print("potatos hand: ", ph)
            ri = [r for r in input("enter tiles >> ").split()]
            for i in ri:
                ph.remove(i)
    if o == "quit":
        break
    
    v = input('what would you like to view? ')
    if v == 'ph':
        print(ph)
    elif v == 'pb':
        print(pb)
    elif v == 'th':
        print(th)
    elif v == 'tb':
        print(tb)