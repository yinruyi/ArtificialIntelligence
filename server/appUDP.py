#conding:utf-8
import os,sys
import io
import time,datetime
import socket
import random
import image_classification_predict

reload(sys)
sys.setdefaultencoding('utf-8')

UPLOAD_FOLDER = 'static/uploads/'

def saveImg(imgString):
	time_ = str(datetime.datetime.now()).replace(' ', '_')
	time_ = time_.replace(':','_')
	new_img_name = time_ + str(random.randint(10000, 1000000)) + '.jpg'
	with open(UPLOAD_FOLDER+new_img_name,'wb') as img:
		img.write(imgString)
	return image_classification_predict.Main(UPLOAD_FOLDER+new_img_name)

class UdpServer(object):  
    def tcpServer(self):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
        sock.bind(('', 9527))  
        sock.listen(5)
        while True:
            try:
                revcData, (remoteHost, remotePort) = sock.recvfrom(1024)  
                print("[%s:%s] connect" % (remoteHost, remotePort))
                try:  
                    sendDataLen = sock.sendto(saveImg(revcData), (remoteHost, remotePort))  
                except:
                    sendDataLen = sock.sendto('error', (remoteHost, remotePort))  
                print "revcData: ", revcData  
                print "sendDataLen: ", sendDataLen
            except socket.timeout:
                print 'timeout'
        sock.close()


		
if __name__ == "__main__":  
    udpServer = UdpServer()  
    udpServer.tcpServer()  