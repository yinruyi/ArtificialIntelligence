# -*- coding:utf8 -*-  
  
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')  
  
import socket  
  
class UdpServer(object):  
    def tcpServer(self):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
        sock.bind(('', 9527))       # 绑定同一个域名下的所有机器  
          
        while True:  
            revcData, (remoteHost, remotePort) = sock.recvfrom(1024)  
            print("[%s:%s] connect" % (remoteHost, remotePort))     # 接收客户端的ip, port  
            try:  
                sendDataLen = sock.sendto(calculate(revcData), (remoteHost, remotePort))  
            except:
                sendDataLen = sock.sendto('error', (remoteHost, remotePort))  
            print "revcData: ", revcData  
            print "sendDataLen: ", sendDataLen  
              
        sock.close()  


def calculate(revcData):
    return str(revcData)+'after_cal'

if __name__ == "__main__":  
    udpServer = UdpServer()  
    udpServer.tcpServer()  