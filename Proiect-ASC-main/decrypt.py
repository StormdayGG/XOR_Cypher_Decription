import sys
fisier_int = sys.argv[1]
key = sys.argv[2]
fisier_out = sys.argv[3]
f = open(fisier_int)
g = open(fisier_out, "w", encoding = "utf-8")
text = f.read()
textl = len(text) // 8
keyl = len(key)
indice = 0
text_c = ""
for i in range(0, textl):
    nr = 0
    for k in range(7, -1, -1):
        nr = nr + (ord(text[indice]) - 48) * pow(2, k)
        indice += 1
    j = i % keyl
    var = nr ^ ord(key[j])
    text_c = text_c + chr(var)
text_c = str(text_c)
g.write(text_c)
f.close()
g.close()
