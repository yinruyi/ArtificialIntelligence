import SocketServer  
from SocketServer import StreamRequestHandler as SRH  
from time import ctime  
import binascii
import Image
from PIL import ImageFile
from array import array
import io
ImageFile.LOAD_TRUNCATED_IMAGES = True
host = ''  
port = 9999  
addr = (host,port)  
BUFFER_SIZE = 1024*16

def byte2Img(imgString):
    with open('test.jpg', 'wb') as f:
        f.write(imgString.replace(' ', '').decode('hex'))
    return ''

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
            ioImage(data)
            '''
            data = bytearray(data) 
            print data
            data = repr(data)
            data = binascii.hexlify(data)
            print type(data),data,len(data)
            print "RECV from ", self.client_address[0]  
            byte2Img(data)
            print 'finish'
            '''
            self.request.send('data')  
print 'server is running....'  
server = SocketServer.ThreadingTCPServer(addr,Servers)  
server.serve_forever()  