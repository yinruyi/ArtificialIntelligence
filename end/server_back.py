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
from array import array
import struct

reload(sys)
sys.setdefaultencoding('utf-8')

UPLOAD_FOLDER = 'uploads/'
host = ''  
port = 9999  
addr = (host,port)  

def recvall(sock, size):
    message = bytearray()
    #print "Start receiving image-data"
    # count packages
    i = 0
    # Loop until all expected data is received.
    while len(message) < size:
        buffer = sock.recv(size - len(message))    
        print "received package #"+str(i)
        i = i+1
        if not buffer:
            # End of stream was found when unexpected.
            raise EOFError
            print'Could not receive all expected data!'
        message.extend(buffer)
    #print "Finished receiving: "+str(message)
    return bytes(message)

def byte2Img(imgString, address=('no_address',0)):
    #if '<' in imgString and '>' in imgString:
    address = address[0]
    imgString = imgString.replace('<','')
    imgString = imgString.replace('>','')
    time_ = str(datetime.datetime.now()).replace(' ', '_')
    time_ = time_.replace(':','_')
    address = address.replace('.','_')
    new_img_name = address + time_ + str(random.randint(10000, 1000000)) + '.jpg'
    with open(UPLOAD_FOLDER+new_img_name, 'wb') as f:
        f.write(imgString)
    return image_classification_predict_back.Main(UPLOAD_FOLDER+new_img_name)


class Servers(SRH):  
    def handle(self):  
        print 'got connection from ',self.client_address  
        #self.wfile.write('connection %s:%s at %s succeed!' % (host,port,ctime()))  
        while True:  
            #data = self.request.recv(BUFFER_SIZE)  
            #if not data:   
            #    break
            packed = recvall(self.request, struct.calcsize('!I'))
            size = struct.unpack('!I', packed)[0]
            print size
            data = recvall(self.request, size)
            if not data:
                break
            print self.client_address
            msg = byte2Img(data, self.client_address)
            self.request.send(msg)

if __name__ == '__main__':
    print 'server is running....'  
    server = SocketServer.ThreadingTCPServer(addr, Servers)  
    server.serve_forever()  
