from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor

class IphoneChat(Protocol):
    def connectionMade(self):
        self.factory.clients.append(self)
        print "clients are ", self.factory.clients

    def connectionLost(self, reason):
        self.factory.clients.remove(self)

    def dataReceived(self, data):
    	print data
        file = open('test.jpeg','w')

        file.write(data)
        file.close()


factory = Factory()

factory.clients=[]


factory.protocol = IphoneChat
reactor.listenTCP(9999, factory)
print "Iphone Chat server started"
reactor.run()