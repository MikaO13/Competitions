n = int(input())

for test in range(n):
    tn = input()
    ds = len(tn)
    digits = []
    
    for digit in tn:
        digits.append(digit)
        
    a = ''
    b = ''

    for digit in digits:
        if digit == '4':
            a += '2'
            b += '2'
        else:
            a += digit
            b += '0'

    print(int(a), int(b))