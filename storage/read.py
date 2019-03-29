
# Careful for big size for this case. Will also take big size with memory.
fin = open('relativity', 'rt')
poem = fin.read()
fin.close()
print(len(poem))
print(poem)

#Fragment
poem = ''
fin = open('relativity', 'rt')
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment

fin.close()
print(len(poem))
print(poem)

#Read line
poem = ''
fin = open('relativity', 'rt')
while True:
    line = fin.readline()
    if not line:
        break
    poem += line
fin.close()
print(len(poem))
print(poem)

#Read with iterator
poem = ''
fin = open('relativity', 'rt')
for line in fin:
    poem += line
fin.close()
print(len(poem))
print(poem)

#readlines
fin = open('relativity', 'rt')
lines = fin.readlines()
fin.close()
print(lines)