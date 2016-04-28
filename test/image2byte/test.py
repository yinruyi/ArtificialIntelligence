#conding:utf-8
with open("test.jpg", "rb") as imageFile:
  f = imageFile.read()
  b = bytearray(f)
  print b,type(b)
