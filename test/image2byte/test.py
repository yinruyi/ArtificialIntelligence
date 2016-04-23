#conding:utf-8
with open("test.jpg", "rb") as imageFile:
  f = imageFile.read()
  b = bytearray(f)

print b[2],type(b)
import os
import io
import Image
from array import array


image = Image.open(io.BytesIO(b))
image.save("test1.jpg")