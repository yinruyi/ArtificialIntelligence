import os, struct, socket

def recvall(sock, size):
    message = bytearray()

    print "Start receiving image-data"

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
            'Could not receive all expected data!'
        message.extend(buffer)

    #print "Finished receiving: "+str(message)
    return bytes(message)

if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 65000))
    server.listen(5)
    while True:
        connection, address = server.accept()
        #print('Sending data to:', address)
        packed = recvall(connection, struct.calcsize('!I'))
        size = struct.unpack('!I', packed)[0]
        print("Size of image: "+str(size))
        print('Receiving data from:', address)
    	data = recvall(connection, size)
    	with open('112.jpg', 'wb') as file:
            file.write(data)
        connection.close()