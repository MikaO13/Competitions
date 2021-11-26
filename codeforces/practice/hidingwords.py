import random
wordfile = open('wordlist.txt','r')
words = wordfile.readlines()
wordfile.close()
wordlist = []
for each in words:
    wordlist.append(each)

currword = ''

for i in range(41):
    while True: 
        alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
        orig = wordlist[random.randrange(len(wordlist))] #pick a random word
        orig = orig[:-1]
        orig = orig.upper()
        good = True
        for char in orig:
            if char in alphabet:
                alphabet.pop(alphabet.index(char))
            else:
                good = False
                break
        if good:
            print(''.join(alphabet))
            print('||'+orig+'||')
            break