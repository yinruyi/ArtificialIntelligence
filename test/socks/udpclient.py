# -*- coding:utf8 -*-  
  
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')  
  
import socket  
  
class UdpClient(object):  
    def tcpclient(self):  
        clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
  
        sendDataLen = clientSock.sendto("[1,1,1,1]", ('182.92.10.18', 9527))  
        recvData = clientSock.recvfrom(1024)  
        print "sendDataLen: ", sendDataLen  
        print "recvData: ", recvData  
          
        clientSock.close()  
          
if __name__ == "__main__":  
    udpClient = UdpClient()  
    udpClient.tcpclient()  