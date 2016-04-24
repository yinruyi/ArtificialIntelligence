import socket


host = '192.168.1.120'

port = 9527

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host , port))



f = open("test.jpg", "r")

while True:

    veri = f.readline(512)
    print veri
    if not veri:

        break

    s.send(veri)

f.close()

print "resim gonderildi"

s.close()