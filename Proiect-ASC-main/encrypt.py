import sys
key = sys.argv[1]
fisier_int = sys.argv[2]
fisier_out = sys.argv[3]
f = open(fisier_int)
g = open(fisier_out, "w")
text = f.read()
nrbin = ""
keyl = len(key)
c = 0
def binar(nr, lung=8):
    b = bin(nr).lstrip("0b")
    b = "0" * (lung - len(b)) + b
    return b
for i in range(0, len(text)):
    j = i % keyl
    text_c = ord(text[i]) ^ ord(key[j])
    nrbin = nrbin + binar(text_c)
    c += 1
g.write(nrbin)
f.close()
g.close()
