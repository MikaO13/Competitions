n = int(input())
p = [i for i in input().split()]
s = "EASY"
for i in p:
    if i == "1": 
        s = "HARD"
        break
print(s)