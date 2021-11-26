cards = list(map(int, input().split()))
d = {}
for card in cards:
    if card not in d:
        d[card] = 1
    else:
        d[card] += 1

biggest = 0 #min(3, d[card])
t = 0
for card in d:
    if card*min(3, d[card]) > biggest and d[card] > 1:
        biggest = card*min(3, d[card])
    t += card*d[card]

print(t - biggest)