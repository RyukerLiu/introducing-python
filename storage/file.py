poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

print(len(poem))

fout = open('relativity', 'wt')
x = fout.write(poem)
print(x)
fout.close()

fout = open('relativity_print_1', 'wt')
x = print(poem, file=fout)
print(x)
fout.close()

fout = open('relativity_print_2', 'wt')
x = print(poem, file=fout, sep='',end='')
print(x)
fout.close()

fout = open('relativity_write_2', 'wt')
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    x = fout.write(poem[offset:offset+chunk])
    print(x)
    offset += chunk
fout.close()

try:
    fout = open('relativity', 'xt')
    x = fout.write(poem)
    print(x)
    fout.close()
except FileExistsError:
    print('relativity already exists! That  was a close one.')