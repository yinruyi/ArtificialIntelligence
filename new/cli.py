import socket, struct
import time
def send(client):
    with open('111.jpg', 'rb') as file:
        data = file.read()
    #print 'image'
    # Construct message with data size.
    size = struct.pack('I', len(data))
    print size,type(size)
    message = size + data
    #print message,type(message)
    print 'msg'
    client.sendall(message)
    print 'send'
    msg = client.recv(1024)
    #client.sendall(message)
    #msg = client.recv(1024)
    print msg

def main(host):
    # Connect to server and get image size.
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, 9999))
    except Exception as e:
        print str(e)
    while True:
        #pass
        send(client)
        time.sleep(0.5)
        print 'hello'
    #send(client)
    client.close()

if __name__ == '__main__':
	main('localhost')