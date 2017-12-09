from camera import VideoCamera
import socket
import struct


camera = VideoCamera()
ADDR = ('localhost', 6000)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
while True:
    frame = camera.get_frame()
    print len(frame)
    msg = struct.pack('>I', len(frame))
    client.send(msg)
    client.sendall(frame)

client.close()
