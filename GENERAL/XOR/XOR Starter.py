
st = "label"

st = [ord(i) for i in st]

for i in st:
    print(chr(i^13), end='')