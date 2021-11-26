a = input().lower()
b = input().lower()

def compare(a, b):
    for i in range(0,len(a)):
        if(a.lower()[i]<b.lower()[i]):
            return -1
        elif(a.lower()[i]>b.lower()[i]):
            return 1
    return 0


print(compare(a, b))