import errno
import functools
import socket
from tornado import ioloop, iostream
from time import gmtime, strftime


class Connection(object):
    def __init__(self, connection):
        self.stream = iostream.IOStream(connection)
        self._read()

    def _read(self):
        self.stream.read_until('\n', self._eol_callback)

    def _eol_callback(self, data):
        self.handle_data(data)


def connection_ready(sock, fd, events):
    while True:
        try:
            connection, address = sock.accept()
        except socket.error, e:
            if e[0] not in (errno.EWOULDBLOCK, errno.EAGAIN):
                raise
            return
        else:
            connection.setblocking(0)
            CommunicationHandler(connection)


class CommunicationHandler(Connection):
    """Put your app logic here"""
    def handle_data(self, data):
        self.stream.write("OK")
        self._read()
        print "%s" % (strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        print data
        data = bytearray(data)
        print data
        data = repr(data)
        print data

if __name__ == '__main__':
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setblocking(0)
    sock.bind(("", 9999))
    sock.listen(128)

    io_loop = ioloop.IOLoop.instance()
    callback = functools.partial(connection_ready, sock)
    io_loop.add_handler(sock.fileno(), callback, io_loop.READ)
    
    try:
        print "Starting Tornado socketserver"
        io_loop.start()
    except KeyboardInterrupt:
        io_loop.stop()
        print "exited cleanly"
