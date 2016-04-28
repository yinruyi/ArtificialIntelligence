#conding:utf-8
import SocketServer  
from SocketServer import StreamRequestHandler as SRH  
from time import ctime  
import os,sys
import io
import time,datetime
import socket
import random
import image_classification_predict_back
import Image
from array import array

reload(sys)
sys.setdefaultencoding('utf-8')

UPLOAD_FOLDER = 'uploads/'
BUFFER_SIZE = 1024000*10
host = ''  
port = 9999  
addr = (host,port)  

def saveImg(imgString, address='no_address'):
    time_ = str(datetime.datetime.now()).replace(' ', '_')
    time_ = time_.replace(':','_')
    address = address.replace('.','_')
    new_img_name = address + time_ + str(random.randint(10000, 1000000)) + '.jpg'
    with open(UPLOAD_FOLDER+new_img_name,'wb') as img:
        img.write(imgString)
    return image_classification_predict_back.Main(UPLOAD_FOLDER+new_img_name)



def byte2Img(imgString, address='no_address'):
    if '<' in imgString and '>' in imgString:
        imgString = imgString.replace('<','')
        imgString = imgString.replace('>','')
        time_ = str(datetime.datetime.now()).replace(' ', '_')
        time_ = time_.replace(':','_')
        address = address.replace('.','_')
        new_img_name = address + time_ + str(random.randint(10000, 1000000)) + '.jpg'
        with open(UPLOAD_FOLDER+new_img_name, 'w') as f:
            f.write(imgString.replace(' ', '').decode('hex'))
        return image_classification_predict_back.Main(UPLOAD_FOLDER+new_img_name)
    else:
    	return ''


class Servers(SRH):  
    def handle(self):  
        print 'got connection from ',self.client_address  
        self.wfile.write('connection %s:%s at %s succeed!' % (host,port,ctime()))  
        while True:  
            data = self.request.recv(BUFFER_SIZE)  
            if not data:   
                break  
            print data  
            print "RECV from ", self.client_address[0]
            try:
                msg = byte2Img(data, self.client_address[0])
            except:
                msg = 'error'
            self.request.send(msg)

if __name__ == '__main__':
    print 'server is running....'  
    server = SocketServer.ThreadingTCPServer(addr,Servers)  
    server.serve_forever()  