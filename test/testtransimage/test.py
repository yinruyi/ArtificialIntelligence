with open("111.jpg","rb") as img:
	f1=img.readline()
with open("test.jpg","rb") as img:
	f2=img.readline()
print len(f1),len(f2)