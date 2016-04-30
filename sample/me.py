#coding:utf-8
from array import array
import binascii
import socket
import time,datetime
import random

BUFFER_SIZE=1024*16

def byte2Img(imgString, address='no_address'):
    with open('test.jpg', 'wb') as f:
        f.write(imgString.replace(' ', '').decode('hex'))
    #return image_classification_predict_back.Main(UPLOAD_FOLDER+new_img_name)

if __name__ == '__main__':
	print "start"
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(('',9999))
	sock.listen(5)
	while True:
		connection, address = sock.accept()
		try:
			connection.settimeout(5)
			data = connection.recv(BUFFER_SIZE)
			data = bytearray(data)
			data = repr(data)
			print data,len(data)
			data = binascii.hexlify(data)
			print data,len(data)
			msg = byte2Img(data)
			print 'finish'
		except:
			print "time out"
		#connection.close()
			

