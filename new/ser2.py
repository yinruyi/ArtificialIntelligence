#conding:utf-8
from time import ctime  
import os,sys
import io
import time,datetime
import os, struct, socket
import sys, time
import thread
import random
import image_classification_predict_back
import SocketServer  
from SocketServer import StreamRequestHandler as SRH  
reload(sys)
sys.setdefaultencoding('utf-8')

UPLOAD_FOLDER = 'uploads/'
BUFFER_SIZE = 1024000
host = ''  
port = 9999  
addr = (host,port)  

def rename(address='no_address'):
    address = address[0]
    time_ = str(datetime.datetime.now()).replace(' ', '_')
    time_ = time_.replace(':','_')
    address = address.replace('.','_')
    new_img_name = address + time_ + str(random.randint(10000, 1000000)) + '.jpg'
    return UPLOAD_FOLDER+new_img_name

class Servers(SRH):

    def recvall(self, size):
        message = bytearray()
        print "Start receiving image-data"
        # count packages
        i = 0
        # Loop until all expected data is received.
        while len(message) < size:
            buffer = self.request.recv(size - len(message))        
            #print "received package #"+str(i)
            i = i+1
            if not buffer:
                # End of stream was found when unexpected.
                raise EOFError
                #'Could not receive all expected data!'
            message.extend(buffer)
        #print "Finished receiving: "+str(message)
        return bytes(message)

    def handle(self):
        while True:
            packed = self.recvall(struct.calcsize('!I'))
            size = struct.unpack('I', packed)[0]
            data = self.request.recv(BUFFER_SIZE)  
            print("Size of image: "+str(size))
            print('Receiving data from:', 'address')
            data = self.recvall(size)
            new_img_name = rename()
            with open(new_img_name, 'wb') as file:
                file.write(data)
            try:
                message = image_classification_predict_back.Main(new_img_name)
            except:
                message = 'error'
            self.request.send(message)


if __name__ == '__main__':
    print 'server is running....'  
    server = SocketServer.ThreadingTCPServer(addr,Servers)  
    server.serve_forever()  