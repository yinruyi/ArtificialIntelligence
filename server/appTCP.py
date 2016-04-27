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
BUFFER_SIZE = 4096

def saveImg(imgString):
    time_ = str(datetime.datetime.now()).replace(' ', '_')
    time_ = time_.replace(':','_')
    new_img_name = time_ + str(random.randint(10000, 1000000)) + '.jpg'
    with open(UPLOAD_FOLDER+new_img_name,'wb') as img:
        img.write(imgString)
    return image_classification_predict.Main(UPLOAD_FOLDER+new_img_name)

class TcpServer(object):  
    def tcpServer(self):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
        sock.bind(('', 9999))  
        sock.listen(5)

        while True:
            ss, addr = sock.accept()
            try:
                revcData, (remoteHost, remotePort) = ss.recvfrom(BUFFER_SIZE)  
                print("[%s:%s] connect" % (remoteHost, remotePort))
                try:  
                    sendDataLen = ss.sendto(saveImg(revcData), (remoteHost, remotePort))  
                except:
                    sendDataLen = ss.sendto('error', (remoteHost, remotePort))  
                print "revcData: ", revcData  
                print "sendDataLen: ", sendDataLen
            except ss.timeout:
                print 'timeout'
        sock.close()


        
if __name__ == "__main__":  
    tcpServer = TcpServer()  
    tcpServer.tcpServer()  