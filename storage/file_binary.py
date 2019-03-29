bdata = bytes(range(0, 256))
print(len(bdata))
print(bdata)

fout = open('bfile', 'wb')
fout.write(bdata)
fout.close()

fin = open('bfile', 'rb')
bdata = fin.read()
len(bdata)
print(bdata)
fin.close()


with open('bfile', 'wb') as fout:
    fout.write(bdata)

fin = open('bfile', 'rb')
print(fin.tell())
fin.seek(255)
bdata = fin.read()
print(bdata)

fin.seek(-1, 2)
bdata = fin.read()
print(bdata)
fin.close()

fin = open('bfile', 'rb')
fin.seek(254, 0)
fin.seek(1, 1)
bdata = fin.read()
print(bdata)
fin.close()