import socket
import sys
from time import sleep

HOST, PORT = "localhost", 9999
data = "h"

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((HOST, PORT))
    while True:
        # Connect to server and send data
        sock.sendall(data + "\n")
        # Receive data from the server and shut down
        received = sock.recv(1024)
        print "Sent:     {}".format(data)
        print "Received: {}".format(received)
        sleep(1)
finally:
    sock.close()

