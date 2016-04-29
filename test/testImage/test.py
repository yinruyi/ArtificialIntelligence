#conding:utf-8

# with open("test.jpg", "rb") as imageFile:
#   f = imageFile.read()
#   b = bytearray(f)
#   print b,type(b)
f = open('ReleaseNote.txt','r')
line=f.readline()

line = line.replace('<','')
line = line.replace('>','')
#print line,type(line)
with open('test.jpg','w') as img:
	img.write(line)
with open('t.jpg', 'w') as f:
	f.write(line.replace(' ', '').decode('hex'))