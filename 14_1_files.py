with open('workfile') as f:
    read_data = f.read()
f.close()
#7.2.1. Methods of File Objects

f.read()
f.readline()#if f.readline() 
for line in f:
    print(line, end='')
f.write('This is test\n')

value = ('the anser', 42)

s = str(value)
f.write(s)
f.tell()# returns an integer giving the file object’s 
#current position in the file represented as number of bytes from the
#  beginning of the file when in binary mode and an opaque number when in text mode.

#f.seek(offset,from_what)#To change the file object’s position
f = open('worklife', 'rb+')
f.write(b'0123456789abcdef')
f.seek(5)
f.read(1)
f.seek(-3, 2)
f.read(1)

import json
lists = ['love', 'hate', 2009, 1997]
json.dumps(lists)

#json.dump(x, f)
x = json.load(f)