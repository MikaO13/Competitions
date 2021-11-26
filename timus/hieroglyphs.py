n = int(input())
h = {'a': [], 'b': [], 'c':[], 'd':[], 'e':[], 'f':[], 'g':[], 'h': [], 'i':[], 'j':[], 'k':[], 'l':[], 'm':[], 'n':[], 'o':[], 'p':[], 'q':[], 'r':[], 's':[], 't':[], 'u':[], 'v':[], 'w':[], 'x':[], 'y':[], 'z':[]}

for i in range(n):
    word = input()
    h[word[0]] += [word]

letter = input()

for word in h[letter]:
    print(word)