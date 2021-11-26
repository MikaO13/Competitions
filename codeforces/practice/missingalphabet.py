s = input()
alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
for letter in s:
    alphabet.pop(alphabet.index(letter))
print(''.join(alphabet))