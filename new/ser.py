#conding:utf-8
from time import ctime  
import os,sys
import io
import time,datetime
import os, struct, socket
import sys, time
import thread
import random
import image_classification_predict
reload(sys)
sys.setdefaultencoding('utf-8')
UPLOAD_FOLDER = 'uploads/'

def rename(address='no_address'):
    address = address[0]
    time_ = str(datetime.datetime.now()).replace(' ', '_')
    time_ = time_.replace(':','_')
    address = address.replace('.','_')
    new_img_name = address + time_ + str(random.randint(10000, 1000000)) + '.jpg'
    return UPLOAD_FOLDER+new_img_name

def recvall(sock, size):
    message = bytearray()
    print "Start receiving image-data"
    # count packages
    i = 0
    # Loop until all expected data is received.
    while len(message) < size:
        buffer = sock.recv(size - len(message))        
        #print "received package #"+str(i)
        i = i+1
        if not buffer:
            # End of stream was found when unexpected.
            raise EOFError
            #'Could not receive all expected data!'
        message.extend(buffer)
    #print "Finished receiving: "+str(message)
    return bytes(message)

def handler(connection, address):
    while True:
        packed = recvall(connection, struct.calcsize('I'))
        size = struct.unpack('I', packed)[0]
        print("Size of image: "+str(size))
        print('Receiving data from:', address)
        data = recvall(connection, size)
        new_img_name = rename(address)
        with open(new_img_name, 'wb') as file:
            file.write(data)
        try:
            message = image_classification_predict.Main(new_img_name)
        except:
            message = 'error'
        connection.send(message)
        #connection.close()


if __name__ == '__main__':
    print 'start'
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 9999))
    server.listen(25)
    while True:
        connection, address = server.accept()
        #print('Sending data to:', address)
        #handler(connection,address)
        thread.start_new_thread(handler,(connection,address))

