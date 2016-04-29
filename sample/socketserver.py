import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data
        self.request.sendall("OK")

if __name__ == "__main__":
    HOST, PORT = "", 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    print "Starting socketserver at %s:%s" % (HOST, PORT)
    server.serve_forever()
