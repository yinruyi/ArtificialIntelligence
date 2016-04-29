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
from PIL import ImageFile
from array import array
import binascii

ImageFile.LOAD_TRUNCATED_IMAGES = True
reload(sys)
sys.setdefaultencoding('utf-8')

UPLOAD_FOLDER = 'uploads/'
BUFFER_SIZE = 1024000
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
    #if '<' in imgString and '>' in imgString:
    imgString = imgString.replace('<','')
    imgString = imgString.replace('>','')
    time_ = str(datetime.datetime.now()).replace(' ', '_')
    time_ = time_.replace(':','_')
    address = address.replace('.','_')
    new_img_name = address + time_ + str(random.randint(10000, 1000000)) + '.jpg'
    with open(UPLOAD_FOLDER+new_img_name, 'wb') as f:
        f.write(imgString.replace(' ', '').decode('hex'))
    return image_classification_predict_back.Main(UPLOAD_FOLDER+new_img_name)
    # else:ls
    # 	return ''

def ioImage(data):
    data = bytearray(data)
    image = Image.open(io.BytesIO(data))
    image.save('savepath.jpg')    

class Servers(SRH):  
    def handle(self):  
        print 'got connection from ',self.client_address  
        self.wfile.write('connection %s:%s at %s succeed!' % (host,port,ctime()))  
        while True:  
            data = self.request.recv(BUFFER_SIZE)  
            if not data:   
                break
            data = bytearray(data)
            with open('data1.txt','wb') as datafile:
                  datafile.write(data)            
            data = repr(data)
            with open('data2.txt','wb') as datafile:
                  datafile.write(data)  
            data = binascii.hexlify(data)
            print type(data),data
            with open('data.jpg','wb') as datafile:
                  datafile.write(data)
            print "RECV from ", self.client_address[0]
            #try:
            msg = byte2Img(data, self.client_address[0])
            #except:
            #    msg = 'error'
            print msg
            self.request.send(msg)

if __name__ == '__main__':
    print 'server is running....'  
    server = SocketServer.ThreadingTCPServer(addr,Servers)  
    server.serve_forever()  
