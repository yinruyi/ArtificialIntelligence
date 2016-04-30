from socket import *  
  
host = '182.92.10.18'  
port = 9999  
bufsize = 1024  
addr = (host,port)  
client = socket(AF_INET,SOCK_STREAM)  
client.connect(addr)  
with open("111.jpg","rb") as img:
	f = img.read()
 
# data = raw_input()
data = f  

client.send('%s\r\n' % data)  
data = client.recv(bufsize)  

print data.strip()  
client.close()  