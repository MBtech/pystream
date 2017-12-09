import socket
import struct

HOST = 'localhost'
PORT = 6000
ADDR = (HOST,PORT)
BUFSIZE = 4096

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(ADDR)
serv.listen(5)

print 'listening ...'
conn, addr = serv.accept()
print 'client connected ... ', addr

def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data

def get_frame():
  l = recvall(conn,4)
  size = struct.unpack('>I', l)[0]
  print size
  packet = recvall(conn,size)
  return packet


