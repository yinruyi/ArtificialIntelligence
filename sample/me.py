#coding:utf-8
from array import array
import binascii
import socket
BUFFER_SIZE=1024000

def byte2Img(imgString, address='no_address'):
    #if '<' in imgString and '>' in imgString:
    imgString = imgString.replace('<','')
    imgString = imgString.replace('>','')
    time_ = str(datetime.datetime.now()).replace(' ', '_')
    time_ = time_.replace(':','_')
    address = address.replace('.','_')
    new_img_name = address + time_ + str(random.randint(10000, 1000000)) + '.jpg'
    with open(new_img_name, 'wb') as f:
        f.write(imgString.replace(' ', '').decode('hex'))
    #return image_classification_predict_back.Main(UPLOAD_FOLDER+new_img_name)

if __name__ == '__main__':
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(('',9999))
	sock.listen(5)
	while True:
		connection, address = sock.accept()
		#try:
		connection.settimeout(50)
		data = connection.recv(BUFFER_SIZE)
		data = bytearray(data)
		data = repr(data)
		print data,len(data)
		data = binascii.hexlify(data)
		print "hah"
		msg = byte2Img(data)
		print 'finish'
		#except:
		#	print "time out"
		connection.close()
			

