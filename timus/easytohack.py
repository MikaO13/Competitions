st4 = input()

st3 = []
for char in st4:
    st3.append(ord(char) - ord('a'))
# do something if only one character!!!!
st2 = [0 for i in range(len(st4))]

if len(st2) > 1:
    for i in range(1, len(st2)):
        st2[i] = (st3[i] - st3[i-1]) % 26

st2[0] = st3[0] - 5
if st2[0] < 0:
    st2[0] += 26

st1 = ""
for l in st2:
    st1 += chr(l + ord('a'))
print(st1)